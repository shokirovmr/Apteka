from aiogram.fsm.state import StatesGroup, State


class TypeAddStates(StatesGroup):
    name_uz = State()
    name_ru = State()
    name_en = State()
