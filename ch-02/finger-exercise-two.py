# Finger exercise: Replace the comment in the following code with a while loop.
numXs = int(input('How many times should I print the letter X? '))

toPrint = ''

# for  in range(1, numXs):
while numXs > 0:
    toPrint += 'x'
    numXs -= 1

print(toPrint)
