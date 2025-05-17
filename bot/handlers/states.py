from aiogram.fsm.state import StatesGroup, State


class NewUser(StatesGroup):
    user_id = State()
    username = State()
    first_name = State()
    last_name = State()
    role = State()
