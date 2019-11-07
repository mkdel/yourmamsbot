# encoding=utf8
# -*- coding: utf-8 -*-
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
	try:
		cur = conn.cursor()
		content_type, chat_type, chat_id = telepot.glance(msg)
		if "text" in msg:
			text = msg["text"]
			print(text)
			insertStatement = "INSERT INTO messages (msg_id,chat_id, time, text) VALUES ('" + str(msg["message_id"]) + "','"+ str(chat_id) +"',"+ str(msg["date"]) +",'"+ text+ "');"
			print(insertStatement)
			cur.execute(insertStatement)
			conn.commit()
			#cur.close()
	except (Exception, psycopg2.Error) as error	:
		print ("Error while fetching data from PostgreSQL", error)

	finally:
		#closing database connection.
		if(conn):
			cur.close()
			print("PostgreSQL cursore is closed")
			#conn.close()
bot.message_loop(handle)

print ('Listening ...')

# Keep the program running.
while 1:
    time.sleep(10)
