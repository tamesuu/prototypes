#!/usr/bin/python
# coding: utf-8

import sqlite3
from string import Template
from os import path
from httphandler import Request, Response, get_htmltemplate
from simpletemplate import SimpleTemplate

con = sqlite3.connect('./bookmark.dat')
cur = con.cursor()
try:
    cur.execute("""CREATE TABLE IF NOT EXISTS bookmark (
                   title, text, url, text);""")
except:
    pass

req = Request()
f = req.form
value_dic = { 'message': '', 'title': '', 'url': '', 'bookmarks': '' }

if f.has_key('post'):
    pass

cur.execute("SELECT title, url FROM bookmark")
value_dic['bookmarks'] = tuple(cur.fetchall())

res = Response()
p = path.join(path.dirname(__file__), 'stbookmarkform.html')
t = SimpleTemplate(file_path=p)
body = t.render(value_dic)
res.set_body(body)
print res
