# Print Hello World to console
sectionName = "How To Print"
print('{} Section'.format(sectionName))

print('Hello World')

# Math Operators Section
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

# Strings Section
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

# Lists (Arrays) Section
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

# Dictionaries Section
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

# Tuples Section
###########################################################
sectionName = 'Tuples'
print('{} Section'.format(sectionName))

# Tuples are like lists but are immutable and use parethesis!
t = (1,2,3)
l = [1,2,3]
print(type(t))
print(type(l))

# Count function counts how many times a value is in your str, variable, list, etc...
l = [1,1,1]
print(l.count(1))
print(t.count(3))

# Index function show what the first index of the value give is found at
print(t.index(2))
print(l.index(1))

# Tuples are used when you have a list but you don't want to accidently change a value in the list

# Sets Section
###############################################################
sectionName = 'Sets'
print('{} Section'.format(sectionName))

# Sets are unordered collections of unique elements.
mySet = set()

# Add function lets you add an element to a set
mySet.add(1)
print(mySet)

# Sets won't add the same value so all values in a set are unique
mySet.add(1)
print(mySet)

# Make a List into a Set
myList = [1,1,4,5,5,5,5,7,6,6]
print(set(myList))

# Boolean Section
##################################################################
sectionName = "Boolean"
print('{} Section'.format(sectionName))

# Booleans convey True or False Statments

True
False
print(1 < 2)
print(1 == 2)

print(type(1 < 2))

# None can be a place holder for a variable if you do not want to give it a value initially
empty = None
print(empty)
print(type(empty))

# Comparison Operators Section
##################################################################
sectionName = 'Comparison Operators'
print('{} Section'.format(sectionName))

# The AND comparision operator has to have both statements to be True in order to be True
1 > 0.5 and 0.5 <= 1/2
True

1 > 0.5 and 0.5 >= 1/2
False

# The OR comparison operator needs just one statement to be True in order to be True

(100 == 20) or (100 != "100")
True

(100 == 20) or (100 == "100")
False

# The NOT comparison operator just gives you the oposite Boolean that the statement is

not 1 == 1
False

not 1 != 1
True


# Python Statements Section
#############################################################################
sectionName = 'Python Statements'
print('{} Section'.format(sectionName))

# IF/ELSE Statments

if sectionName == 'Python Statements':
    print('You are in the Python Statements Section!')
else:
    print('Please check the code for your variable sectionName, because you are in the Python Statements Section...')

# elif Statements are other conditions that can do something different

fruit = 'Grapes'

if fruit == 'Bananas':
    print("I'm having some Bananas for luch!")
elif fruit == 'Grapes':
    print("I feel like I'm in Greece eating these grapes!")
else:
    print("I'm not even sure I'm eating a fruit...")


# FOR LOOPS
#############################################################################
sectionName = 'For Loops'
print('{} Section'.format)

fruitList = ['apples', 'peaches', 'avacados', 'pineapples', 'lemons', 'bananas']

for eachFruit in fruitList:
    print('Did you know {} were fruits?'.format(eachFruit))

for eachFruit in fruitList:
    if eachFruit == 'peaches':
        print("I only like {}".format(eachFruit))
    elif eachFruit == 'avacados':
        print("I nevermind I also love {}".format(eachFruit))
    else:
        print ("I don't really like that fruit...")

byThree = [1,3,7,9,11,27,99,5]

for index in byThree:
    if index % 3 == 0:
        print('{} is divisible by 3!'.format(index))
    else:
        print('{} is not divisible by 3...'.format(index))

sum = 0

for index in byThree:
    if index % 3 == 0:
        sum += index
    else:
        print(f'{index} was not divisible by 3')

print(f'Adding the indexes divisible by 3 in the variable byThree gave us the sum of {sum}!')

# Show each sum
sum = 0
for index in byThree:
    if index % 3 == 0:
        sum += index
        print(sum)

myName = 'Darius Turner'

for letter in myName:
    print(letter)

# Print string for each character in Name
for _ in 'Name':
    print('Copy this string!')

# TUPLE UNPACKING - Tuples in list are common in Python code

t = [(56,2),(3,472),(59,61.6)]

for coordinate in t:
    print(coordinate)

# Can get each element in a Tuple using this method
for (x,y) in t:
    print(f'{x} is the x coordinate for the point!')
    print(f'{y} is the y coordinate for the point!')

for (x,y) in t:
    print(f'{x} is the X coordinate and {y} is the Y coordinate for the point!')


# Dictionaries Example with for loops
d = {'k1':1,'k2':2,'k3':3}

# Shows Keys
for item in d:
    print(item)

# Shows Keys and Values
for item in d.items():
    print(item)

# Shows Values
for key,value in d.items():
    print(value) 

# Another method to show Values

for value in d.values():
    print(value)

# WHILE LOOPS Section
##################################################################################
sectionName = "While Loops"
print(f'{sectionName} Section')

