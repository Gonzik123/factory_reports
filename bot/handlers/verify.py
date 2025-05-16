from aiogram import Router, F, Bot
from aiogram.types import Message, CallbackQuery
from bot.utils import setup_logger
setup_logger()

from bot.db.crud import check_user
from bot.db.session import SessionLocal
from bot.keyboards import only_reg_kb

router = Router()

@router.callback_query(F.data == 'login')
async def handler_register(callback: CallbackQuery):
    '''
    Обработка клавиши "Авторизоваться"
    '''
    await callback.message.delete()
    user_id = callback.from_user.id
    await callback.message.answer('Происходит проверка вашего аккаунта в бд...')
    async with SessionLocal() as session:
        result = await check_user(session, user_id)

        if result:
            #wait callback.message.delete()
            await callback.message.answer('Вы уже зарегистированы! \n'
                                        'Вам доступен основной функционал бота.')
            return
        
        #await callback.message.delete()
        await callback.message.answer('Вас ещё нет в базе. \n'
                                    'Зарегистрироваться?', reply_markup=only_reg_kb)
        return


        