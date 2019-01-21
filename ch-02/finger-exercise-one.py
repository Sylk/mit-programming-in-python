# Finger exercise: Write a program that examines three variables—x, y, and z—and prints the largest
# odd number among them. If none of them are odd, it should print a message to that effect.
from random import randint

x, y, z = randint(0, 1000), randint(0, 1000), randint(0, 1000)

print("X => " + str(x), "\nY => " + str(y), "\nZ => " + str(z))

# Determine odd values and add them to oddValues
oddValues = []

if x % 2 != 0:
    oddValues.append(x)

if y % 2 != 0:
    oddValues.append(y)

if z % 2 != 0:
    oddValues.append(z)

if len(oddValues):
    print("\nLargest Odd Number => " + str(max(oddValues)))
else:
    print("\nNo odd values")