#using functions iwth variables
def cheese_and_crackers(cheese_count, boxes_of_crackers):
	print "You have %d cheese" % cheese_count
	print "you have %d boxes of crackers" % boxes_of_crackers
	print "man thats enough for a party"
	print "get a blanket\n"
	
print "we can jsut give the fucntion numbers directly:"
cheese_and_crackers(20,30)

print "or we can use variables from our script"
amount_of_cheese = 10
amount_of_crackers = 20

cheese_and_crackers(amount_of_cheese, amount_of_crackers)

print "we can even do math inside too:"
cheese_and_crackers(10 + 20, 20 + 100)

print "or we can combine variables and numbers:"
cheese_and_crackers(amount_of_cheese + 55, amount_of_crackers + 3)
