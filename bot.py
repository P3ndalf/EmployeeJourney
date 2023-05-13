from telegram import Update, ReplyKeyboardMarkup, InlineKeyboardMarkup, InlineKeyboardButton
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

from urllib import request

import psycopg2

import requests

keyboard = [['Ближайшие события'], ['Сотрудники'], ['Проекты']]


reply_markup = ReplyKeyboardMarkup(keyboard)

BOT_TOKEN = "6141821836:AAGJHF9TS2wsPCemhVirF5QqjXs-ezGlKhY"

conn = psycopg2.connect(
    database="railway", user='postgres', password='ndohA6xh8Gzl4i4GSf2g', host='containers-us-west-179.railway.app', port=7396
)

skiped_status_svg = """
<svg width="10" height="10" viewBox="0 0 10 10" fill="none" xmlns="http://www.w3.org/2000/svg">
    <path fill-rule="evenodd" clip-rule="evenodd" d="M5 10C7.7615 10 10 7.7615 10 5C10 2.2385 7.7615 0 5 0C2.2385 0 0 2.2385 0 5C0 7.7615 2.2385 10 5 10ZM4.25 7.4955C4.25 7.062 4.5795 6.75 4.9955 6.75C5.4205 6.75 5.75 7.062 5.75 7.4955C5.75 7.929 5.4205 8.25 4.9955 8.25C4.5795 8.25 4.25 7.929 4.25 7.4955ZM4.586 2C4.55227 2.00003 4.51889 2.0069 4.48787 2.02017C4.45686 2.03345 4.42886 2.05286 4.40554 2.07725C4.38223 2.10163 4.3641 2.13049 4.35223 2.16206C4.34037 2.19364 4.33502 2.2273 4.3365 2.261L4.4895 5.761C4.49234 5.82538 4.51992 5.88618 4.5665 5.93071C4.61308 5.97524 4.67506 6.00006 4.7395 6H5.261C5.32544 6.00006 5.38742 5.97524 5.434 5.93071C5.48058 5.88618 5.50816 5.82538 5.511 5.761L5.6635 2.261C5.66499 2.22726 5.65962 2.19356 5.64772 2.16195C5.63583 2.13034 5.61765 2.10146 5.59428 2.07707C5.57092 2.05268 5.54285 2.03327 5.51178 2.02003C5.48071 2.00678 5.44728 1.99997 5.4135 2H4.586Z" fill="#FF2222"/>
</svg>
"""

planned_status_svg = """
<svg width="10" height="10" viewBox="0 0 10 10" fill="none" xmlns="http://www.w3.org/2000/svg">
    <path d="M5 0C7.7615 0 10 2.239 10 5C10 7.761 7.7615 10 5 10C2.2385 10 0 7.761 0 5C0 2.239 2.2385 0 5 0ZM5 0.8335C2.7025 0.8335 0.8335 2.7025 0.8335 5C0.8335 7.2975 2.7025 9.1665 5 9.1665C7.2975 9.1665 9.1665 7.2975 9.1665 5C9.1665 2.7025 7.2975 0.8335 5 0.8335ZM4.625 2C4.81475 2 4.97173 2.14117 4.99657 2.32414L5 2.375V5H6.625C6.832 5 7 5.168 7 5.375C7 5.56475 6.85883 5.72173 6.67586 5.74657L6.625 5.75H4.625C4.43525 5.75 4.27827 5.60883 4.25343 5.42586L4.25 5.375V2.375C4.25 2.168 4.418 2 4.625 2Z" fill="#F4D845"/>
</svg>
"""

