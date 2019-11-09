print("input a number")
number = int(raw_input("number: "))

for x in xrange(1,13):
	result = number * x
	print(str(number) + " x " +  str(x) + " = " + str(result))
