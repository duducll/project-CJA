# Sum imput values
import sys

sum=0
n=0

for num in sys.stdin:
	sum += float (num)
# Print the mean of the numbers given in a file
	n += 1

print sum/n

