ALTER DATABASE yourmamsbot RENAME TO yourmamsbottemplate;
CREATE DATABASE yourmamsbot WITH ENCODING = 'UTF8'  TEMPLATE yourmamsbottemplate;