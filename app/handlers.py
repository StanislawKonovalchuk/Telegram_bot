from aiogram import Dispatcher,Bot,F 
from aiogram import Router
from aiogram.filters import CommandStart, Command
from aiogram.types import Message
import json

import app.kaybaerd as kb

router = Router()
scene =dict
with open("Scene.json", "r") as file:
    text = file.read()
    json_data = json.loads(text)
    

@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.reply(f'Hallo', reply_markup=kb.main)

@router.message() 
async def echo_message(message: Message):
    await message.answer(message.text)

@router.message(F.text in )
async def get_buttons(message: Message):
    user_text = message.text.strip()
    response_text = None
    
    for category in json_data["buttons"]:
        for key, value in category.items():
            if user_text in value:
                response_text = value[user_text]["response"]
                break
        if response_text:
            break
