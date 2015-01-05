#!/usr/bin/python
print "Content-Type: text/html\n\n"

from jinja2 import Template, Environment, FileSystemLoader
from connection import cursor, db

import cgi, cgitb
from connection import cursor, db

data= cgi.FieldStorage()

problemid = data.getvalue("var")
#problemid = 1

sql = "SELECT title, statement, sample_io, boundary, tag_difficulty, tag_topic from problem_code WHERE problemid = {0}".format(int(problemid))
cursor.execute(sql)
data = cursor.fetchall()
	
templateLoader = FileSystemLoader( searchpath="/" )
templateEnv = Environment( loader=templateLoader )
TEMPLATE_FILE = "/var/www/html/problem_code.html"
template = templateEnv.get_template( TEMPLATE_FILE )

templateVars = { "title" : data[0][0], "title" : data[0][0], "description": data[0][1] + '<hr>'+data[0][2] + '<hr>' +data[0][3] }
print template.render( templateVars )
