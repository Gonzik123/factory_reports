from sqlalchemy import select
# from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.asyncio import AsyncSession

from bot.utils import setup_logger


from bot.db.session import SessionLocal

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
    async with SessionLocal() as session:
        new_user = Users(
            user_id=user_id,
            first_name=first_name,
            last_name=last_name,
            nicname=nicname
        )
        session.add(new_user)

        try:
            await session.commit()
            return 'Вы были успешно добавлены в БД.'
        except Exception as e:
            await session.rollback()
            print(
                f'У пользователя {user_id}'
                f'произошла ошибка при создание учётной записи - {e}'
                )
            return 'Произошла ошибка. Обратитесь в тех. поддержку.'
