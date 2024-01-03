from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder
from lexicon.lexicon_en import LEXICON_EN


# Creating keyboard using ReplyKeyboardBuilder 


# Create buttons with consent and refusal responses 
button_yes = KeyboardButton(text=LEXICON_EN['yes_button'])
button_no = KeyboardButton(text=LEXICON_EN['no_button'])


# Initialize the builder for the keyboard 
# with the 'Go ahead' and 'I don't want to!' buttons. 
yes_or_no_kb_builder = ReplyKeyboardBuilder()


# Add buttons to the builder with the argument width=2 
yes_or_no_kb_builder.row(button_yes, button_no, width=2)


# Create the keyboard with buttons 'Go ahead' and 'I don't want to!' 
yes_or_no_kb: ReplyKeyboardMarkup = yes_or_no_kb_builder.as_markup(
    one_time_keyboard=True,
    resize_keyboard=True,
)


# Create game buttons 
button_rock = KeyboardButton(text=LEXICON_EN['rock'])
button_paper = KeyboardButton(text=LEXICON_EN['paper'])
button_scissors = KeyboardButton(text=LEXICON_EN['scissors'])


# Initializing the keyboard builder with response options for the game 
game_kb_builder = ReplyKeyboardBuilder()


# Add buttons to the builder with the argument width=3 
game_kb_builder.row(button_rock, button_paper, button_scissors)


# Creating the keyboard builder with response options for the game 
game_kb: ReplyKeyboardMarkup = game_kb_builder.as_markup(
    one_time_keyboard=True,
    resize_keyboard=True
)