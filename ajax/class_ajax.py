#!/usr/bin/python

print "Content-Type: text/html\n"

import cgi, cgitb
from connection import cursor, db

data= cgi.FieldStorage()

classid = data.getvalue("classid")
field = data.getvalue("field")

#print classid
#print field

sql = "SELECT %s from class WHERE classid = %d" % (field, int(classid))
cursor.execute(sql)
data = cursor.fetchall()
for row in data:
	timeline = row[0] 
	
print timeline
