from typing import Optional

from fastapi import Depends, Request
from fastapi_users import BaseUserManager, IntegerIDMixin, models, schemas, exceptions

from app.users.models import Users, get_users_db
from app.config import settings


class UsersManager(IntegerIDMixin, BaseUserManager[Users, int]):
    reset_password_token_secret = settings.SECRET_KEY_2
    verification_token_secret = settings.SECRET_KEY_2

    async def create(
        self,
        user_create: schemas.UC,
        safe: bool = False,
        request: Optional[Request] = None,
    ) -> models.UP:
        await self.validate_password(user_create.password, user_create)

        existing_user = await self.user_db.get_by_email(user_create.email)
        if existing_user is not None:
            raise exceptions.UserAlreadyExists()

        user_dict = (
            user_create.create_update_dict()
            if safe
            else user_create.create_update_dict_superuser()
        )
        password = user_dict.pop("password")
        user_dict["hashed_password"] = self.password_helper.hash(password)
        user_dict["role_id"] = 1

        created_user = await self.user_db.create(user_dict)

        await self.on_after_register(created_user, request)

        return created_user


async def get_users_manager(user_db=Depends(get_users_db)):
    yield UsersManager(user_db)

