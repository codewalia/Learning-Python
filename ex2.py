#little complex usage of strings

x = "there are %d types of people." % 10
binary = "binary"
do_not = "don't"
y = "those who know %s and those who %s." % (binary, do_not)

print x
print y

print "i said : %r." % x
# r is replaced by 'x' 
print "i also said:: '%s'." %y

hillarious = False
joke_evaluation = "isn't that joke so funny?! %r"

# % r already embedded in the string
print joke_evaluation % hillarious
#since %r was already in the string this no need to use it agian here , so %r is replaced by hillaripous
w = "this is left side of..."
e  = " a string with a right side."

print w + e
