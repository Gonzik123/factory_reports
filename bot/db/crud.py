from sqlalchemy import select
# from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.asyncio import AsyncSession

from bot.utils import setup_logger


# from bot.db.session import SessionLocal

from bot.db.models import Users

setup_logger()


async def check_user(session: AsyncSession, user_id: int):
    '''
    Проверка наличие пользователя в БД
    '''
    result = await session.execute(
        select(Users.user_id).
        where(Users.user_id == user_id)
    )

    id = result.scalar_one_or_none()

    if id:
        return True
    else:
        return None


async def add_user(
        session: AsyncSession,
        user_id: int,
        first_name: str,
        last_name: str,
        nicname: str,
        role='inspector',
        ):
    '''Добавление пользователя в бд'''
    pass
