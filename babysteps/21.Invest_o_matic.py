import boilerplate

def invest(amount, rate, time):
	print('principal amount: {}'.format(amount))
	print('annual rate of return: {}'.format(rate))
	total = amount

	for x in range (1, time + 1):
		total = total + (total * rate)
		print('year {}: {}'.format(x, total))


invest(100, .05, 8)
invest(2000, .025, 5)

'''
The returned investments from my caculations are very close to the book, 
but not exact.  I think my math is right because it's accurate to several
decimal places.
'''
