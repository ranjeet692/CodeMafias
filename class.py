#!/usr/bin/python
# -*- coding: utf-8 -*-
print "Content-Type: text/html\n\n"
from jinja2 import Template, Environment, FileSystemLoader
templateLoader = FileSystemLoader( searchpath="/" )
templateEnv = Environment( loader=templateLoader )
TEMPLATE_FILE = "/var/www/html/class.html"
template = templateEnv.get_template( TEMPLATE_FILE )
classid=1
title = "Core Java"
d = " Presenting the TRAILER of Bhushan Kumar's 'Roy', a T-Series Film, Directed by Vikramjit Singh, Produced by Divya Khosla Kumar, Bhushan Kumar and Krishan Kumar Co-Produced by Ajay Kapoor, starring Ranbir Kapoor in a Dynamic Role, Arjun Rampal and Jacqueline Fernandez."
timeline=""
links=""
templateVars = { "title" : title, "description" :  d }
print template.render( templateVars )

