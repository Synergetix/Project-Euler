# Project Euler Problem 1
# Find the sum of the multiples of 3 and the multiples of 5 that are less than 1000
# Answer: 233,168

sum = 0

for i in range(1,1000):
	if i%3==0 or i%5==0: # checks to see if is a multiple of 3 or 5 or both (this way the numbers are not counted twice)
		sum+= i

print sum




