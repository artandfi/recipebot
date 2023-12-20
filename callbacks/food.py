from enum import Enum
from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import ContextTypes
from states import State
from callbacks.basic import buttons, command_with_buttons, strs, YES_NO


class FoodOptions(Enum):
    food = [strs[x] for x in ['snack', 'main_course', 'side_dish', 'soup', 'salad', 'dessert']]
    cooking_type = [strs[x] for x in ['boiled', 'fried', 'baked', 'smoked', 'preserved', 'raw']]
    soup_type = [strs[x] for x in ['clear', 'creamy']]
    flavor = [strs[x] for x in ['sweet', 'sour', 'bitter', 'salty', 'spicy']]
    spicy_level = [strs[x] for x in ['low', 'medium', 'hot']]
    main_ingredient = [strs[x] for x in ['meat', 'seafood', 'fruit', 'veggies', 'other']]
    meat_type = [strs[x] for x in ['chicken', 'pork', 'beef', 'mutton', 'veal', 'rabbit', 'turkey', 'duck', 'venison', 'other']]
    seafood_type = [strs[x] for x in ['white_fish', 'red_fish', 'molluscs', 'squid', 'crustaceans']]


async def food(update: Update, context: ContextTypes.DEFAULT_TYPE):
    return await command_with_buttons(
        update,
        context,
        FoodOptions.food,
        strs['meal_type_prompt'],
        State.meal_type,
        user_data_key=strs['meal_type'],
        placeholder=strs['meal_type']
    )


async def cooking_type(update: Update, context: ContextTypes.DEFAULT_TYPE):
    return await command_with_buttons(
        update,
        context,
        FoodOptions.cooking_type,
        strs['cooking_type_prompt'],
        State.cooking_type,
        user_data_key=strs['cooking_type'],
        placeholder=strs['cooking_type']
    )


async def soup_type(update: Update, context: ContextTypes.DEFAULT_TYPE):
    reply_keyboard = buttons(FoodOptions.soup_type)

    await update.message.reply_text(
        strs['soup_texture_prompt'],
        reply_markup=ReplyKeyboardMarkup(
            reply_keyboard,
            one_time_keyboard=True,
            input_field_placeholder=strs['soup_texture']
        )
    )

    return await command_with_buttons(
        update,
        context,
        FoodOptions.soup_type,
        strs['soup_texture_prompt'],
        State.soup_type,
        user_data_key=strs['soup_texture'],
        placeholder=strs['soup_texture']
    )


async def dessert_milk(update: Update, context: ContextTypes.DEFAULT_TYPE):
    return await command_with_buttons(
        update,
        context,
        YES_NO,
        strs['dessert_milk_prompt'],
        State.dessert_milk,
        user_data_key=strs['dessert_milk']
    )


async def dessert_fruit(update: Update, context: ContextTypes.DEFAULT_TYPE):
    return await command_with_buttons(
        update,
        context,
        YES_NO,
        strs['dessert_fruit_prompt'],
        State.dessert_fruit,
        user_data_key=strs['dessert_fruit']
    )


async def dessert_sugar(update: Update, context: ContextTypes.DEFAULT_TYPE):
    return await command_with_buttons(
        update,
        context,
        YES_NO,
        strs['dessert_sugar_prompt'],
        State.dessert_sugar,
        user_data_key=strs['dessert_sugar']
    )


async def dessert_berries(update: Update, context: ContextTypes.DEFAULT_TYPE):
    return await command_with_buttons(
        update,
        context,
        YES_NO,
        strs['dessert_berries_prompt'],
        State.dessert_berries,
        user_data_key=strs['dessert_berries']
    )


async def flavor(update: Update, context: ContextTypes.DEFAULT_TYPE):
    return await command_with_buttons(
        update,
        context,
        FoodOptions.flavor,
        strs['main_flavor_prompt'],
        State.flavor,
        user_data_key=strs['main_flavor'],
        placeholder=strs['main_flavor']
    )


async def spicy_level(update: Update, context: ContextTypes.DEFAULT_TYPE):
    return await command_with_buttons(
        update,
        context,
        FoodOptions.spicy_level,
        strs['spicy_level_prompt'],
        State.spicy_level,
        user_data_key=strs['spicy_level'],
        placeholder=strs['spicy_level']
    )


async def main_ingredient(update: Update, context: ContextTypes.DEFAULT_TYPE):
    return await command_with_buttons(
        update,
        context,
        FoodOptions.main_ingredient,
        strs['main_ingredient_prompt'],
        State.main_ingredient,
        user_data_key=strs['main_ingredient'],
        placeholder=strs['main_ingredient']
    )


async def meat(update: Update, context: ContextTypes.DEFAULT_TYPE):
    return await command_with_buttons(
        update,
        context,
        FoodOptions.meat_type,
        strs['meat_type_prompt'],
        State.meat_type,
        user_data_key=strs['meat_type'],
        placeholder=strs['meat_type']
    )


async def seafood(update: Update, context: ContextTypes.DEFAULT_TYPE):
    return await command_with_buttons(
        update,
        context,
        FoodOptions.seafood_type,
        strs['seafood_type_prompt'],
        State.seafood_type,
        user_data_key=strs['seafood_type'],
        placeholder=strs['seafood_type']
    )
