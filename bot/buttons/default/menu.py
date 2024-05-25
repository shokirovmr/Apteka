from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


menu_markup = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="🗒 Dori turlari bo'limi"),
            KeyboardButton(text="🗂 Kategoriyalar bo'limi"),
        ],
        [
            KeyboardButton(text="Dorilar bo'limi"),
            KeyboardButton(text="Doktorlar bo'limi"),
        ]
    ],
    resize_keyboard=True
)

menu_types = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="📜 Dori turlari ro'yxati"),
            KeyboardButton(text="➕ Dori turini qo'shish"),
        ],
        [
            KeyboardButton(text="◀️ Orqaga")
        ]
    ],
    resize_keyboard=True
)