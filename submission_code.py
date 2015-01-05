#!/usr/bin/python
print "Content-Type: text/html\n\n"

import cgi, os
import cgitb; cgitb.enable()
import requests


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
   
print '''<div class="panel-heading">Test Cases</div>
				<div class="panel-body">
				  <!-- Table -->
  					<table class="table">
   					 	<tr>
   					 		<th>#</th><th>Time</th><th>Memory</th><th>Result</th>
   					 	<tr/>
   					 	<tr>
   					 		<td>1</td><td>1.032</td><td>342</td><td>90%</td>
   					 	<tr/>
   					 	<tr>
   					 		<td>2</td><td>1.023</td><td>435</td><td>50%</td>
   					 	<tr/>
 					 </table>
				</div>'''

