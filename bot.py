from telegram import Update, ReplyKeyboardMarkup, InlineKeyboardMarkup, InlineKeyboardButton
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

import psycopg2

keyboard = [['Ближайшие события'], ['Сотрудники'], ['Проекты']]


reply_markup = ReplyKeyboardMarkup(keyboard)


conn = psycopg2.connect(
   database="railway", user='postgres', password='ndohA6xh8Gzl4i4GSf2g', host='containers-us-west-179.railway.app', port=7396
)

async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'Hello {update.effective_user.first_name}')
    # await update.message.


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="EJM Бот для Хакатона 2023")
    response = await update.message.reply_text('Выберите функцию', reply_markup=reply_markup)
    print(response)

async def ping(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    conn = psycopg2.connect(
        database="railway", user='postgres', password='ndohA6xh8Gzl4i4GSf2g', host='containers-us-west-179.railway.app', port=7396
    )
    cursor = conn.cursor()
    data = cursor.execute("select version()")
    await context.bot.send_message(chat_id=update.effective_chat.id, text=data)
    # conn.close()

cursor = conn.cursor()

#Executing an MYSQL function using the execute() method
print(cursor.execute("select version()"))

# Fetch a single row using fetchone() method.
data = cursor.fetchone()
print("Connection established to: ",data)

# conn.close()


app = ApplicationBuilder().token(
    "6141821836:AAGJHF9TS2wsPCemhVirF5QqjXs-ezGlKhY").build()

app.add_handler(CommandHandler("hello", hello))
app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("ping", ping))

app.run_polling()
