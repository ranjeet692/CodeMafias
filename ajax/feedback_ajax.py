#!/usr/bin/python

print "Content-Type: text/plain\n"

import cgi, cgitb
from connection import cursor, db

data= cgi.FieldStorage()

classid = data.getvalue("classid")
studentid = data.getvalue("studentid")
question1 = data.getvalue("q1Radios")
question2 = data.getvalue("q2Radios")
question3 = data.getvalue("q3Radios")
comment = data.getvalue("commentbox")

sql = "insert into feedback values({0},{1},'{2}','{3}','{4}','{5}')" .format(int(classid), int(studentid), question1, question2, question3, comment)
cursor.execute(sql)
db.commit()

print classid + " " + " " + studentid + " " + " " + question1 + " " + question2 + " " + question3 + " " + comment
