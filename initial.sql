CREATE USER yourmamsbot WITH PASSWORD 'yourmamsbot';
CREATE DATABASE yourmamsbot WITH OWNER yourmamsbot;
\c yourmamsbot;
CREATE TABLE messages (msg_id integer, chat_id integer, time integer, text varchar, PRIMARY KEY (msg_id, chat_id));
ALTER TABLE messages OWNER TO yourmamsbot;

