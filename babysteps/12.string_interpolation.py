import boilerplate

name = "foobot"
tentacles = 8
laser_eyes = 2
observed_laws_of_robotics = 0


print(name, 'has', str(tentacles), 'tentacles,', str(laser_eyes), 'laser eyes, and observes', \
	str(observed_laws_of_robotics), 'laws of robotics.')

'''
Isaac Asimov's "Three Laws of Robotics"

- A robot may not injure a human being or, through inaction, allow a human being to come to harm.
- A robot must obey orders given it by human beings except where such orders would conflict with the First Law.
- A robot must protect its own existence as long as such protection does not conflict with the First or Second Law.
'''

print("RUN!!!!")

'''
String interpolation is just inserting stuff into a string. 
In this case we inserted 3 variables by converting them into strings, into a single sentence.
'''

print(name+' has '+str(tentacles)+' tentacles, '+str(laser_eyes)+' laser eyes, and observes '+\
        str(observed_laws_of_robotics)+' laws of robotics.')

# pluses also work to join string elements, but requires more formatting work

print('{} has {} tentacles, {} laser eyes, and observes {} laws of robotics.'\
	.upper().format(name, tentacles, laser_eyes, observed_laws_of_robotics))

'''
I like this last form of substitution, using {}'s as stand-ins for variable values
The string 'foobot' is not upper-cased in this last example.  WHY NOT?
My guess is that method order matters.  Python applies upper() to the string BEFORE it substitutes the variables.
This may be changeable by ordering the methods differently.
'''

print('{} has {} tentacles, {} laser eyes, and observes {} laws of robotics.'\
        .format(name, tentacles, laser_eyes, observed_laws_of_robotics).upper())

# Yep.

