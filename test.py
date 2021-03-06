
# -*- coding: utf-8 -*-

import db

db.create_engine(user='root',password='password',database='test',host='127.0.0.1',port=3306)

users = db.select('select * from user')
# user => 
# [
# 	{'id':1, 'name':'Michael'}
# 	{'id':2, 'name':'Bob'}
# 	{'id':3, 'name':'Adam'}
# ]
n = db.update('insert into user(id,name) values (?,?)',4, 'jack')


with db.connection():
	db.select()
	db.update()
	db.update()

with db.transaction():
	db.select()
	db.update()

