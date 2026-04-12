import logging

from beanie import PydanticObjectId
from auth.authenticate import authenticate
from auth.hash_password import hash_password, verify_password
from auth.jwt_handler import TokenData, create_access_token
from database.connection import Database
from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from models.users import User, TokenResponse, UserDto

logger = logging.getLogger(__name__)

user_router = APIRouter()

user_database = Database(User)


@user_router.get("")
async def get_all_users(user: TokenData = Depends(authenticate)) -> list[UserDto]:
    logger.info(f"User [{user.username}] is viewing all users.")
    if user.role != "SuperAdmin":
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="Operation not allowed"
        )

    db_users = await user_database.get_all()
    result = []
    for u in db_users:
        result.append(
            UserDto(id=str(u.id), email=u.email, role=u.role, active=u.active)
        )
    return result


@user_router.put("/{id}/status")
async def update_user_status(
    id: PydanticObjectId, user: TokenData = Depends(authenticate)
) -> dict:
    logger.info(f"User [{user.username}] is updating user #{id}' status.")
    if user.role != "SuperAdmin":
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="Operation not allowed"
        )

    db_user = await user_database.get(id)
    if not db_user:
        logger.warning(f"\t The user #{id} NOT Found.")
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User with supplied ID does not exist",
        )

    await db_user.set({User.active: not db_user.active})
    logger.info(f"\t User #[{id}]'s status is updated.")
    return {"message": "User updated successfully."}
