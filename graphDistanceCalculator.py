"""

This script allows a user to enter space separated coordinates
and will return the distance travelled (depending on the unit variable) 
between the points.

Valid input is as follows:
A capital letter followed by a whole number (int)

e.g.
A1 B20 C305 D19203

Invalid input:
Any coordinates that start with lower case letters or contain a float

e.g.
a2 C1.2 a1.2 a0

An invalid input will terminate the script and return the first instance
of invalid input

The 'unit' variable on line 44 can be modified to reflect units travelled.

"""

from math import sqrt

def checkValidInput(coords):
	if coords == []:
		return False, ''
	for i in range(len(coords)):
		if not coords[i][0].isupper() or not coords[i][1:].isdecimal():
			return False, coords[i]
		else:
			pass
	return True, None

validInput = True
while validInput == True:
	try:
		coords = input('Enter trip map references: ').split()
		validInput, badInput = checkValidInput(coords)
		distance = 0
		units = 0.5 							#Each unit travelled is 0.5km

		if validInput == True:
			for i in range(len(coords) - 1):
				width = abs(int(ord(coords[i][0])) - int(ord(coords[i + 1][0])))
				height = abs(int(coords[i][1:]) - int(coords[i + 1][1:]))
				distance += sqrt(width ** 2 + height ** 2)

			distance *= units
			print('Total distance = {:.1f} km'.format(distance))

		else:
			print('Bad reference: ', '\'', badInput, '\'', sep='')
	except TypeError:
		print('\nPlease enter at least one valid coordinate.\n')
		