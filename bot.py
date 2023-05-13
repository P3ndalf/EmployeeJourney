from telegram import Update, ReplyKeyboardMarkup, InlineKeyboardMarkup, InlineKeyboardButton
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

import psycopg2

keyboard = [['Ближайшие события'], ['Сотрудники'], ['Проекты']]


reply_markup = ReplyKeyboardMarkup(keyboard)

BOT_TOKEN = "6141821836:AAGJHF9TS2wsPCemhVirF5QqjXs-ezGlKhY"

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
    cursor = conn.cursor()
    cursor.execute("select version()")
    data = cursor.fetchone()
    await context.bot.send_message(chat_id=update.effective_chat.id, text=data)


async def events(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    cursor = conn.cursor()
    cursor.execute(
        '''
            SELECT
                *
            FROM
                event_type
                INNER JOIN event ON event_type.id = event.type_id
                INNER JOIN state ON state.id = event.state_id
            WHERE date > current_date;
        '''
    )
    data = cursor.fetchall()
    await context.bot.send_message(chat_id=update.effective_chat.id, text='Предстоящие события:')
    for event in data:
        (_, event_type, _, _, _, event_desc, event_date,
         is_online, event_title, _, event_state) = event
        print(event)
        await context.bot.send_message(chat_id=update.effective_chat.id, text='''
            Название: {0}
            Статус: {1}
            Описание: {2}
            Дата: {3}
            Вид: {4}
        '''.format(event_title, event_state, event_desc, event_date, event_type))

cursor = conn.cursor()

# Executing an MYSQL function using the execute() method
cursor.execute("select version()")

# Fetch a single row using fetchone() method.
data = cursor.fetchone()
print("Connection established to: ", data)

app = ApplicationBuilder().token(BOT_TOKEN).build()

app.add_handler(CommandHandler("hello", hello))
app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("ping", ping))
app.add_handler(CommandHandler("events", events))

app.run_polling()
