import os
import sys
import traceback
from telegram.ext import Updater, Filters
from telegram.ext import CommandHandler, ConversationHandler, MessageHandler
import tasks

def start(bot, update):
    chat_id = update.message.chat_id
    text = update.message.text
    bot.send_message(chat_id=chat_id, text="I'm a bot, please talk to me!")

def echo(bot, update):
    chat_id = update.message.chat_id
    text = update.message.text
    
    task_cls_list = [tasks.ToonDown, tasks.GuGu, tasks.EngDict]

    try:
        for task_cls in task_cls_list:
            task = task_cls(text)

            if task.is_valid():
                response = task.proc()
                break
            else:
                response = '네가 무슨 말 하는지 모르겠어. :('
    except Exception as e:
        response = '처리 중에 오류 발생!'
        traceback.print_exc()
    
    bot.send_message(chat_id=chat_id, text=response)

def main(token):
    bot = Updater(token=TOKEN)

    handler = CommandHandler('start', start)
    bot.dispatcher.add_handler(handler)

    handler = MessageHandler(Filters.text, echo)
    bot.dispatcher.add_handler(handler)

    bot.start_polling()

    print('running telegram bot...')
    bot.idle()

if __name__ == '__main__':
    TOKEN = None
    if TOKEN is None:
        print('ERROR! 텔레그램 토큰을 지정해주세요.', file=sys.stderr)
        sys.exit(1)
    main(TOKEN)
