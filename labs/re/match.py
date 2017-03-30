import re

line = "Cats are smarter than dogs"

matched_object = re.match(r'(.*) are (.*?) .*', line, re.M | re.I)

if matched_object:
    print "matched_object.group()  : ", matched_object.group()
    print "matched_object.group(1) : ", matched_object.group(1)
    print "matched_object.group(2) : ", matched_object.group(2)
else:
    print "No match!!"
