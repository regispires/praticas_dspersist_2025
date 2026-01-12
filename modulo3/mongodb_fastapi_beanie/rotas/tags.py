from fastapi import APIRouter, Depends
from modelos import Post
from fastapi_pagination import Page, Params, paginate
from fastapi_pagination.ext.beanie import apaginate


router = APIRouter(
    prefix="/tags",
    tags=["Tags"],
)


@router.get("/", response_model=Page[str])
async def get_tags(params: Params = Depends()) -> Page[str]:
    """ 
    Retorna as tags distintas existentes nos posts.
    """
    tags = await Post.distinct("tags")  # Aguarda a lista de tags
    return paginate(tags, params)


@router.get("/{tag}/posts", response_model=Page[Post])
async def get_posts_by_tag(tag: str) -> Page[Post]:
    posts = await apaginate(Post.find(
        Post.tags == tag,
        fetch_links=True  # EAGER: user, comments, comment.user
    ))
    return posts
