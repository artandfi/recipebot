from enum import Enum
from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import ContextTypes
from states import State
from callbacks.basic import command_with_buttons, strs, YES_NO


class DrinkOptions(Enum):
    drink_type = [strs[x] for x in ['juice', 'tea', 'coffee', 'other']]
    tea_type = [strs[x] for x in ['green', 'black', 'white', 'herbal']]
    herbal_tea_effect = [strs[x] for x in ['calm_down', 'energize', 'fall_asleep', 'relieve_cough']]


async def drink(update: Update, context: ContextTypes.DEFAULT_TYPE):
    return await command_with_buttons(
        update,
        context,
        DrinkOptions.drink_type,
        strs['drink_type_prompt'],
        State.drink_type,
        user_data_key=strs['drink_type'],
        placeholder=strs['drink_type']
    )


async def juice_fruit(update: Update, context: ContextTypes.DEFAULT_TYPE):
    return await command_with_buttons(
        update,
        context,
        YES_NO,
        strs['fruit_juice_prompt'],
        State.juice_fruit,
        user_data_key=strs['fruit_juice']
    )


async def juice_veggie(update: Update, context: ContextTypes.DEFAULT_TYPE):
    return await command_with_buttons(
        update,
        context,
        YES_NO,
        strs['veggie_juice_prompt'],
        State.juice_veggie,
        user_data_key=strs['veggie_juice']
    )


async def tea_type(update: Update, context: ContextTypes.DEFAULT_TYPE):
    return await command_with_buttons(
        update,
        context,
        DrinkOptions.tea_type,
        strs['tea_type_prompt'],
        State.tea_type,
        user_data_key=strs['tea_type'],
        placeholder=strs['tea_type']
    )


async def herbal_tea_effect(update: Update, context: ContextTypes.DEFAULT_TYPE):
    return await command_with_buttons(
        update,
        context,
        DrinkOptions.herbal_tea_effect,
        strs['tea_effect_prompt'],
        State.herbal_tea_effect,
        user_data_key=strs['tea_effect'],
        placeholder=strs['tea_effect']
    )


async def coffee_milk(update: Update, context: ContextTypes.DEFAULT_TYPE):
    return await command_with_buttons(
        update,
        context,
        YES_NO,
        strs['coffee_milk_prompt'],
        State.coffee_milk,
        user_data_key=strs['coffee_milk']
    )
