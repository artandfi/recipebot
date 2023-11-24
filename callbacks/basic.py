from typing import Iterable
from enum import Enum
from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import ContextTypes
from states import State
from chatgpt import chatgpt_response


YES_NO = ["Yes", "No"]


class BasicOptions(Enum):
    food_or_drink = ["Food", "Drink"]


def buttons(options: Enum | Iterable):
    return [[o] for o in (options.value if isinstance(options, Enum) else options)]


def update_user_choices(update: Update, context: ContextTypes.DEFAULT_TYPE, new_latest_key: str):
    latest_key = context.user_data['latest_key']
    context.user_data[latest_key] = update.message.text
    context.user_data['latest_key'] = new_latest_key


async def command_with_buttons(
        update: Update, context: ContextTypes.DEFAULT_TYPE,
        options: Iterable[str] | Enum, prompt: str, state: State, user_data_key: str, placeholder=''
):
    reply_keyboard = buttons(options)

    await update.message.reply_text(
        prompt,
        reply_markup=ReplyKeyboardMarkup(
            reply_keyboard,
            one_time_keyboard=True,
            input_field_placeholder=placeholder
        )
    )

    update_user_choices(update, context, user_data_key)
    return state


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a message when the command /start is issued."""
    reply_keyboard = buttons(BasicOptions.food_or_drink)
    user = update.effective_user

    await update.message.reply_text(
        f"Hi {user.full_name}! I am here to help you choose what to cook. Do you want to cook food or a drink?",
        reply_markup=ReplyKeyboardMarkup(
            reply_keyboard,
            one_time_keyboard=True,
            input_field_placeholder="What to cook"
        )
    )

    context.user_data['latest_key'] = "What to cook"
    return State.food_or_drink


async def additional(update: Update, context: ContextTypes.DEFAULT_TYPE):
    return await command_with_buttons(
        update,
        context,
        ["Skip"],
        "You may also list any additional details about your meal, or press 'Skip' if you don't want to",
        State.additional,
        user_data_key='Additional details',
        placeholder='Additional details'
    )


async def recipe(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.message.text != 'Skip':
        context.user_data['Additional details'] = update.message.text
    
    del context.user_data['latest_key']

    preferences = '\n'.join([f"{key}: {value}" for key, value in context.user_data.items()])

    await update.message.reply_text(
        f"Summary\n-----\n{preferences}\n-----\nPlease wait while a recipe is being retrieved..."
    )

    await update.message.reply_text(
        chatgpt_response(
            f"Hi! Please give me a recipe of your choice with the following requirements:\n{preferences}"
        )
    )

    return State.end


async def help(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a message when the command /help is issued."""
    await update.message.reply_text("Help text")


async def cancel(update: Update, context: ContextTypes.DEFAULT_TYPE):
    reply_keyboard = buttons(['Start'])

    await update.message.reply_text(
        "Feel free to ask me for another recipe!",
        reply_markup=ReplyKeyboardMarkup(
            reply_keyboard,
            one_time_keyboard=True
        )
    )

    context.user_data.clear()
    return State.end
