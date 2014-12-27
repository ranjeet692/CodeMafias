#!/usr/bin/python
# -*- coding: utf-8 -*-


print "Content-Type: text/html\n\n"


from jinja2 import Template, Environment, FileSystemLoader
from connection import cursor, db

#fetching data from a table class
sql = "SELECT * from class WHERE classid = %d" % (1)
cursor.execute(sql)
data = cursor.fetchall()
for row in data:
	title = row[1]
	description = row[2]

templateLoader = FileSystemLoader( searchpath="/" )
templateEnv = Environment( loader=templateLoader )
TEMPLATE_FILE = "/var/www/html/class.html"
template = templateEnv.get_template( TEMPLATE_FILE )
classid=1
timeline=""
links=""
assignment=""
test=""
remarks=""

templateVars = { "title" : title, "description" :  description }
print template.render( templateVars )

