from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes

# Bot token from BotFather
BOT_TOKEN = "YOUR_BOT_TOKEN"

# Menu items
MENU = {
    "Pizza": 10.99,
    "Burger": 7.99,
    "Pasta": 8.99,
    "Salad": 5.99
}

# Start command handler
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    welcome_message = (
        "Welcome to My Restaurant Bot! 🍽️\n"
        "Use /menu to see our menu and place an order."
    )
    await update.message.reply_text(welcome_message)

# Menu command handler
async def show_menu(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton(item, callback_data=item)] for item in MENU.keys()
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text("Here’s our menu. Select an item to order:", reply_markup=reply_markup)

# Callback handler for menu selection
async def handle_order(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    item = query.data
    price = MENU[item]

    # Confirm order
    await query.answer()
    await query.edit_message_text(
        f"You selected *{item}*.\n"
        f"Price: ${price:.2f}\n\n"
        "Thank you for your order! Use /menu to order more items.",
        parse_mode="Markdown"
    )

# Main function
def main():
    # Initialize the bot
    app = Application.builder().token(BOT_TOKEN).build()

    # Add command handlers
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("menu", show_menu))
    app.add_handler(CallbackQueryHandler(handle_order))

    # Start polling
    print("Bot is running...")
    app.run_polling()

if __name__ == "__main__":
    main()
