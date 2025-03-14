from aiogram import Dispatcher,Bot,F 
from aiogram import Router
from aiogram.filters import CommandStart, Command
from aiogram.types import Message
import json
import app.keyboard as kb

router = Router()
scene = dict()

with open("buttons.json", "r") as file:
     text = file.read()
     scene.update(json.loads(text))
     print(scene)

@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.reply(f'Hallo', reply_markup=kb.main)

@router.message(F.text.in_(scene.keys()))
async def get_buttons(message: Message):
    user_text = message.text.strip()
    vals = scene[user_text]
    keyboard = await kb.inline_vals(vals[1])
    await message.reply(vals[0], reply_markup=keyboard)
