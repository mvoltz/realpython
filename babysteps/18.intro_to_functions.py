import boilerplate

'''
Reusable code below. Yay!
'''

def square(number):
	''' Return the square of a number.'''
	sqr_num = number ** 2
	return sqr_num

input_num = 5
output_num = square(input_num)

print(output_num)

# Be sure to define your functions BEFORE you try to call them

'''
The thing that looks like a multi-line comment right after the function, is called a docstring.
Besides being helpful when reading code directly, docstrings populate the 'help()' function
to get information about the function.
'''

def subtract_two_nums(n1, n2):
	''' Returns the difference between two numbers.
	    Subtracts n2 from n1.'''
	return n1 - n2

n1 = input ('Enter a number: ')
n2 = input ('Lets subtract a number from the first one: ')

print('The magic result is: {}'.format(subtract_two_nums(int(n1),int(n2))))

'''
Functions can take multiple arguments
For the above subtraction function we needed to convert string input results
to integers.
'''

'''
Functions are built using the 'def' keyword.  Multiple arguments are defined 
inside parenthesis, then a colon.
Best practice is to name a function using a verb and make the arguments nouns.
Within a function, indented statements define the actions to take, optionally
returning a value to the caller.
'''
