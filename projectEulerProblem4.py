#Project Euler project 4
#Finding the largest palindromic number obtained by multiplying two 3-digit numbers
#Answer: 906609 (the product of 913 and 993)



def isPalindrome(n):
	array1= list(str(n)) #convert the number as a string and break into an array of digits
	len1 = len(array1)
	c = 1  # set c = 1 if we have a palindrome
	for i in range(len1/2):  #comparing opposite ends pairwise to see if they match
		if array1[i] != array1[-i-1]:
			c = 0
			break
	return c
			
array0 = [ ]

for i in range(900, 1000):
	for j in range(i, 1000):
		p = i*j
		if isPalindrome(p) == 1:
			array0.append([i, j, p])
		
print array0


