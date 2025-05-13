from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


register_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Авторизоваться', callback_data='registr')
        ]
    ]
)