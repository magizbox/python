#!/usr/bin/python
import re

line = "Cats are smarter than dogs"

search_object = re.search(r'dogs', line, re.M | re.I)
if search_object:
    print "search --> search_object.group() : ", search_object.group()
else:
    print "Nothing found!!"
