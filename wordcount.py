# -*- coding: utf-8 -*-
import psycopg2

try:
	conn = psycopg2.connect(host="localhost",database="yourmamsbot", user="yourmamsbot", password="yourmamsbot")
	conn.set_client_encoding('UTF8')
	print conn.encoding
	cur = conn.cursor()
	cur.execute("SELECT msg_id, chat_id,time, convert_to(text, 'utf-8')  from messages -- where text like 'Test'")

	messages = cur.fetchall() 
	conn.commit()   
	print("Print each message and it's columns values")
	for message in messages:
		print("msg_id = ", message[0], )
		print("chat_id = ", message[1])
		print("time  = ", message[2], "\n")
		print("text  = ", message[3], "\n")
		#message[4].split
	print conn.encoding  


#	INSERT INTO books (id, title, author_id, subject_id)
#	VALUES (, 'Practical PostgreSQL', 1212, 4);
		
except (Exception, psycopg2.Error) as error	:
	print ("Error while fetching data from PostgreSQL", error)

finally:
    #closing database connection.
    if(conn):
        cur.close()
        conn.close()
        print("PostgreSQL connection is closed")
