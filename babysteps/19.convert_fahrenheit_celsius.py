import boilerplate

#formulas
# F = C * (9/5) + 32
# C = (F - 32) * (5/9)

def convert(num1):
	print("If your number was Fahrenheit, the equivalent in Celsius is: {}"\
	.format((int(num1) - 32) * (5/9)))
	print("If your number was Celsius, the equivalent in Fahrenheit is:: {}"\
	.format((int(num1) * (9/5) + 32)))

num1 = input("Let's start with a number: ")
convert(num1)

'''
I tried doing fancy 'if' statements and such but i've decided to learn with
the pace of the ebook.  I.e. - my 'if' statements didn't work
'''
