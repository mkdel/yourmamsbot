# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import psycopg2
import string

try:
    conn = psycopg2.connect(host="localhost",database="yourmamsbot", user="yourmamsbot", password="yourmamsbot")
    conn.set_client_encoding('UTF8')
    print(conn.encoding)
    cur = conn.cursor()
    cur.execute("SELECT msg_id, chat_id,time, text from messages -- where text like 'Test'")

    messages = cur.fetchall() 
    conn.commit()   
    print("Print each message and it's columns values")
    for message in messages:
        print("-msg_id = " + message[0])
        print(" chat_id = "+ message[1])
        print(" time  = "+ str(message[2]))
        print(" msg " + message[3])
        curins=conn.cursor()
        for word in message[3].translate(str.maketrans('','',string.punctuation)).split(' '): #.decode('utf-8')
            print("  a word: "+ word)
            insert_text="INSERT INTO words (word,counter) Values(lower('"+word+"'),1) ON CONFLICT (word) DO UPDATE SET counter=words.counter+1"# where word like ('"+word+"')"
            curins.execute(insert_text)
            #word varchar(50), counter integer, chat_id integer, starttime date, endtime date
        conn.commit()
    #to show code page
    #print conn.encoding  


#	INSERT INTO words (id, title, author_id, subject_id)
#	VALUES (, 'Practical PostgreSQL', 1212, 4);
		
except (Exception, psycopg2.Error) as error	:
    print ("Error while fetching data from PostgreSQL", error)

finally:
    #closing database connection.
    if(conn):
        cur.close()
        conn.close()
        print("PostgreSQL connection is closed")
