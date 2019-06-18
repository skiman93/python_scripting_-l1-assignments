import sys

def ruler(num):
	numbers='1234567890'
	digits = [int(x) for x in str(num)]
	
	# Prints the first line up to the first digit. i.e. up to 4 in 45
	firstDig = []
	count = 1
	for x in range(digits[0]):
		firstDig.append("%10s" % count)
		count+=1
		
	for d in range(len(firstDig)):
		print(firstDig[d], end='')
	print()
	
	# Adds the remaining digits to an array to stringify
	stringVal = ""
	if len(digits) == 2:
		for i in range(digits[1]):
			stringVal += (str(i+1))
		
	# Prints the second line and left over up to the last digit. i.e. up to 5 in 45
	myString = (numbers*digits[0])
	print(myString,end=stringVal)
	
try:
	ruler(sys.argv[1])
		
except IndexError as e:
	number = input("Please enter a number: ")
	ruler(number)
	