#more vairabes and using formatters
my_name = " Walia, Ankur"
my_age = 24
my_height = 6 #ft
my_weight = 68 #kg
my_eyes = "black"
my_teeth = "White"
my_hair = "brown"


#using those variables

print "Lets talk about %s" % my_name
print " he is %d ft tall" % my_height
print "he is %d kg heavy" %my_weight, " thats a lil less"
print "he is got %s eyes and %s hair" % (my_eyes, my_hair)
#the tricky line
print "if i add %d, %d, and %d i get %r" %(my_age, my_height, my_weight, my_age + my_height + my_weight)