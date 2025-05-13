from aiogram import Router, F, Bot
from aiogram.types import Message, CallbackQuery
from bot.utils import setup_logger
setup_logger()


router = Router()

@router.callback_query(F.data == 'registr')
async def handler_register(callback: CallbackQuery):
    await callback.message.delete()
    await callback.message.answer('Происходит проверка вашего аккаунта в бд...')
    