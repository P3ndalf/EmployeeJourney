from telegram import Update, ReplyKeyboardMarkup, InlineKeyboardMarkup, InlineKeyboardButton
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

import psycopg2

keyboard = [['Ближайшие события'], ['Сотрудники'], ['Проекты']]


reply_markup = ReplyKeyboardMarkup(keyboard)

BOT_TOKEN = "6141821836:AAGJHF9TS2wsPCemhVirF5QqjXs-ezGlKhY"

conn = psycopg2.connect(
    database="railway", user='postgres', password='ndohA6xh8Gzl4i4GSf2g', host='containers-us-west-179.railway.app', port=7396
)


style = """
<style>
@import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@400;500;600;700&display=swap');

body {
  font-family: 'Montserrat', sans-serif;
  max-width: 700px;
  margin-left: auto;
  margin-right: auto;
}

.profile {
  display: flex;
  align-items: center;
  width: 280px;
  height: 103px;
  border: 1px solid red;
  border-radius: 24px;
  padding: 20px 30px;
  margin-left: auto;
  margin-right: auto;
  margin-bottom: 40px;
}

.profile svg {
  flex-shrink: 0;
  margin-right: 20px;
}

.leaf-wrapper {
  display: grid;
  grid-template-columns: 1fr 1fr;
  width: 500px;
  margin-left: auto;
  margin-right: auto;
}

.leaf {
  position: relative;
  padding: 20px;
  border: 2px solid #FF2222;
  border-radius: 25px 0px 25px;
  grid-column: 2;
  margin-left: 20px;
}

.leaf::before {
  content: '';
  position: absolute;
  display: block;
  height: 150%;
  width: 7px;
  background-color: red;
  left: -26px;
  border-radius: 100vw;
}

.leaf-title {
  text-align: right;
  display: block;
}

.leaf-status {
  position: absolute;
  top: 18px;
  left: 18px;
  width: 10px;
  height: 10px;
  border-radius: 50%;
  translate: transform(-50%, -50%);
}

.leaf-status.active {
  background: #2DC33C;
}
.leaf-status.deactive {
  background: #D9D9D9;
}

.leaf-date {
  font-size: 12px;
  text-align: right;
  display: block;
  margin-bottom: 5px;
}

.leaf-desc {
  font-size: 12px;
}

.leaf-wrapper:nth-child(2n + 1) .leaf {
  grid-column: 1;
  border-radius: 0px 25px 0px;
  margin-left: 0;
  margin-right: 20px;
}

.leaf-wrapper:nth-child(2n + 1) .leaf::before {
  left: unset;
  right: -25px;
}

.leaf-wrapper:nth-child(2n + 1) .leaf-title {
  text-align: left;
}

.leaf-wrapper:nth-child(2n + 1) .leaf-date {
  text-align: left;
}

.leaf-wrapper:nth-child(2n + 1) .leaf-status {
  left: unset;
  right: 18px;
}

</style>
"""
root = lambda arr: """
<div class="profile">
  <svg width="40" height="30" viewBox="0 0 40 30" fill="none" xmlns="http://www.w3.org/2000/svg">
    <path fill-rule="evenodd" clip-rule="evenodd" d="M10.956 7.88987C11.7631 6.9968 11.7631 5.55015 10.956 4.65708L10.9289 4.62665C10.1217 3.73358 8.8141 3.73358 8.00699 4.62665L0.605335 12.8146C-0.201778 13.7076 -0.201778 15.1571 0.605335 16.0502L8.00699 24.2375C8.8141 25.1306 10.1217 25.1306 10.9289 24.2375L10.956 24.2077C11.7631 23.3146 11.7631 21.8679 10.956 20.9749L6.50538 16.0502C5.69827 15.1571 5.69827 13.7076 6.50538 12.8146L10.956 7.88987ZM39.3947 12.8146L31.993 4.62665C31.188 3.73358 29.8783 3.73358 29.0711 4.62665L29.044 4.65708C28.2369 5.55015 28.2369 6.9968 29.044 7.88987L33.4967 12.8146C34.3038 13.7076 34.3038 15.1571 33.4967 16.0502L29.044 20.9749C28.2369 21.8679 28.2369 23.3146 29.044 24.2077L29.0711 24.2375C29.8783 25.1306 31.188 25.1306 31.993 24.2375L39.3947 16.0502C40.2018 15.1571 40.2018 13.7076 39.3947 12.8146ZM26.9671 3.2497L16.3094 28.2433C15.9642 29.0291 15.3584 30 14.5769 30H14.5356C13.016 30 12.0257 27.738 12.6976 26.2128L23.2932 1.45583C23.6385 0.672391 24.9182 0.0580303 24.9182 0.0580303V0C26.9857 0 27.6369 1.72457 26.9671 3.2497Z" fill="#FF2222"/>
  </svg>
  <div style="white-space: pre;">
    ФИО: {0} {1} {2}
    Дата рождения: {3}
    Должность: {4}
  </div>
</div>
""".format(arr[0], arr[1], arr[2], arr[3], arr[4])
leaf = lambda arr: """
<div class='leaf-wrapper'>
  <div class='leaf'>
    <span class='leaf-title'>
      {0}
    </span>
    <span class='leaf-date'>{1}</span>
    <span class='leaf-desc'>
      {2}
    </span>
    <div class='leaf-status deactive'></div>
  </div>
</div>
""".format(arr[0], arr[1], arr[2])




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


async def employee(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    cursor = conn.cursor()
    if context.args[0].isdigit():    
        cursor.execute("SELECT * FROM employee where id = {}".format(context.args[0]))
    else:
        cursor.execute("SELECT * FROM employee where lastname like '%{}%'".format(context.args[0]))
    data = cursor.fetchall()
    if len(data) == 1:
        emp = data[0]
        await context.bot.send_message(chat_id=update.effective_chat.id, text="{0} {1} {2}, д.р. {3}, местоположение - {4}, {5} {6}".format(
            emp[1], emp[2], emp[3], emp[4], emp[5], "онлайн" if emp[6] == "True" else "оффлайн", emp[7]
        ))
        
        cursor.execute("select * from employee_event inner join event on event.id = employee_event.id where employee_id = '{0}'".format(emp[0]))
        data = cursor.fetchall()
        leaves = []
        for event in data:
            leaves.append(leaf([str(event[8]), str(event[6]), str(event[5])]))
        print(leaves)
        
        with open("map.html", 'w') as f:
            f.write(style)
            f.write(root([emp[1], emp[2], emp[3], emp[4], emp[7]]))
            for l in leaves:
                f.write(l)
        
    else:
        await context.bot.send_message(chat_id=update.effective_chat.id, text='Введите повторно команду с id рабочего для уточнения:')
        for each in data:
            await context.bot.send_message(chat_id=update.effective_chat.id, text="{0} - {1} {2} {3}".format(
                each[0], each[1], each[2], each[3]
            ))
            
    
        

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
app.add_handler(CommandHandler("employee", employee))


app.run_polling()
