from aiogram import Router
from aiogram.types import Message
from aiogram.filters import CommandStart

from bot.keyboards import register_kb
router = Router()

@router.message(CommandStart())
async def start_handler(message: Message):
    await message.answer('Запуск бота.', reply_markup=register_kb)