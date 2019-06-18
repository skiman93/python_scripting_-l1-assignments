def isListOfInts(l):
	# print(type(l))
	if type(l) == tuple:
		return 'ValueError:' , l, 'arg not of <list> type'
		
	elif not any(isinstance(x, (str, float)) for x in l):
		return 'True'
		
	else:
		return 'False'
		
def testList(array):
	return isListOfInts(array)
	
print('[] --> ', end=''), print(testList([]))
print('[1] --> ', end=''), print(testList([1]))
print('[1,2] --> ', end=''), print(testList([1,2]))
print('[0] --> ', end=''), print(testList([0]))
print('[\'1\'] --> ', end=''), print(testList(['1']))
print('1,\'a\'] --> ', end=''), print(testList([1,'a']))
print('[\'a\',1] --> ', end=''), print(testList(['a',1]))
print('[1, 1.] --> ', end=''), print(testList([1, 1.]))
print('[1., 1.] --> ', end=''), print(testList([1., 1.]))
print(testList((1,2)))
