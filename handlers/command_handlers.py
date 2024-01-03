from aiogram import Router
from aiogram.filters import Command, CommandStart
from aiogram.types import Message
from keyboards.keyboards import yes_or_no_kb
from lexicon.lexicon_en import LEXICON_EN


# Initialization module router 
router = Router()


# This handler will work on command /start 
@router.message(CommandStart())
async def process_command_start(message: Message):
    await message.answer(text=LEXICON_EN['/start'], reply_markup=yes_or_no_kb)
    
    
# This handler will work on command /help 
@router.message(Command(commands=['help']))
async def process_help_command(message: Message):
    await message.answer(text=LEXICON_EN['/help'], reply_markup=yes_or_no_kb)