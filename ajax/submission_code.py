#!/usr/bin/python
print "Content-Type: text/html\n\n"

import cgi, os
import cgitb; cgitb.enable()
import requests
from jinja2 import Template, Environment, FileSystemLoader
from connection import cursor, db

try: # Windows needs stdio set for binary mode.
    import msvcrt
    msvcrt.setmode (0, os.O_BINARY) # stdin  = 0
    msvcrt.setmode (1, os.O_BINARY) # stdout = 1
except ImportError:
    message = 'Error'

form = cgi.FieldStorage()

# A nested FieldStorage instance holds the file
fileitem = form['file']

# Test if the file was uploaded
if fileitem.filename:
   
    #strip leading path from file name to avoid directory traversal attacks
	fn = os.path.basename(fileitem.filename)
  	open('/home/ranjeet/template/'+fn, 'wb').write(fileitem.file.read())
  	message = 'The file "' + fn + '" was uploaded successfully'
   
else:
	message = 'No file was uploaded'
   
#print message +" " + fileitem.filename
#print form
templateLoader = FileSystemLoader( searchpath="/" )
templateEnv = Environment( loader=templateLoader )
TEMPLATE_FILE = "/var/www/html/problem_code.html"
template = templateEnv.get_template( TEMPLATE_FILE )
templateVars = { "title" : data[0][0], "title" : data[0][0], "description": data[0][1] + '<hr>'+data[0][2] + '<hr>' +data[0][3], message: message }
print template.render( templateVars )
