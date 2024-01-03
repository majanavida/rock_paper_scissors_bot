from aiogram import Router
from aiogram.types import Message
from lexicon.lexicon_en import LEXICON_EN


# Initialization module router 
router = Router()


# Handler for messages, that didn't hit other handlers 
@router.message()
async def send_answer(message: Message):
    await message.answer(text=LEXICON_EN['other_answer'])