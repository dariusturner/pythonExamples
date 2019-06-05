# Print Hello World to console
sectionName = "How To Print"
print('{} Section'.format(sectionName))

print('Hello World')

# Math Operators
#########################################################
sectionName = 'Math Operators'
print('{} Section'.format(sectionName))

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

# The Type function is used to see if a value is a int, float, str, Boolean, list, etc...
print(type(myVar))

floatvar = 1.5

print(type(floatvar))

# Strings
###########################################################
sectionName = 'Strings'
print('{} Section'.format(sectionName))

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

# Lists (Arrays)
###################################################################
sectionName = 'Lists'
print('{} Section'.format(sectionName)) 

my_list = ['string', 1,  83.8]

print(len(my_list))
print(my_list[:2])

firstList = ['one', 'two', 'three']
secondList = ['four', 'five', 'six']

firstList = firstList + secondList

print(firstList + secondList)
print(firstList)

# Lists are mutable
firstList[3] = 'How did I get here?'
print(firstList)

firstList.append('seven')
print(firstList)
print(firstList.pop())

# Pop still pops off the last index in the list firstList
print(firstList)

poppedItem = firstList.pop()
print(poppedItem)

# Can add index to pop function to remove a target index from your list
print(firstList.pop(3))

# Sort function
letterList = ['a','d','j','c']
numList = [5,8,6,5]

letterList.sort()
print(letterList)

numList.sort()
sortedList = numList
print(sortedList)

# Reverse function reverses the indexes in a list
sortedList.reverse()
print(sortedList)

# Nested List
sortedList.append([9,95,9])
print(sortedList)
print(sortedList[4][1])

# Dictionaries
############################################################
sectionName = 'Dictionaries'
print('{} Section'.format(sectionName))

my_dict = {'key1':'value1','key2':'value2'}
#Get vaule1
print(my_dict['key1'])
food_list = {'apples':2.99,'fruit package':9.99,'banana':0.60}
print('How much is the fruit package? Price = ${}!'.format(food_list['fruit package']))

# How to get nested values from lists or dictionaries

example_dict = {'k1':[1,2,3],'k2':{'lvl2':"I am a level two's value, I hope you printed me to your console!"}}

#Print 3
print(example_dict['k1'][2])
#print lvl2 value
print(example_dict['k2']['lvl2'])

#### Dictionaries are mutable #####

# Uppercase lvl2 vaulue
print(example_dict['k2']['lvl2'].upper())

# How to add a new key and value to a dictionary
example_dict['k3'] = "I'm your third key's value!"
print(example_dict)

# How to change a key's value
example_dict['k1'] = 3
print(example_dict['k1'])

#Dictionaries are mappings and do not retain order! If you do want the capabilities of a dictionary but you would like ordering as well, check out the ordereddict object!