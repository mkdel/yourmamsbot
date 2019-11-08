\c yourmamsbot;
CREATE TABLE words (word varchar(50), counter integer, chat_id integer, starttime date, endtime date);
ALTER TABLE words ADD CONSTRAINT word_unique UNIQUE (word);
