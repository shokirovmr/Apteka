from aiogram.types import Message
from aiogram.filters import CommandStart

from loader import dp

from bot.buttons.default import menu_markup
from bot.filters import PrivateFilter, AdminFilter


@dp.message(PrivateFilter(), CommandStart(), AdminFilter())
async def start_bot(msg: Message):
    await msg.answer("Menu", reply_markup=menu_markup)
