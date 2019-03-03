import boilerplate

'''
There are two kinds of loops in Python: 'for' loops and 'while' loops.
They're used to run repeatedly until a stop condition is met.
'''

n = 1
while (n <= 10): 
	print('n = ', n)
	n = n + 1
print ('While loop finished')

for n in range(1, 10):		# prints 1-9, not 10
	print('n = ', n)
print ('For loop finished')

# Loops inside loops

for n in range(1, 5):
	for o in ['a', 'b', 'c']:
		print('n =', n, 'and o =', o)
print ('Nested loop finished')
