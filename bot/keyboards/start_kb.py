from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


register_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text='Авторизоваться', callback_data='login')],
        [InlineKeyboardButton(text='Зарегистрироваться', callback_data='registry')]
    ]
)

only_reg_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Зарегистрироваться', callback_data='registry')
        ]
    ]
)