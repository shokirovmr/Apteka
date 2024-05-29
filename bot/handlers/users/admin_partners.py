from typing import Union

from aiogram import F
from aiogram.enums import ContentType
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State
from bot.buttons.default import menu_markup
from bot.buttons.default.menu import partners_menu
from bot.filters import AdminFilter, PrivateFilter
from aiogram.types import Message, CallbackQuery, ReplyKeyboardRemove
from loader import dp, db

from bot.states import PartnersAddStates


@dp.message(PrivateFilter(), lambda msg: msg.text == "📁 Hamkorlar", AdminFilter())
async def partners_show(msg: Message):
    await msg.answer(msg.text, reply_markup=partners_menu)


@dp.message(PrivateFilter(), F.text == "➕ Hamkor qo'shish", AdminFilter(), State(None))
async def partner_add(msg: Union[Message, CallbackQuery], state: FSMContext):
    await msg.delete()
    await msg.answer("Hamkorni logotipini yuboring: ", reply_markup=ReplyKeyboardRemove())
    await state.set_state(PartnersAddStates.image)


@dp.message(PrivateFilter(), PartnersAddStates.image, lambda msg: msg.content_type in [ContentType.PHOTO])
async def partner_add_image(msg: Message, state: FSMContext):
    image_id = msg.photo[-1].file_id
    await db.add_partner(image_id)

    await msg.answer(f"Hamkor muvaffaqiyatli qo'shildi!", reply_markup=partners_menu)
    await state.clear()
