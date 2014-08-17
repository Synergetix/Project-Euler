# Project Euler problem 3
# Finding the largest prime factor of 600851475143
#Answer: 6857 (?)
import math

n = 600851475143

for i in xrange(0, int(math.sqrt(n))+1):  #it is sufficient to look at the range [0, sqrt(n)] because if x, in that range, is factor then its cofactor will be in the range [sqrt(n), n]
	k = int(math.sqrt(n))+1-i  #look at numbers less than n/2 in a decreasing order to catch the largest prime factor earlier
	p = 0   # 'boolean' to indicate if there is "second-level" factor
	if n%k == 0:  #check if number k (other than 1) divides n evenly
		for j in xrange(2, int(math.sqrt(k))+1):
			if k%j==0:  #check if number j (other than 1) divides k evenly
				p = 1	#set to 1 to show that k has a factor other than 1
				break   # break loop because k is not a prime factor of n (k has a factor that is not 1)
		if p == 0: # k does not have factor other than 1
			print k
			break