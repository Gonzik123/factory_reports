from aiogram import Router, F
from aiogram.types import CallbackQuery
from aiogram.fsm.context import FSMContext
from bot.utils import setup_logger


from bot.db.crud import check_user
from bot.db.session import SessionLocal
from bot.keyboards import only_reg_kb


setup_logger()
router = Router()


@router.callback_query(F.data == 'login')
async def handler_login(callback: CallbackQuery):
    '''
    Обработка клавиши "Авторизоваться"
    '''
    await callback.message.delete()  # type: ignore[union-attr]
    user_id = callback.from_user.id
    await callback.message.answer(  # type: ignore[union-attr]
        'Происходит проверка вашего аккаунта в бд...'
    )
    async with SessionLocal() as session:
        result = await check_user(session, user_id)

        if result:
            # wait callback.message.delete()
            await callback.message.answer(  # type: ignore[union-attr]
                                    'Вы уже зарегистированы! \n'
                                    'Вам доступен основной функционал бота.')
            return

        # await callback.message.delete()
        await callback.message.answer(  # type: ignore[union-attr]
                                    'Вас ещё нет в базе. \n'
                                    'Зарегистрироваться?',
                                    reply_markup=only_reg_kb)
        return


@router.callback_query(F.data == 'registry')
async def handler_register(callback: CallbackQuery, state: FSMContext):
    pass
