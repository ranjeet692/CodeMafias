#!/usr/bin/python
print "Content-Type: text/html\n\n"

from jinja2 import Template, Environment, FileSystemLoader
from connection import cursor, db

import cgi, cgitb
from connection import cursor, db

data= cgi.FieldStorage()

assignmentid = data.getvalue("var")

sql = "SELECT title from assignment WHERE assignmentid = %d" % (int(assignmentid))
cursor.execute(sql)
data = cursor.fetchall()
for row in data:
	title = row[0]
	
	
sql = "SELECT mcq_problemid from assignment_mcq WHERE assignmentid = %d" % (int(assignmentid))
cursor.execute(sql) 
data = cursor.fetchall()
i = 0
questions = ''

for j in range(len(data)):
	sql1 = "SELECT statement, option1, option2, option3, option4 from problem_mcq where problemid = %d" % (int(data[j][0]))
	cursor.execute(sql1)
	data1 = cursor.fetchall()
	for row1 in data1:
		i = i+1
		questions = questions + '<div class="panel panel-default feedback_panel">' \
				'<div class="panel-body">' \
					'<strong>'+ row1[0] +'</strong>' \
				'</div>' \
				'<div class="panel-footer">' \
					'<div class="radio">' \
						'<label><input type="radio" name="'+str(data[j][0])+'" id="'+str(data[j][0])+'Radios1" value="option1" checked>'+ row1[1] +'</label>'\
					'</div>' \
					'<div class="radio">'\
						'<label><input type="radio" name="'+str(data[j][0])+'" id="'+str(data[j][0])+'Radios2" value="option2">'+ row1[2] + '</label>'\
					'</div>'\
					'<div class="radio">'\
						'<label><input type="radio" name="'+str(data[j][0])+'" id="'+str(data[j][0])+'Radios3" value="option3">'+ row1[3] + '</label>'\
					'</div>'\
					'<div class="radio">'\
						'<label><input type="radio" name="'+str(data[j][0])+'" id="'+str(data[j][0])+'Radios4" value="option4">'+ row1[4] +	'</label>'\
					'</div>'\
				'</div>'\
			'</div>'	

templateLoader = FileSystemLoader( searchpath="/" )
templateEnv = Environment( loader=templateLoader )
TEMPLATE_FILE = "/var/www/html/problem_mcq.html"
template = templateEnv.get_template( TEMPLATE_FILE )

templateVars = { "title" : title, "page_header" : title, "questions":questions }
print template.render( templateVars )
