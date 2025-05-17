from aiogram import Router, F
from aiogram.types import CallbackQuery, Message
from aiogram.fsm.context import FSMContext
from bot.utils import setup_logger


from bot.db.crud import check_user, add_user
from bot.db.session import SessionLocal
from bot.keyboards import only_reg_kb
from bot.handlers.states import NewUser

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
    await state.clear()
    user_id = callback.from_user.id
    username = callback.from_user.username
    await state.set_state(NewUser.user_id)
    await state.update_data(
        user_id=user_id,
        username=username
    )
    await callback.message.answer('Введите ваше имя')
    await state.set_state(NewUser.first_name)
    

@router.message(NewUser.first_name)
async def handler_take_first_name(message: Message, state: FSMContext):
    first_name = message.text.strip()
    await state.update_data(
        first_name=first_name
    )
    await state.set_state(NewUser.last_name)
    await message.answer('Введите вашу фамилию')


@router.message(NewUser.last_name)
async def handler_take_last_name(message: Message, state: FSMContext):
    last_name = message.text.strip()
    await state.update_data(
        last_name=last_name
    )
    await state.set_state(NewUser.last_name)

    data = await state.get_data()
    first_name = data['first_name']
    user_id = data['user_id']
    username = data['username']
    async with SessionLocal() as session:
        result = await add_user(
            session=session, 
            user_id=user_id,
            username=username,
            first_name=first_name,
            last_name=last_name)
        
    if result == True:
        await message.answer(f'Регистраиця прошла успешно, ваши данные:\n'
                             f'Имя: {first_name}'
                             f'Фамилия: {last_name}')
        await state.clear()
        return
    
    await state.clear()
    await message.answer(
        'Произошла ошибка, попробуйте позже.\n'
        'Или обратитесь в тех. поддержку'
    )