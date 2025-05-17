from sqlalchemy import select
# from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.asyncio import AsyncSession

import logging
from bot.utils import setup_logger

from bot.db.session import SessionLocal

from bot.db.models import Users

from datetime import datetime
import pytz


setup_logger()
logger = logging.getLogger(__name__)


def now_msk():
    return datetime.now(pytz.timezone('Europe/Moscow')).strftime("%Y-%m-%d %H:%M:%S")


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
        username: str,
        role='inspector',
        ):
    '''Добавление пользователя в бд'''
    async with SessionLocal() as session:
        new_user = Users(
            user_id=user_id,
            first_name=first_name,
            last_name=last_name,
            username=username
        )
        session.add(new_user)

        try:
            await session.commit()
            return True
        except Exception as e:
            await session.rollback()
            logger.error(f'Не удалось создать учётную запись для user_id={user_id}'
                         f'По причине - {e}')

            return False
