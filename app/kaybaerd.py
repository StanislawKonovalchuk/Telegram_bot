import json
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

def kaydord_Buttons():
    with open("Scene.json", "r", encoding="utf-8") as file:
        data = json.load(file)

    if isinstance(data, dict):
        buttons_data = data.get("buttons", [])
    else:
        raise ValueError("Невірний формат JSON. Очікується словник.")

    buttons = [[KeyboardButton(text=btn["text"])] for btn in buttons_data if isinstance(btn, dict) and "text" in btn]

    return ReplyKeyboardMarkup(keyboard=buttons, resize_keyboard=True)


main = kaydord_Buttons()