completed_status_svg = """
<svg width="17" height="10" viewBox="0 0 17 10" fill="none" xmlns="http://www.w3.org/2000/svg">
    <path d="M3.81631 8.14291L1.18452 5.2253C0.913544 4.9249 0.474207 4.9249 0.203231 5.2253C-0.0677438 5.52571 -0.0677438 6.01276 0.203231 6.31316L3.32567 9.7747C3.59665 10.0751 4.03598 10.0751 4.30696 9.7747L11.9396 1.31316C12.2106 1.01276 12.2106 0.525706 11.9396 0.225302C11.6686 -0.0751008 11.2293 -0.0751008 10.9583 0.225302L3.81631 8.14291Z" fill="#2DC33C"/>
    <path d="M9.16414 9.7747C8.89316 10.0751 8.45383 10.0751 8.18285 9.7747C7.88699 9.48222 7.88061 8.97159 8.16904 8.67014L8.67349 8.14291L15.8155 0.225302C16.0865 -0.0751008 16.5258 -0.0751008 16.7968 0.225302C17.0677 0.525706 17.0677 1.01276 16.7968 1.31316L9.16414 9.7747Z" fill="#2DC33C"/>
</svg>
"""


style = """
<style>

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
  display: block;
  margin-bottom: 5px;
}

.leaf-desc {
  font-size: 12px;
}

.leaf-info {
    display: grid;
    gap: 8px;
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

.leaf-wrapper:nth-child(2n + 1) .leaf-info {
    margin-left: auto;
}

.leaf-wrapper:nth-child(2n + 1) .leaf-info div {
    order: 1;
}

.leaf-wrapper:nth-child(2n + 1) .leaf-status {
  left: unset;
  right: 18px;
}

</style>
"""


def root(arr): return """
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


def leaf(title, description, start_date, online, state):
    is_online = online if 'active' else 'deactive'
    status_svg = None

    if state == 'Запланиро0ван':
        status_svg = planned_status_svg
    elif state == 'Выполнено':
        status_svg = completed_status_svg
    elif state == 'Пропущено':
        status_svg = skiped_status_svg
    else:
        status_svg = ''

    return """
        <div class='leaf-wrapper'>
            <div class='leaf'>
                <span class='leaf-title'>
                {0}
                </span>
                <div class='leaf-info'>
                    <span class='leaf-date'>{1}</span>
                    {4}
                </div>
                <span class='leaf-desc'>
                    {2}
                </span>
                <div class='leaf-status {3}'></div>
            </div>
        </div>
        """.format(
        title,
        start_date,
        description,
        is_online,
        status_svg
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


async def employee(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    cursor = conn.cursor()
    if context.args[0].isdigit():
        cursor.execute(
            "SELECT * FROM employee where id = {}".format(context.args[0]))
    else:
        cursor.execute(
            "SELECT * FROM employee where lastname like '%{}%'".format(context.args[0]))
    data = cursor.fetchall()
    if len(data) == 1:
        emp = data[0]
        await context.bot.send_message(chat_id=update.effective_chat.id, text="{0} {1} {2}, д.р. {3}, местоположение - {4}, {5} {6}".format(
            emp[1], emp[2], emp[3], emp[4], emp[5], "онлайн" if emp[6] == "True" else "оффлайн", emp[7]
        ))

        cursor.execute(
            """select 
                title,
                description,
                start_date,
                online,
                name as state
            from employee_event 
            inner join event on event.id = employee_event.id 
            inner join state on event.state_id = state.id 
            where employee_id = {}
        """.format(emp[0]))
        data = cursor.fetchall()
        leaves = []
        for event in data:
            leaves.append(leaf([str(event[0]), str(event[2]), str(event[3]), str(event[4]), str(event[5])]))

        html = ''
        html += root([emp[1], emp[2], emp[3], emp[4], emp[7]])
        for l in leaves:
            html += l

        HCTI_API_ENDPOINT = "https://hcti.io/v1/image"
        # Retrieve these from https://htmlcsstoimage.com/dashboard
        HCTI_API_USER_ID = '90cc590a-094b-4153-8b0d-9eda9bec7526'
        HCTI_API_KEY = '5c872b4f-1d53-4fd4-be63-758c846a69f4'

        data = {'html': html,
                'css': style,
                'google_fonts': "Montserrat"}

        image = requests.post(url=HCTI_API_ENDPOINT, data=data, auth=(
            HCTI_API_USER_ID, HCTI_API_KEY))

        await context.bot.send_message(chat_id=update.effective_chat.id, text=image.json()['url'])

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
