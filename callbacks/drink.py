from enum import Enum
from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import ContextTypes
from states import State
from callbacks.basic import command_with_buttons, YES_NO


class DrinkOptions(Enum):
    drink_type = ["Juice", "Tea", "Coffee", "Other"]
    tea_type = ["Green", "Black", "White", "Herbal"]
    herbal_tea_effect = ["Calm Down", "Energize", "Fall Asleep Faster", "Relieve Cough"]


async def drink(update: Update, context: ContextTypes.DEFAULT_TYPE):
    return await command_with_buttons(
        update,
        context,
        DrinkOptions.drink_type,
        "Please choose the type of the drink",
        State.drink_type,
        user_data_key="Drink type",
        placeholder="Drink type"
    )


async def juice_fruit(update: Update, context: ContextTypes.DEFAULT_TYPE):
    return await command_with_buttons(
        update,
        context,
        YES_NO,
        "Would you like a fruit juice?",
        State.juice_fruit,
        user_data_key="Fruit juice"
    )


async def juice_veggie(update: Update, context: ContextTypes.DEFAULT_TYPE):
    return await command_with_buttons(
        update,
        context,
        YES_NO,
        "Would you like a veggie juice?",
        State.juice_veggie,
        user_data_key="Veggie juice"
    )


async def tea_type(update: Update, context: ContextTypes.DEFAULT_TYPE):
    return await command_with_buttons(
        update,
        context,
        DrinkOptions.tea_type,
        "What type of tea would you like?",
        State.tea_type,
        user_data_key="Tea type",
        placeholder="Tea type"
    )


async def herbal_tea_effect(update: Update, context: ContextTypes.DEFAULT_TYPE):
    return await command_with_buttons(
        update,
        context,
        DrinkOptions.herbal_tea_effect,
        "What effect would you like your herbal tea to have?",
        State.herbal_tea_effect,
        user_data_key="Herbal tea effect",
        placeholder="Herbal tea effect"
    )


async def coffee_milk(update: Update, context: ContextTypes.DEFAULT_TYPE):
    return await command_with_buttons(
        update,
        context,
        YES_NO,
        "Do you want milk in your coffee?",
        State.coffee_milk,
        user_data_key="Coffee with milk"
    )
