# encoding=utf8
import telepot
import urllib3
import time
import secrets
import psycopg2

import sys
reload(sys)
sys.setdefaultencoding('utf8')

print('\nConnecting to database')
conn = psycopg2.connect(host="localhost",database="yourmamsbot", user="yourmamsbot", password="yourmamsbot")

# Bot initialization
token=secrets.token
bot = telepot.Bot(token)


def handle(msg):
    print(msg)
    cur = conn.cursor()
    content_type, chat_type, chat_id = telepot.glance(msg)
    if "text" in msg:
        text = msg["text"]
        insertStatement = "INSERT INTO messages (msg_id,chat_id, time, text) VALUES ('" + str(msg["message_id"]) + "','"+ str(chat_id) +"',"+ str(msg["date"]) +",'"+ text+ "');"
#        print(insertStatement)
        cur.execute(insertStatement)
        conn.commit()
        cur.close()


bot.message_loop(handle)

print ('Listening ...')

# Keep the program running.
while 1:
    time.sleep(10)
