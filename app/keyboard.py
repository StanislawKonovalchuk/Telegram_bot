import json
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder

main = ReplyKeyboardMarkup(keyboard=[
        [KeyboardButton(text="Привіт")],
        [KeyboardButton(text="Бувай")]
    ])

async def inline_vals(vals: list[str]):
    keyboard = ReplyKeyboardBuilder()
    for val in vals:
        keyboard.add(KeyboardButton(text=val))
    return keyboard.adjust(2).as_markup(resize_keyboard=True)