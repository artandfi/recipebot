import os
import openai
from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import Application, ContextTypes, CommandHandler, Updater, MessageHandler, filters, ConversationHandler
from callbacks.basic import start, help, additional, recipe, cancel, YES_NO
from callbacks.food import (
    FoodOptions,
    food, cooking_type, soup_type, dessert_milk, dessert_fruit, dessert_sugar, dessert_berries, flavor,
    spicy_level, main_ingredient, meat, seafood
)
from callbacks.drink import drink, juice_fruit, juice_veggie, tea_type, coffee_milk, herbal_tea_effect
from states import State


def main() -> None:
    """Start the bot."""
    with open("bot_token.txt") as f:
        bot_token = f.read()
    
    with open("openai_key.txt") as f:
        os.environ['OPENAI_KEY'] = f.read()

    # Create the Application and pass it your bot's token.
    application = Application.builder().token(bot_token).build()

    conv_handler = ConversationHandler(
        entry_points=[CommandHandler('start', start)],
        states={
            State.food_or_drink: [
                MessageHandler(filters.Text(["Food"]), food),
                MessageHandler(filters.Text(["Drink"]), drink)
            ],
            State.meal_type: [
                MessageHandler(filters.Text(["Snack", "Main Course", "Side Dish"]), cooking_type),
                MessageHandler(filters.Text(["Soup"]), soup_type),
                MessageHandler(filters.Text(["Salad"]), flavor),
                MessageHandler(filters.Text(["Dessert"]), dessert_milk)
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
                MessageHandler(filters.Text(["Sweet", "Sour", "Bitter", "Salty"]), main_ingredient),
                MessageHandler(filters.Text(["Spicy"]), spicy_level)
            ],
            State.spicy_level: [
                MessageHandler(filters.Text(FoodOptions.spicy_level.value), main_ingredient)
            ],
            State.main_ingredient: [
                MessageHandler(filters.Text(["Meat"]), meat),
                MessageHandler(filters.Text(["Seafood"]), seafood),
                MessageHandler(filters.Text(["Fruit", "Veggies", "Other"]), additional)
            ],
            State.meat_type: [
                MessageHandler(filters.Text(FoodOptions.meat_type.value), additional)
            ],
            State.seafood_type: [
                MessageHandler(filters.Text(FoodOptions.seafood_type.value), additional)
            ],
            State.drink_type: [
                MessageHandler(filters.Text(["Juice"]), juice_fruit),
                MessageHandler(filters.Text(["Tea"]), tea_type),
                MessageHandler(filters.Text(["Coffee"]), coffee_milk),
                MessageHandler(filters.Text(["Other"]), additional)
            ],
            State.juice_fruit: [
                MessageHandler(filters.Text(YES_NO), juice_veggie)
            ],
            State.juice_veggie: [
                MessageHandler(filters.Text(YES_NO), additional)
            ],
            State.tea_type: [
                MessageHandler(filters.Text(["Green", "Black", "White"]), additional),
                MessageHandler(filters.Text(["Herbal"]), herbal_tea_effect)
            ],
            State.herbal_tea_effect: [
                MessageHandler(filters.Text(["Calm Down", "Energize", "Fall Asleep Faster", "Relive Cough"]), additional)
            ],
            State.coffee_milk: [
                MessageHandler(filters.Text(YES_NO), additional)
            ],
            State.additional: [
                MessageHandler(filters.TEXT, recipe)
            ],
            State.end: [
                MessageHandler(filters.Text(["Start"]), start)
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
