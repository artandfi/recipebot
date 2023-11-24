from enum import Enum
from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import ContextTypes
from states import State
from callbacks.basic import buttons, command_with_buttons, YES_NO


class FoodOptions(Enum):
    food = ["Snack", "Main Course", "Side Dish", "Soup", "Salad", "Dessert"]
    cooking_type = ["Boiled", "Fried", "Baked", "Smoked", "Preserved", "Raw"]
    soup_type = ["Clear", "Creamy"]
    flavor = ["Sweet", "Sour", "Bitter", "Salty", "Spicy"]
    spicy_level = ["Low", "Mild", "Hot"]
    main_ingredient = ["Meat", "Seafood", "Fruit", "Veggies", "Other"]
    meat_type = ["Chicken", "Pork", "Beef", "Lamb", "Veal", "Rabbit", "Turkey", "Duck", "Venison", "Other"]
    seafood_type = ["White Fish", "Red Fish", "Molluscs", "Squid", "Crustaceans"]


async def food(update: Update, context: ContextTypes.DEFAULT_TYPE):
    return await command_with_buttons(
        update,
        context,
        FoodOptions.food,
        "Please choose the type of the meal",
        State.meal_type,
        user_data_key="Meal type",
        placeholder="Meal type"
    )


async def cooking_type(update: Update, context: ContextTypes.DEFAULT_TYPE):
    return await command_with_buttons(
        update,
        context,
        FoodOptions.cooking_type,
        "Please choose the way you'd like to cook your meal",
        State.cooking_type,
        user_data_key="Way of cooking",
        placeholder="Way of cooking"
    )


async def soup_type(update: Update, context: ContextTypes.DEFAULT_TYPE):
    reply_keyboard = buttons(FoodOptions.soup_type)

    await update.message.reply_text(
        "Please choose the soup texture",
        reply_markup=ReplyKeyboardMarkup(
            reply_keyboard,
            one_time_keyboard=True,
            input_field_placeholder="Soup texture"
        )
    )

    return await command_with_buttons(
        update,
        context,
        FoodOptions.soup_type,
        "Please choose the soup texture",
        State.soup_type,
        user_data_key="Soup texture",
        placeholder="Soup texture"
    )


async def dessert_milk(update: Update, context: ContextTypes.DEFAULT_TYPE):
    return await command_with_buttons(
        update,
        context,
        YES_NO,
        "Would you like milk in your dessert?",
        State.dessert_milk,
        user_data_key="Dessert with milk"
    )


async def dessert_fruit(update: Update, context: ContextTypes.DEFAULT_TYPE):
    return await command_with_buttons(
        update,
        context,
        YES_NO,
        "Would you like fruit in your dessert?",
        State.dessert_fruit,
        user_data_key="Dessert with fruit"
    )


async def dessert_sugar(update: Update, context: ContextTypes.DEFAULT_TYPE):
    return await command_with_buttons(
        update,
        context,
        YES_NO,
        "Would you like sugar in your dessert?",
        State.dessert_sugar,
        user_data_key="Dessert with sugar"
    )


async def dessert_berries(update: Update, context: ContextTypes.DEFAULT_TYPE):
    return await command_with_buttons(
        update,
        context,
        YES_NO,
        "Would you like berries in your dessert?",
        State.dessert_berries,
        user_data_key="Dessert with berries"
    )


async def flavor(update: Update, context: ContextTypes.DEFAULT_TYPE):
    return await command_with_buttons(
        update,
        context,
        FoodOptions.flavor,
        "What flavor would you like to be predominant in your dish?",
        State.flavor,
        user_data_key="Predominant flavor",
        placeholder="Predominant flavor"
    )


async def spicy_level(update: Update, context: ContextTypes.DEFAULT_TYPE):
    return await command_with_buttons(
        update,
        context,
        FoodOptions.spicy_level,
        "How spicy would you like your dish?",
        State.spicy_level,
        user_data_key="Spiciness level",
        placeholder="Spiciness level"
    )


async def main_ingredient(update: Update, context: ContextTypes.DEFAULT_TYPE):
    return await command_with_buttons(
        update,
        context,
        FoodOptions.main_ingredient,
        "What main ingredient would you like your dish to have?",
        State.main_ingredient,
        user_data_key="Main ingredient",
        placeholder="Main ingredient"
    )


async def meat(update: Update, context: ContextTypes.DEFAULT_TYPE):
    return await command_with_buttons(
        update,
        context,
        FoodOptions.meat_type,
        "What kind of meat would you like?",
        State.meat_type,
        user_data_key="Meat kind",
        placeholder="Meat kind"
    )


async def seafood(update: Update, context: ContextTypes.DEFAULT_TYPE):
    return await command_with_buttons(
        update,
        context,
        FoodOptions.seafood_type,
        "What kind of seafood would you like?",
        State.seafood_type,
        user_data_key="Seafood kind",
        placeholder="Seafood kind"
    )
