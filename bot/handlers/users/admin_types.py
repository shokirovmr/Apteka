from aiogram import F
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State
from aiogram.types import Message, ReplyKeyboardRemove
from loader import dp, db

from bot.buttons.default import menu_types
from bot.filters import PrivateFilter, AdminFilter
from bot.states import TypeAddStates


@dp.message(PrivateFilter(), lambda msg: msg.text == "🗒 Dori turlari bo'limi", AdminFilter(), State(None))
async def types_show(msg: Message):
    await msg.answer(msg.text, reply_markup=menu_types)


@dp.message(PrivateFilter(), F.text == "➕ Dori turini qo'shish", AdminFilter(), State(None))
async def type_add(msg: Message, state: FSMContext):
    await msg.answer("🇺🇿 Dori turining o'zbekcha nomini kiriting: ", reply_markup=ReplyKeyboardRemove())
    await state.set_state(TypeAddStates.name_uz)


@dp.message(TypeAddStates.name_uz)
async def type_name_uz(msg: Message, state: FSMContext):
    await state.set_data({'name_uz': msg.text})
    await msg.answer("🇷🇺 Dori turining ruscha nomini kiriting: ")
    await state.set_state(TypeAddStates.name_ru)


@dp.message(TypeAddStates.name_ru)
async def type_name_ru(msg: Message, state: FSMContext):
    await state.update_data({'name_ru': msg.text})
    await msg.answer("🇬🇧 Dori turining inglizcha nomini kiriting: ")
    await state.set_state(TypeAddStates.name_en)


@dp.message(TypeAddStates.name_en)
async def type_name_ru(msg: Message, state: FSMContext):
    await state.update_data({'name_en': msg.text})
    await msg.answer("✅ Dori turi muvaffaqiyatli qo'shildi!")
    await msg.answer("🗒 Dori turlari bo'limi", reply_markup=menu_types)
    data = await state.get_data()
    await db.add_type(**data)
    await state.clear()
