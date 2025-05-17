from aiogram.fsm.state import StatesGroup, State


class NewUser(StatesGroup):
    user_id = State()
    nicname = State()
    first_name = State()
    last_name = State()
    role = State()
