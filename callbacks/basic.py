import json
from typing import Iterable
from enum import Enum
from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import ContextTypes
from states import State
from chatgpt import chatgpt_response
from config import STRINGS_PATH


with open(STRINGS_PATH) as f:
    strs = json.load(f)


YES_NO = [strs['yes'], strs['no']]


class BasicOptions(Enum):
    food_or_drink = [strs['food'], strs['drink']]


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
        f"{strs['hi']} {user.full_name}! {strs['initial_prompt']}",
        reply_markup=ReplyKeyboardMarkup(
            reply_keyboard,
            one_time_keyboard=True,
            input_field_placeholder=strs['what_to_cook']
        )
    )

    context.user_data['latest_key'] = strs['what_to_cook']
    return State.food_or_drink


async def additional(update: Update, context: ContextTypes.DEFAULT_TYPE):
    return await command_with_buttons(
        update,
        context,
        [strs['skip']],
        strs['details_prompt'],
        State.additional,
        user_data_key=strs['details'],
        placeholder=strs['details']
    )


async def recipe(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.message.text != strs['skip']:
        context.user_data[strs['details']] = update.message.text
    
    del context.user_data['latest_key']

    preferences = '\n'.join([f"{key}: {value}" for key, value in context.user_data.items()])

    await update.message.reply_text(
        f"{strs['summary']}\n-----\n{preferences}\n-----\n{strs['wait']}"
    )

    await update.message.reply_text(
        chatgpt_response(
            f"{strs['chatgpt_prompt']}\n{preferences}"
        )
    )

    return State.end


async def help(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a message when the command /help is issued."""
    await update.message.reply_text(strs['help'])


async def cancel(update: Update, context: ContextTypes.DEFAULT_TYPE):
    reply_keyboard = buttons([strs['start']])

    await update.message.reply_text(
        strs['ask_another'],
        reply_markup=ReplyKeyboardMarkup(
            reply_keyboard,
            one_time_keyboard=True
        )
    )

    context.user_data.clear()
    return State.end
