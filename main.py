import os
import json
from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import Application, ContextTypes, CommandHandler, Updater, MessageHandler, filters, ConversationHandler
from callbacks.basic import start, help, additional, recipe, cancel, strs, YES_NO
from callbacks.food import (
    FoodOptions,
    food, cooking_type, soup_type, dessert_milk, dessert_fruit, dessert_sugar, dessert_berries, flavor,
    spicy_level, main_ingredient, meat, seafood
)
from callbacks.drink import drink, juice_fruit, juice_veggie, tea_type, coffee_milk, herbal_tea_effect
from states import State
from config import BOT_TOKEN_PATH, OPENAI_KEY_PATH


def main() -> None:
    """Start the bot."""
    with open(BOT_TOKEN_PATH) as f:
        bot_token = f.read()
    
    with open(OPENAI_KEY_PATH) as f:
        os.environ['OPENAI_KEY'] = f.read()

    application = Application.builder().token(bot_token).build()

    conv_handler = ConversationHandler(
        entry_points=[CommandHandler('start', start)],
        states={
            State.food_or_drink: [
                MessageHandler(filters.Text([strs['food']]), food),
                MessageHandler(filters.Text([strs['drink']]), drink)
            ],
            State.meal_type: [
                MessageHandler(filters.Text([strs['snack'], strs['main_course'], strs['side_dish']]), cooking_type),
                MessageHandler(filters.Text([strs['soup']]), soup_type),
                MessageHandler(filters.Text([strs['salad']]), flavor),
                MessageHandler(filters.Text([strs['dessert']]), dessert_milk)
            ],
            State.cooking_type: [
                MessageHandler(filters.Text(FoodOptions.cooking_type.value), flavor)
            ],
            State.soup_type: [
                MessageHandler(filters.Text(FoodOptions.soup_type.value), flavor)
            ],
            State.dessert_milk: [
                MessageHandler(filters.Text(YES_NO), dessert_fruit)
            ],
            State.dessert_fruit: [
                MessageHandler(filters.Text(YES_NO), dessert_sugar)
            ],
            State.dessert_sugar: [
                MessageHandler(filters.Text(YES_NO), dessert_berries)
            ],
            State.dessert_berries: [
                MessageHandler(filters.Text(YES_NO), additional)
            ],
            State.flavor: [
                MessageHandler(filters.Text([strs['sweet'], strs['sour'], strs['bitter'], strs['salty']]), main_ingredient),
                MessageHandler(filters.Text([strs['spicy']]), spicy_level)
            ],
            State.spicy_level: [
                MessageHandler(filters.Text(FoodOptions.spicy_level.value), main_ingredient)
            ],
            State.main_ingredient: [
                MessageHandler(filters.Text([strs['meat']]), meat),
                MessageHandler(filters.Text([strs['seafood']]), seafood),
                MessageHandler(filters.Text([strs['fruit'], strs['veggies'], strs['other']]), additional)
            ],
            State.meat_type: [
                MessageHandler(filters.Text(FoodOptions.meat_type.value), additional)
            ],
            State.seafood_type: [
                MessageHandler(filters.Text(FoodOptions.seafood_type.value), additional)
            ],
            State.drink_type: [
                MessageHandler(filters.Text([strs['juice']]), juice_fruit),
                MessageHandler(filters.Text([strs['tea']]), tea_type),
                MessageHandler(filters.Text([strs['coffee']]), coffee_milk),
                MessageHandler(filters.Text([strs['other']]), additional)
            ],
            State.juice_fruit: [
                MessageHandler(filters.Text(YES_NO), juice_veggie)
            ],
            State.juice_veggie: [
                MessageHandler(filters.Text(YES_NO), additional)
            ],
            State.tea_type: [
                MessageHandler(filters.Text([strs['green'], strs['black'], strs['white']]), additional),
                MessageHandler(filters.Text(["Herbal"]), herbal_tea_effect)
            ],
            State.herbal_tea_effect: [
                MessageHandler(filters.Text([strs['calm_down'], strs['energize'], strs['fall_asleep'], strs['relieve_cough']]), additional)
            ],
            State.coffee_milk: [
                MessageHandler(filters.Text(YES_NO), additional)
            ],
            State.additional: [
                MessageHandler(filters.TEXT, recipe)
            ],
            State.end: [
                MessageHandler(filters.Text([strs['start']]), start)
            ]
        },
        fallbacks=[CommandHandler('cancel', cancel)]
    )

    # on different commands - answer in Telegram
    application.add_handler(conv_handler)
    application.add_handler(CommandHandler("help", help))

    # Run the bot until its owner presses Ctrl-C
    application.run_polling()


if __name__ == "__main__":
    main()
