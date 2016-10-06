#writing and reading files

from sys import argv

script, filename = argv

print "we are going to earse %r" % filename
print "if u dont want that hit ctrl + c (^c)"
print "if u want that, press enter"

raw_input("?")

print "opening the file..."
target = open(filename, 'w')

print "truncating the file, goodbye"
target.truncate()

print "now m going to ask u three lines"

line1  = raw_input("line 1")
line2  = raw_input("line 2")
line3 = raw_input("line 3")

print " i am going to write these to the file"

target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

print "and finally, we clsoe it"
target.close()

