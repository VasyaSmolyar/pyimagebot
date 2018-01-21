import telebot
from telebot import types
import image
import writer

token = 'TOKEN'

bot = telebot.TeleBot(token)
img = image.Image(token)

markup = types.ReplyKeyboardMarkup()
ia = types.KeyboardButton('/load')
ih = types.KeyboardButton('/help')
ib = types.KeyboardButton('/gray')
ic = types.KeyboardButton('/sepia')
ie = types.KeyboardButton('/negate')
markup.row(ia,ih)
markup.row(ib,ic,ie)


def check_img(func):
    def ret(message):
        chat_id = message.chat.id
        func(chat_id)
        try:
            with open(img.imgpath(str(chat_id) + '_tmp'),'rb') as f:
                bot.send_photo(chat_id,f,reply_markup = markup)
        except FileNotFoundError:
            bot.send_message(chat_id,'Сначала загрузите картинку!')
    return ret


@bot.message_handler(content_types=["photo"])
def save(message):
    ph = message.photo[2]
    file_info = bot.get_file(ph.file_id)
    img.save(message.chat.id,file_info)
    bot.send_message(message.chat.id,'Фото загружено!',reply_markup = markup)

@bot.message_handler(commands=["load"])
def load(message):
    chat_id = message.chat.id
    try:
        with open(img.imgpath(chat_id),'rb') as f:
            bot.send_photo(chat_id,f,reply_markup = markup)
    except FileNotFoundError:
        bot.send_message(chat_id,'Сначала загрузите картинку!')


@bot.message_handler(commands=["gray"])
@check_img
def gray(chat_id):
    wr = writer.Writer(chat_id)
    wr.gray()

@bot.message_handler(commands=["sepia"])
@check_img
def sepia(chat_id):
    wr = writer.Writer(chat_id)
    wr.sepia()

@bot.message_handler(commands=["negate"])
@check_img
def negate(chat_id):
    wr = writer.Writer(chat_id)
    wr.negate()

@bot.message_handler(commands=["start","help"])
def start(message):
    text = '''
    Image Bot v0.1
    Для начала работы отправьте боту картинку.
    Список команд:
    /start , /help - выводит эту надпись
    /load - возвращает исходную картинку
    /gray - чёрно-белый фильтр
    /sepia - сепия
    /negate - негатив
    '''
    bot.send_message(message.chat.id,text)

if __name__ == "__main__":
    bot.polling(none_stop=True)
