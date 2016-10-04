#params, unpacking and vriables

from sys import argv

#using sys modules, argv is the arguments




script , user_name = argv
prompt = '>'

print "Hi %s, i'm the %s script" % (user_name, script)
print "i'd like to ask u some question"
print "do u like me %s?" % user_name
likes = raw_input(prompt)

print "where do u live"
lives = raw_input(prompt)

print "what kind of pc do u have?"
computer = raw_input(prompt)

print"""
alright, %s, u said %s about
liking me and u live in %s,
and u have a %s computer nice!
""" % (user_name, likes, lives, computer)



