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
