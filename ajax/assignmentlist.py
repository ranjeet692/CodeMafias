#!/usr/bin/python

print "Content-Type: text/plain\n"

import cgi, cgitb
from connection import cursor, db
from connection import cursor, db

data= cgi.FieldStorage()

classid = data.getvalue("classid")


sql = "SELECT * from assignment where classid = {0} ORDER BY startdate DESC".format(int(classid))
cursor.execute(sql)
data = cursor.fetchall()
count = len(data)
for i in range(len(data)):
	print '<div class="panel panel-danger">' \
				'<div class="panel-heading">Assignment #'+ str(count) + '</div>' \
				'<div class="panel-body">' \
					'<h4><strong><a href="problem_mcq.py?var='+str(data[i][0])+'">'+ str(data[i][4])+'</a></strong></h4>' \
					'<hr/>' \
					'<h5>Due Date : '+ str(data[i][3]) +' </h5>' \
					'<hr/><h5>Result : </h5><hr/>' \
				'</div>' \
			'</div>'
	count = count - 1
	#print data[i][0]
	

