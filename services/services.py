import random
from lexicon.lexicon_en import LEXICON_EN


# Fucntion that returns bot random choice 
def get_bot_choice() -> str:
    return random.choice(['rock', 'paper', 'scissors'])


# A function that returns the key from the dictionary for which 
# the value passed as an argument is stored - user choice 
def _normalize_user_answer(user_answer: str) -> str:
    for key in LEXICON_EN:
        if LEXICON_EN[key] == user_answer: break
    return key


# Function that determines the winner 
def get_winner(user_choice: str, bot_choice: str) -> str:
    user_choice = _normalize_user_answer(user_choice)
    rules = {
        'rock': 'scissors',
        'scissors': 'paper',
        'paper': 'rock',
    }
    if user_choice == bot_choice:
        return 'draw'
    elif rules[user_choice] == bot_choice:
        return 'user_won'
    return 'bot_won '