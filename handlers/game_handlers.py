from aiogram import Router, F
from aiogram.types import Message
from keyboards.keyboards import game_kb, yes_or_no_kb
from lexicon.lexicon_en import LEXICON_EN
from services.services import get_bot_choice, get_winner


# Initialization module router 
router = Router()


# This handler will work, when user accepts the game 
@router.message(F.text == LEXICON_EN['yes_button'])
async def process_yes_answer(message: Message):
    await message.answer(text=LEXICON_EN['yes'], reply_markup=game_kb)
    
    
# This handler will work, when user doesn't accept the game 
@router.message(F.text == LEXICON_EN['no_button'])
async def process_no_answer(message: Message):
    await message.answer(text=LEXICON_EN['no'])
    
    
# This handler will work on any in-game buttons 
@router.message(F.text.in_([LEXICON_EN['rock'],
                            LEXICON_EN['paper'],
                            LEXICON_EN['scissors']]))
async def process_game_button(message: Message):
    bot_choice = get_bot_choice()
    await message.answer(text=f'{LEXICON_EN['bot_choice']} '
                              f'- {LEXICON_EN[bot_choice]}')
    winner = get_winner(message.text, bot_choice)
    await message.answer(text=LEXICON_EN['user_won'], reply_markup=yes_or_no_kb)