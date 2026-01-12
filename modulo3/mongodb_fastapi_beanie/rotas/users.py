from fastapi import APIRouter, HTTPException
from beanie import PydanticObjectId
from fastapi_pagination import Page
from fastapi_pagination.ext.beanie import apaginate
from modelos import User

router = APIRouter(
    prefix="/users",
    tags=["Users"],
)


@router.get("/", response_model=Page[User])
async def get_users() -> Page[User]:
    return await apaginate(User.find_all()) # equivalente a User.find({})


@router.get("/{user_id}", response_model=User)
async def get_user(user_id: PydanticObjectId) -> User:
    user = await User.get(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user


@router.post("/", response_model=User)
async def create_user(user: User) -> User:
    await user.insert()
    return user


@router.put("/{user_id}", response_model=User)
async def update_user(user_id: PydanticObjectId, user_data: dict) -> User:
    user = await User.get(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    # Atualiza apenas campos presentes no dict
    for key, value in user_data.items():
        setattr(user, key, value)

    await user.save()
    return user


@router.delete("/{user_id}")
async def delete_user(user_id: PydanticObjectId) -> dict:
    user = await User.get(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    await user.delete()
    return {"message": "User deleted"}
