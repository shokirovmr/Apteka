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
        ],
        [
            KeyboardButton(text="📁 Hamkorlar"),
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

categories_menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="📜 Kategoriyalar ro'yxati"),
            KeyboardButton(text="➕ Kategoriya qo'shish"),
        ],
        [
            KeyboardButton(text="◀️ Orqaga")
        ]
    ],
    resize_keyboard=True
)


partners_menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="📜 Hamkorlar ro'yxati"),
            KeyboardButton(text="➕ Hamkor qo'shish"),
        ],
        [
            KeyboardButton(text="◀️ Orqaga")
        ]
    ],
    resize_keyboard=True
)
