#this file just opens a connection with the database
import MySQLdb
db=MySQLdb.connect("localhost","root","Rnh174","test")
cursor=db.cursor()

