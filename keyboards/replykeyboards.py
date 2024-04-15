from aiogram.utils.keyboard import ReplyKeyboardBuilder
from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

''' ------------------------- 1 Способ -------------------------'''

main = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Кнопка 1')],
    [KeyboardButton(text='Кнопка 2')]
], 
                           resize_keyboard=True,
                           one_time_keyboard=True,
                           input_field_placeholder='Выберите пункт меню.')


''' ------------------------- 2 Способ -------------------------'''

# Инициализируем билдер
kb_builder = ReplyKeyboardBuilder()

# Создаем список с кнопками
buttons: list[KeyboardButton] = [
    KeyboardButton(text=f'Кнопка {i + 1}') for i in range(8)
]

# Распаковываем список с кнопками в билдер, указываем, что
# в одном ряду должно быть 3 кнопки
kb_builder.row(*buttons, width=3)


''' ------------------------- 3 Способ -------------------------'''

# Создаем список списков с кнопками
keyboard: list[list[KeyboardButton]] = [
    [KeyboardButton(text=str(i)) for i in range(1, 4)],
    [KeyboardButton(text=str(i)) for i in range(4, 7)]
]

keyboard.append([KeyboardButton(text='7')])

# Создаем объект клавиатуры, добавляя в него кнопки
my_keyboard = ReplyKeyboardMarkup(
    keyboard=keyboard,
    resize_keyboard=True
)