num = 0
while num <= 5:
    print(f'The current value of num is {num}')
    num+=1
else:
    print(f'Num is not less that or equal to {num}')

# BREAK, CONTINUE & PASS Statements

# break: Breaks out of the current closest enclosing loop.
# continue: Goes to the top of the closest enclosing loop.
# pass: Does nothing at all.

# PASS is used as a place holder for condition statments
x = [1,2,3]
for index in x:
    pass

# CONTINUE skips a certain value if used with an if statement and continues the loop going to the next index
myName = 'Darius'

# Prints Darus
for letter in myName:
    if letter == 'i':
        continue
    print(letter)

# BREAK stops the loop at a certain point
myName = 'Darius'

# Prints Dar
for letter in myName:
    if letter == 'i':
        break
    print(letter)

# Print odd numbers
numList = [1,2,3,4,5,6]

while num < len(numList):
    if num % 2 == 0:
        break
    print(num)

# RANGE is an easy way to define a range for a FOR LOOP

# Prints 0 - 9 and does not include 10
for num in range(10):
    print(num)

# Prints 5 - 10 and does not include 11
for num in range(5,11):
    print(num)

# Can have a step size also - Prints odd numbers
for num in range(5,11,2):
    print(num)

# ENUMERATE FUNCTION prints out indexes faster and easier with less code
word = 'Cool'
# Prints the index and letter - (index, letter)
for item in enumerate(word):
    print(item)

# How to print either the index or letter specifically
for index,letter in enumerate(word):
    print(index)
    print(letter)
    print('\n')

# ZIP function creates a Tuple of the values in different lists
numList = [1,2,3]
letterList = ['z','b','t']
numList2 = [100,200,500]

# If the number of indexes are uneven the zip will end after the last index on the shortest list
for item in zip(numList,letterList,numList2):
    print(item)

# How to create a list using zip
print(list(zip(numList,letterList,numList2)))

# Returns True or False if the value is in the item
'x' in 'Alex'
#True

numList = [1,2,3]
4 in numList
#False

d = {'k1':789,'k2':0,'k3':{'k4':9}}
print(9 in d['k3'].values())
#True

print(9 in d.values())
#False

9 in d['k3'].keys()
#False

'k4' in d['k3'].keys()
#True

# MIN & MAX function gets the smallest value
numList = [9,12,5]
print(min(numList))
# Prints 5

print(max(numList))
# Prints 12

# Import Libraries Section
#################################################################################################
sectionName = 'Import Libraries'
print(f'{sectionName} Section')

# From Random library import Shuffle function that changes the order of things
from random import shuffle

numList = [1,2,3,4,5]
shuffle(numList)
print(numList)

############ CANNOT USE SHUFFLE FUNCTION ON STRINGS

# Random Interger function - grabs a random number in a defined range
from random import randint

print(randint(0,10000))

# Input function takes in user input

# INT changes the input to an integer to use in the if statement
'''usersAge = int(input('Please enter your age...'))

if usersAge >= 21 and  usersAge <= 55:
    print("Want to go to the bar?")
elif usersAge > 55:
    print("You're getting pretty up there!")
else:
    print("You can't even drink yet!")'''


# List Comprehension Section
##############################################################################################
sectionName = 'List Comprehension'
print(f'{sectionName} Section')
# Break down the string and add the indexes of the string to your list
myList = []

myString = 'Hello'

for letter in myString:
    myList.append(letter)
print (myList)

# Less code and still breaks down the string and adds the index of the string to your list
myString = "Hello"
myList = [letter for letter in myString]

# Can add all the indexs to myList and the multiply the indexes by 3 each
myList  = [letter * 3 for letter in myString]
print(myList)

# Can use ranges and if statements
numList = [1,2,3,4,4,5]
myList = [num for num in numList if num % 2 == 0]
print(myList)

# Celcius to Fahrenheit Example
celcius = [0,10,20,30]
fahrenheit = [((9/5)*temp +32) for temp in celcius]
print(fahrenheit)

################ This way can get confusing when you look back at your code at a later time so it's good to use the basic way for the most part

# Multiple 2 lists and append them to a new one
myList = []
for index1 in [2,4,6]:
    for index2 in [1,10,1000]:
        myList.append(index1*index2)
print(myList)

# OR
myList = [index1 * index2 for index1 in [2,4,6] for index2 in [1,10,1000]]
print(myList)





























