import asyncio
import logging

from tgbot.handlers.feedback import register_feedback
from tgbot.handlers.support import register_support
from tgbot.handlers.sendart import register_sendart
from tgbot.handlers.answer import register_answer
from tgbot.handlers.cancel import register_cancel
from tgbot.handlers.chat import register_chat_button
from tgbot.config import load_config
from tgbot.filters.admin import AdminFilter
from tgbot.handlers.user import register_user
from tgbot.middlewares.environment import EnvironmentMiddleware
from ex import bot, dp

logger = logging.getLogger(__name__)


def register_all_middlewares(dp, config):
    dp.setup_middleware(EnvironmentMiddleware(config=config))


def register_all_filters(dp):
    dp.filters_factory.bind(AdminFilter)


def register_all_handlers(dp):
    register_user(dp)
    register_cancel(dp)
    register_feedback(dp)
    register_support(dp)
    register_sendart(dp)
    register_answer(dp)
    register_chat_button(dp)



async def main():
    logging.basicConfig(
        level=logging.INFO,
        format=u'%(filename)s:%(lineno)d #%(levelname)-8s [%(asctime)s] - %(name)s - %(message)s',
    )
    logger.info("Starting bot")
    config = load_config(".env")

    register_all_middlewares(dp, config)
    register_all_filters(dp)
    register_all_handlers(dp)

    # start
    try:
        await dp.start_polling()
    finally:
        await dp.storage.close()
        await dp.storage.wait_closed()
        await bot.session.close()


if __name__ == '__main__':
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        logger.error("Bot stopped!")
