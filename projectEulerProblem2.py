#Project Euler project 2
#Finding the sum of the even Fibonacci numbers that are less than 4,000,000
#Answer: 4,613,732

i=1
j=2

array1 = [2] # array of even Fibonacci numbers
sum = 2 # sum of even Fibonacci numbers
fibmax = 4000000

while i+j < fibmax:
	k = i+j
	if k >= fibmax: break
	i=j
	j=k
	if k%2 == 0:
		array1.append(k)
		sum += k
	
	
#print array1
print sum

