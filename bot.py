import asyncio
import logging
from aiogram import Bot, Dispatcher
from config_data.config import Config, load_config
from handlers import game_handlers, other_handlers, command_handlers


# Logger initialization 
logger = logging.getLogger(__name__)


# Function, that configures and starts bot 
async def main():
    # Configuring logging 
    logging.basicConfig(
        level=logging.INFO,
        format='%(filename)s:%(lineno)d #%(levelname)-8s '
               '[%(asctime)s] - %(name)s - %(message)s')
    
    # Display information about the start of the bot launch to the console 
    logger.info('Bot started')
    
    # Load the config into the config variable 
    config: Config = load_config()
    
    # Initializing the bot and dispatcher 
    bot = Bot(token=config.tg_bot.token, parse_mode='HTML')
    dp = Dispatcher()
    
    # Registering routers in the dispatcher 
    dp.include_router(command_handlers.router)
    dp.include_router(game_handlers.router)
    dp.include_router(other_handlers.router)
    
    # Skip the accumulated updates and start polling 
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)
    
    
if __name__ == '__main__':
    asyncio.run(main())