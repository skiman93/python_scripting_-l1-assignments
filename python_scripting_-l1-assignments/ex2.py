import sys

def isWhiteLine(f):
	file = open(f)
	array = file.readlines()
	
	# Checks to see if the file only contains whitespace
	if all('' == s or s.isspace() for s in array):
		return True

	# If not only white space, non-blank lines are printed to the cmd prompt
	for i in range(len(array)):
		if not all('' == s or s.isspace() for s in array[i]):
			print(array[i].rstrip("\n"))
			
	file.close()
try:
	isWhiteLine(sys.argv[1])
		
except IndexError as e:
	fName = input("Please enter a file name: ")
	isWhiteLine(fName)
	