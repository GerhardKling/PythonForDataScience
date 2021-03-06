"""
U7 Loops
@author: Gerhard Kling
"""

#=========================================================================================================
#For loops
#=========================================================================================================
#Using range
#Note: 10 is exclusive
for j in range(10):
	print(j)

#Loop over iterable object
foods = ['apples', 'pizza', 'bread']

for food in foods:
	print(f"I like to eat {food}")


#=========================================================================================================
#While loops
#=========================================================================================================
#Fibonacci number
#Two initial values
fib = [0, 1]

while fib[-1] < 10000:
	fib.append(fib[-2] + fib[-1])

print(fib)


