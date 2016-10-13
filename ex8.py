#more file operations
from sys import argv
from os.path import exists
#imporitng modules

script, from_file, to_file = argv

#unpacking argv into three vars

print "copying from %s to %s" % (from_file, to_file)

#WE COULD DO THESE TWO ON ONE LINE TOO, HOW?

in_file  = open(from_file)
indata = in_file.read()

#INDATA = OPEN(FROM_FILE).READ()

print "THE INPUT FILE IS %d bytes long" % len(indata)

print "does the output file exists? %r" % exists(to_file)
print "ready, hit RETURN to cntinue, ctrl + c to abort."
raw_input()

out_file = open(to_file, 'w')
out_file.write(indata)

print "alright, done"

out_file.close()
in_file.close()
