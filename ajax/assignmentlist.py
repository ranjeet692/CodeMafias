#!/usr/bin/python

print "Content-Type: text/plain\n"

import cgi, cgitb
from connection import cursor, db
from connection import cursor, db

data= cgi.FieldStorage()

classid = data.getvalue("classid")
#classid = 1

sql = "SELECT * from assignment where classid = {0} ORDER BY startdate DESC".format(int(classid))
cursor.execute(sql)
data = cursor.fetchall()
count = len(data)
for i in range(len(data)):
	if data[i][5] == 0:
		refer_page = '<a href="problem_mcq.py?var='+str(data[i][0])+'">'
		coding_problem = ''
	else:
		refer_page = '<a href="#">'
		sql1 = "SELECT code_problemid from assignment_code where assignmentid = {0}".format(int(data[i][0]))
		cursor.execute(sql1)
		data1 = cursor.fetchall()
		for j in range(len(data1)):
			sql2 = "SELECT title from problem_code where problemid = {0}".format(int(data1[j][0]))
			cursor.execute(sql2)
			data2 = cursor.fetchall()	
			for row in data2:
				coding_problem = '<h5><strong><a href="problem_code.py?var='+str(data1[j][0])+'">'+str(row[0])+'</a></strong></h5>' + coding_problem
		coding_problem = coding_problem + '<hr>'		
	print '<div class="panel panel-danger">' \
				'<div class="panel-heading">Assignment #'+ str(count) + '</div>' \
				'<div class="panel-body">' \
					'<h4><strong>'+ refer_page+str(data[i][4])+'</a></strong></h4>' \
					'<hr/>' \
					'<p>'+coding_problem+'</p>'\
					'<h5>Due Date : '+ str(data[i][3]) +' </h5>' \
					'<hr/><h5>Result : </h5>' \
				'</div>' \
			'</div>'
	count = count - 1
	#print data[i][0]
	

