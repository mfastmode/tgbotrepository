from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder
from lexicon.lexicon_ru import LEXICON

inline_main = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Telegram', url='https://t.me/ivan_vkr')],
    [InlineKeyboardButton(text='Telegram channel ', url='https://t.me/prowb_vasilev')]
])



inline_callback = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Корзина', callback_data='basket')],
    [InlineKeyboardButton(text='Каталог', callback_data='catalog')],
    [InlineKeyboardButton(text='Контакты', callback_data='contacts')]
])



'''------------------------- Через Builder ----------------------------------'''

# Функция для формирования инлайн-клавиатуры на лету
def create_inline_kb(width: int,
                     *args: str,
                     last_btn: str | None = None,
                     **kwargs: str) -> InlineKeyboardMarkup:
    # Инициализируем билдер
    kb_builder = InlineKeyboardBuilder()
    # Инициализируем список для кнопок
    buttons: list[InlineKeyboardButton] = []

    # Заполняем список кнопками из аргументов args и kwargs
    if args:
        for button in args:
            buttons.append(InlineKeyboardButton(
                text=LEXICON[button] if button in LEXICON else button,
                callback_data=button))
    if kwargs:
        for button, text in kwargs.items():
            buttons.append(InlineKeyboardButton(
                text=text,
                callback_data=button))

    # Распаковываем список с кнопками в билдер методом row c параметром width
    kb_builder.row(*buttons, width=width)

    if last_btn:
        kb_builder.row(InlineKeyboardButton(
            text=last_btn,
            callback_data='last_btn'
        ))
    # Возвращаем объект инлайн-клавиатуры
    return kb_builder.as_markup()

# Но в user_handlers в где-нибудь в каком-нибудь хендлере надо создать клаву:
#   keyboard = create_inline_kb(3, 'but_1', 'but_2', 'but_3') ----------------- ЭТО АРГИ(ОБЫЧНЫЕ АРГУМЕНТЫ)
#   И добавить в реплай маркап

# keyboard = create_inline_kb(
#    2, 
#    btn_tel='Телефон', 
#    btn_email='email', 
#    btn_website='Web-сайт', 
#    btn_vk='VK', 
#    btn_tgbot='Наш телеграм-бот'
# )              ---------------------------------------------------------------ЭТО КВАРГИ(ИМЕНОВАННЫЕ)