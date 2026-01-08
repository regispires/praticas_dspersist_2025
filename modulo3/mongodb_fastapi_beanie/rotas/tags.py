from fastapi import APIRouter
from modelos import Post

router = APIRouter(
    prefix="/tags",
    tags=["Tags"],
)


@router.get("/", response_model=list[str])
async def get_all_tags() -> list[str]:
    """
    Retorna todas as tags distintas existentes nos posts.
    """
    tags = await Post.distinct("tags")
    return tags


@router.get("/{tag}/posts", response_model=list[Post])
async def get_posts_by_tag(tag: str) -> list[Post]:
    posts = await Post.find(
        Post.tags == tag,
        fetch_links=True  # EAGER: user, comments, comment.user
    ).to_list()
    return posts