''' #######################################################################################################################
# Test # 1
#######################################################################################################################
print('STARTING FIRST TEST! ' * 3)
# Write an equation that uses multiplication, division, an exponent, addition, and subtraction that is equal to 100.25.

answer = ((100.25/ 2 * 2 - 2)**0 + 99.25)

print(answer)

# NUMBERS Test
############################################
# Answer these 3 questions without typing code. Then type code to check your answer.

# What is the value of the expression 4 * (6 + 5)
answer = 44
# What is the value of the expression 4 * 6 + 5 
answer = 29
# What is the value of the expression 4 + 6 * 5 
answer = 34

# What is the type of the result of the expression 3 + 1.5 + 4?

########## The results type is a float

# What would you use to find a number’s square root, as well as its square?

squared = 4**4
squaredRoot = 16 ** (0.5)

# STRINGS Test
##############################################
# Given the string 'hello' give an index command that returns 'e'. Enter your code in the cell below:

s = 'hello'
# Print out 'e' using indexing

print(s[1])

# Reverse the string 'hello' using slicing:

s ='hello'
# Reverse the string using slicing

print(s[::-1])

# Given the string hello, give two methods of producing the letter 'o' using indexing.

s ='hello'
# Print out the 'o'

# Method 1:
print(s[-1])
# Method 2:
print(s[-1:])


# LISTS Test
######################################################

# Build this list [0,0,0] two separate ways.

# Method 1:
testList1 = [0,0,0]
# Method 2:
testList2 = [0] * 3

print('This is the result from testList1 {} and this is the result from testList2 {}.'.format(testList1, testList2))

# Reassign 'hello' in this nested list to say 'goodbye' instead:
list3 = [1,2,[3,4,'hello']]

list3[2][2] = 'goodbye'
print(list3)

# Sort the list below:
list4 = [5,3,4,6,1]

list4.sort()
print(list4)

# DICTIONARIES Test
#########################################################

# Using keys and indexing, grab the 'hello' from the following dictionaries:

d = {'simple_key':'hello'}
# Grab 'hello'
print(d['simple_key'])

d = {'k1':{'k2':'hello'}}
# Grab 'hello'
print(d['k1']['k2'])

# Getting a little tricker
d = {'k1':[{'nest_key':['this is deep',['hello']]}]}

#Grab hello
print(d['k1'][0]['nest_key'][1][0])

# This will be hard and annoying!
d = {'k1':[1,2,{'k2':['this is tricky',{'tough':[1,2,['hello']]}]}]}
print(d['k1'][2]['k2'][1]['tough'][2][0])

# TUPLES Test
#########################################################

# What is the major difference between tuples and lists?
####### Tuples are immutable while lists are mutable. Meaning that tuple's values can't be changed through assigning

# How do you create a tuple?
tup = (1,2,3)

# SETS Test
#########################################################

# What is unique about a set?

####### Sets can only have unique values in it, so if you have duplicate values in a list or tuple and turn it into a set... Any duplicate values will no longer be in the list and will show only unique values in the list.

# Use a set to find the unique values of the list below:
list5 = [1,2,2,33,4,4,11,22,3,3,2]

print(set(list5))

# BOOLEANS Test
#########################################################

# What will be the resulting Boolean of the following pieces of code (answer fist then check by typing it in!)

# Answer before running cell
2 > 3
False
# Answer before running cell
3 <= 2
False
# Answer before running cell
3 == 2.0
False
# Answer before running cell
3.0 == 3
True
# Answer before running cell
4**0.5 != 2
False

# Final Question: What is the boolean output of the cell block below?

# two nested lists
l_one = [1,2,[3,4]]
l_two = [1,2,{'k1':4}]

# True or False?
l_one[2][0] >= l_two[2]['k1']

answer = False

print('This Test Has Ended! ' * 4) '''













'''
####################################################################################################################
# Statements Test
####################################################################################################################
sectionName = "Statments"
print(f'{sectionName} Test' * 8)

#Use for, .split(), and if to create a Statement that will print out words that start with 's':

#Code here
st = 'Print only the words that start with s in this sentence'
st = st.split()
for word in st:
    if word[0] == 's':
        print(word)

#Use range() to print all the even numbers from 0 to 10.

#Code Here
for num in range(0,11,2):
    print(num)

#Use a List Comprehension to create a list of all numbers between 1 and 50 that are divisible by 3.

#Code here
[print(num) for num in range(1,51) if num % 3 == 0]

#Go through the string below and if the length of a word is even print "even!"

#Code here
st = 'Print every word in this sentence that has an even number of letters'
for word in st.split():
    if len(word) % 2 == 0:
        print('even!')

#Write a program that prints the integers from 1 to 100. But for multiples of three print "Fizz" instead of the number, and for the multiples of five print "Buzz". For numbers which are multiples of both three and five print "FizzBuzz".

#Code here
for num in range(1,101):
    if num % 3 == 0 and num % 5 == 0:
        print('FizzBuzz')
    elif num % 5 == 0:
        print('Buzz')
    elif num % 3 == 0:
        print('Fizz')

#Use List Comprehension to create a list of the first letters of every word in the string below:

st = 'Create a list of the first letters of every word in this string'

#Code here
firstLetters = []
[word[0] for word in st.split(' ')]
print(firstLetters)'''