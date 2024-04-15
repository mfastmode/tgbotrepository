import asyncio
import logging

from aiogram import Bot, Dispatcher
from config_data.config import Config, load_config
from handlers import other_handlers, user_handlers
from keyboards.set_menu import set_commands

async def main():
    # Загружаем конфиг в переменную config
    config: Config = load_config()
    # Создаем объекты бота и диспетчера
    bot = Bot(token=config.tg_bot.token)
    dp = Dispatcher()
    # Регистриуем роутеры в диспетчере
    dp.include_router(user_handlers.router)
    dp.include_router(other_handlers.router)
    # подключаем кнопку меню
    await set_commands(bot)
    await dp.start_polling(bot)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Exit')