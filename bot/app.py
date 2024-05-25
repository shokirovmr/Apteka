import asyncio
import logging
import sys

from loader import dp, bot, db
import handlers


async def main() -> None:
    await db.connect()
    await dp.start_polling(bot)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
