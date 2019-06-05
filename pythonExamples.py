# Print Hello World to console
print('How to print section')

print('Hello World')

# Math Operators
#########################################################
print('Math Operators Section')

print(22 - 5)

print(22 - 5)

print(22 * 5)

print(22 / 5)

print(22 % 5)

print(22 ** 5)

print(22 + 5 * 2)

print((22 - 5) + 5)

print(1 / 2)

# Variables

myVar = 10

print(myVar + myVar)

myVar = myVar * 3

print(myVar)

print(type(myVar))

floatvar = 1.5

print(type(floatvar))

# Strings
###########################################################

print('Strings Section')

print("This is a string that's using two types of quotes!")

# New Line
print('First line \nSecond line')

# Tab (Add 4 spaces)
print('Add \ttab')

# Get length of strings
print("Then length of the string 'My name is Darius is...")
print(len('My name is Darius'))

# Indexing Strings
myString = 'Hello there!'

# Prints Hello!
print(myString[0])
print(myString[1])
print(myString[-9])
print(myString[2])
print(myString[4])
print(myString[-1])

# Index slicing formuala [Start:Stop:Step]

# Prints indexes 0 thru 5 and from 6 to the end... respectively
print(myString[:5])
print(myString[6:])

# Get indexes from certain start and stop points in a string
print(myString[1:5])

# Print the whole string
print(myString[::])
print('Hello World'[::])

# Print start index and every 2nd index after
print(myString[::2])

# Print string in reverse
print(myString[::-1])


# Sting Properties & Methods

# Strings are immutable - you can't use indexing to change individual elements of a string
name = 'Sam'
last_letters = name[1:]

newName = 'P' + last_letters
print(newName)

helloThere = "Hello my name is " + newName + " it's very nice to meet you!"
print(helloThere)

# Multiplcation with Letters
letter = 'Nice to meet you! '
print(letter * 5)

# Functions for strings
hello = 'Hello World!'

print(hello.capitalize())
print(hello.lower())
print(hello.split())

# Can split Strings using letters, numbers or words
hello = 'Hello this is a string'
print (hello.split('i'))

# String Interpolation
name = 'Darius'
print("Hello {} it's nice to meet you!".format(name))

print("Hey {} can {} pass the {} please?".format(name, 'you', 'salt'))

# How to use format if the list is not in the correct order
print("Hey {1} can {2} pass the {0} please?".format('salt', name, 'you'))

##### Debugger shows "Too many arguments for format string" because I have other options in the format list I am not using /// Does not crash the code though
print("Hey {2} can {2} pass the {0} please?".format('salt', name, 'you'))

# Can create variable to use from the format function to use reference to easier in the string
print("Hey {n} can {y} pass the {s} please?".format(n='James', y='you', s='salt' ))

result = 183/999
print(result)

# Float formatting formula "{value:width.precision f}" value is the result/ width adds whitespace from the other text/ precision f defines how many decimal points the value should be rounded to
print('The result of 183/999 is equalt to {r:1.4f}'.format(r=result))


# F-Strings
p = 'Python'
i = 'interesting'

print(f'Hello my name is {name}!')
print(f'Hello my name is {name} and I am learning {p}! I find it very {i}!')

# Lists
###################################################################