import sys
f=sys.argv[1] #file name
tag=sys.argv[2] # name of the tag. eg: html
file1=open(f,"r")
file2=open("tag.list","a")
for c in file1.readlines():
	temp="<{}>".format(tag)+c+"</{}>".format(tag)
	file2.write(temp+"\n")
print "tag is added successfully"
