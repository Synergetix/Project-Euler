# Project Euler problem 3
# Finding the largest prime factor of 600851475143
#Answer: 

n = 600851475143
p = 0  #indicates if there is "second-level" factor
#stop = false  #boolean to stop outer loop

for i in xrange(0, n/2-1):  #it is sufficient to look at the range [0, n/2] because if x, in that range, is factor then its cofactor will be in the range [n/2, n]
	k = n/2-i   #look at numbers less than n/2 in a decreasing order to catch the largest prime factor earlier
	p = 0
	#print k
	if n%k == 0:  #check if number k (other than 1) divides n evenly
		for j in xrange(2, k/2+1):  #look for numbers in an increasing order
			#print j
			if k%j==0:  #check if number j (other than 1) divides k evenly
				#p += 1  # add 1 to count the depth of factor
				p = 1	#set to 1 to show that k has a factor other than 1
				break   # break loop because k is not a prime factor of n (k has a factor that is not 1)
		if p == 0: # k does not have factor other than 1
			print k
			break
#print p