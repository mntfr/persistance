import itertools

def parkerPersistanceFixed(num, steps=0):
	"""
		Fixed algorithm based on the video (sorry I couldn't help it with the name)
		Parameters:
			num = int, number to analyze
			steps = total steps so far, default = 0
		Returns:
			steps = total steps needed
		Return type:
			int
	"""
	if len(str(num)) == 1:
		return steps
	else:
		steps += 1
		digits = [int(i) for i in str(num)]

		result = 1
		for j in digits:
			result *= j
		return parkerPersistanceFixed(result, steps)

#Al the combinations based on the restrictions of the video
firstDigits = [1, 2, 3, 4]
firstDigits = [x for x in itertools.combinations(firstDigits, 2)]
firstDigits = [''.join(str(y) for y in x) for x in firstDigits]

def generateNumber(firstDigits, numberLenght):
	"""
		Possible number generator based on the limites given in the video:
			-First digits a combination of [1, 2, 3, 4] of 2 digits
			-The rest of the number just 7s, 8s or 9s
		Parameters:
			firstDigits = list, possibilities of first 2 digits
			numberLenght = int, lenght of the number to analyze
		Returns:
			possible number
		Return type:
			int, generator
	"""
	for first in firstDigits:
		restOfNumber = itertools.product([7, 8, 9], repeat=numberLenght - 2)
		for comb in restOfNumber:
			lastDigits = ''.join(str(x) for x in comb)
			yield int(first + lastDigits)

#This loop will try every possible combination and analyze them
#This will run forever
#The starter search space is given in the video			
searchSpace = 230
while True:
	for _ in generateNumber(firstDigits, searchSpace):
		if parkerPersistanceFixed(_) >= 11:
			print('{} takes: {} steps'.format(_, parkerPersistanceFixed(_)))
	searchSpace += 1
