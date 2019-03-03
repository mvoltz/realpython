
import boilerplate

'''
In python information is stored as objects.  Strings are objects.
Objects can hold other objects too, so they can become complex.
Different objects may have different capabilities (methods).

Here are some examples:
'''

lower_str = 'this is my inside voice.'
print(lower_str)

# neat, but we've seen this before

print(lower_str.upper())

# the 'upper' method converts the characters to UPPER CASE

'''
neat.  Methods are just functions that are attached to objects.
Another useful function is getting input from users...
'''

uin = input("Hey, what's up? ")
print('You said: ', uin)

'''
You may have already noticed that you can use single quotes ' or double quotes " for strings.
Just be consistent for each string.
'''

sweet_nothings = input("Let's exercise our reddiquette. Whisper something to me. ")
shout = sweet_nothings.upper()
print('Ok, here goes... ', shout)
