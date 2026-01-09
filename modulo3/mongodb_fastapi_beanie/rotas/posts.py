from fastapi import APIRouter, HTTPException
from beanie import PydanticObjectId
from beanie.odm.fields import Link
from fastapi_pagination import Page
from fastapi_pagination.ext.beanie import apaginate
from modelos import Post, PostCreate, Comment, CommentParam, User

router = APIRouter(
    prefix="/posts",
    tags=["Posts"],
)


@router.get("/", response_model=Page[Post])
async def get_posts() -> Page[Post]:
    return await apaginate(Post.find_all(fetch_links=True))


@router.get("/{post_id}", response_model=Post)
async def get_post(post_id: PydanticObjectId) -> Post:
    # EAGER
    post = await Post.get(post_id, fetch_links=True)
    if not post:
        raise HTTPException(status_code=404, detail="Post not found")
    return post


@router.post("/", response_model=Post)
async def create_post(post: PostCreate) -> Post:
    # Extrai o user_id do Link
    user_id = None
    if isinstance(post.user, Link):
        ref = getattr(post.user, "ref", None)
        if ref is not None and getattr(ref, "id", None) is not None:
            user_id = PydanticObjectId(str(ref.id))

    if user_id is None:
        raise HTTPException(status_code=422, detail="Invalid user reference format")

    # Checa existência
    user = await User.get(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    # Opcional: “normaliza” o link para apontar pro doc real
    post.user = user

    await post.insert()

    return post


@router.post("/{post_id}/comments/", response_model=Post)
async def add_comment(post_id: PydanticObjectId, comment: CommentParam) -> Post:
    post = await Post.get(post_id)
    if not post:
        raise HTTPException(status_code=404, detail="Post not found")

    user = await User.get(comment.user)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    # cria o Comment (user é Link[User], então atribuímos o Document)
    comment_new = Comment(user=user, content=comment.content)
    await comment_new.insert()

    # Post.comments é list[Link[Comment]] -> append do Document funciona (vira Link)
    post.comments.append(comment_new)
    await post.save()

    # retorna EAGER
    updated = await Post.get(post.id, fetch_links=True)
    if not updated:
        raise HTTPException(status_code=500, detail="Post updated but could not be loaded")
    return updated


@router.delete("/{post_id}")
async def delete_post(post_id: PydanticObjectId) -> dict:
    post = await Post.get(post_id)
    if not post:
        raise HTTPException(status_code=404, detail="Post not found")

    await post.delete()
    return {"message": "Post deleted"}
