# graphingCalc
Calculates the distance between coordinate points on a map.

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
