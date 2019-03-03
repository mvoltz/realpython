import boilerplate

my_num = '2' 		# this is a string with a number in it, not an integer
print(my_num + my_num) 	# should output 22, not 4, because STRING, not INTEGER
print(my_num * 4) 	# should output 2222

print(int(my_num))	# convert to INTEGER
print(float(my_num))	# convert to FLOAT, for big math

new_num = '2.0'		# this is where it can get tricky
# print(int(new_num))	# this will give an error, because converting a string
			# that would be a float (if converted) would mean
			# losing valuable information after the decimal point
			# if it were converted to an integer
			# uncomment the code to see it

'''
An alternate way to comment code is to the right of your code line.
This works well for short comments but can be cumbersome for long ones.
'''

print('9' + str(9))	# numbers can be converted to strings as well
			# this should print "99"
