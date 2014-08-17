#Project Euler problem 5
#Finding the smallest number that is evenly divisible by numbers from 1 through 20
# Answer: 232,792,560
import random

 
##Monte Carlo version (this does not always give the smallest multiple. ----------------------
#How many trials should be run to find the true minimum on average?)

n2 = 5*7*11*13*17*19
array1 = []

for i in xrange(800):
	n2 *= (2**random.randrange(4,6,1))*(3**random.randrange(2,6,1))
	p = 0 # set value to 0 assuming n is the smallest multiple
	for m in xrange(2, 21):
		if n2 % m != 0:   #if one of [1,..., 20] does not divide n evenly, stop the loop
			p = 1	#set value to 1 if one number does not divide evenly
			break
	if p == 0:
		array1.append(n2)  #collect all the multiples that are found
		
print min(array1) #find the smallest of the multiples obtained during this run


		
		
##Version using for loops  --------------------------------------------------------------------

n = 5*7*11*13*17*19

for i in xrange(4,10):
	p = 0 # set value to 0 assuming n is the smallest multiple
	for j in xrange(2,10):  #this may not be needed? 3 has at most a power of 3?
		n *= (2**i)*(3**j)
		p = 0 # set value to 0 assuming n is the smallest multiple
		#print n
		for m in xrange(2, 21):
			if n%m != 0:   #if one of [1,..., 20] does not divide n evenly, stop the loop
				p = 1	#set value to 1 if one number does not divide evenly
				break
		if p == 0:
			print n #, i, j
			break
	if p == 0:
		break
		
		
# Checking -----------------------------------------------------------
# 2 has a power of 4 because 16 = 2^4 is the largest power of 2 in the range [1, 20]
# 3 has a power of 2 because 9 = 3^2 is the largest power of 3 in the range [1, 20]
# 5, 7,..., 19 (prime numbers) have a power 1 because no number in the range [1, 20] has 
# those factors with a higher power
print (2**4)*(3**2)*5*7*11*13*17*19