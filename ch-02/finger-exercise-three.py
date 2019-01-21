# Finger exercise: Write a program that asks the user to input 10 integers, and then prints the largest
# odd number that was entered. If no odd number was entered, it should print a message to that effect.

inputValues = []

# loop that iterates 10 times
# ask user to enter integer and append them to a list
for i in range(10):
    inputValues.append(int(input('Enter an integer => ')))

oddValues = []

# loop using range that covers the whole integer list
# check the modulo of the number passed in like value[x]
for i in range(10):
    if inputValues[i] % 2 != 0:
        oddValues.append(inputValues[i])

if len(oddValues):
    print("\nLargest Odd Number => " + str(max(oddValues)))
else:
    print("\nNo odd values were entered")