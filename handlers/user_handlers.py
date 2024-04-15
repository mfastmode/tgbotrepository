from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.filters import Command, CommandStart

from lexicon.lexicon_ru import LEXICON_RU
from keyboards.inlinekeyboards import create_inline_kb
import keyboards.replykeyboards as kb


# Инициализируем роутер уровня модуля
router = Router()

# Этот хэндлер срабатывает на команду /start
@router.message(CommandStart())
async def process_start_command(message: Message):
    keyboard = create_inline_kb(3, 'but_1', 'but_2', 'but_3', last_btn='Последняя кнопка')
    await message.answer(text=LEXICON_RU['/start'], reply_markup=keyboard)


# Этот хэндлер срабатывает на команду /help
@router.message(Command(commands='help'))
async def process_help_command(message: Message):
    await message.answer(text=LEXICON_RU['/help'])
    
    
    
'''---------------------- Обработка коллбэков ----------------------''' 

@router.callback_query(F.data == 'basket')
async def basket(callback: CallbackQuery):
    await callback.answer('Вы выбрали корзину', show_alert=True)
    await callback.message.answer('Ваша корзина пуста.', reply_markup=None)
    
    
@router.callback_query(F.data == 'catalog')
async def catalog(callback: CallbackQuery):
    await callback.answer('Вы выбрали каталог', show_alert=True)
    await callback.message.answer('Каталог пуст.')
    
    
@router.callback_query(F.data == 'contacts')
async def contacts(callback: CallbackQuery):
    await callback.answer('Вы выбрали контакты', show_alert=True)
    await callback.message.answer('Контакты не найдены.')
    

# Объединение коллбэков    
'''    
# Этот хэндлер будет срабатывать на апдейт типа CallbackQuery
# с data 'basket' или 'catalog' или 'contacts'
@router.callback_query(F.data.in_(['basket',
                                   'catalog',
                                   'contacts']))
async def process_buttons_press(callback: CallbackQuery):
    await callback.answer()
'''