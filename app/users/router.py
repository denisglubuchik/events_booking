from fastapi import APIRouter, Depends
from fastapi_users import FastAPIUsers

from app.users.models import Users
from app.users.auth import auth_backend
from app.users.manager import get_users_manager
from app.users.schemas import UserRead, UserCreate
from app.users.dao import UsersDAO

fastapi_users = FastAPIUsers[Users, int](
    get_users_manager,
    [auth_backend]
)


router = APIRouter(
    prefix="/users",
    tags=["Users"]
)


current_user = fastapi_users.current_user()
authenticated_user = fastapi_users.current_user(optional=True)


@router.get("/me")
async def get_user(user: Users = Depends(current_user)) -> UserRead:
    user = await UsersDAO.find_by_id(model_id=user.id)
    return user


router.include_router(
    fastapi_users.get_auth_router(auth_backend),
    prefix="/auth/jwt",
)
router.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate),
    prefix="/auth/register",
)

