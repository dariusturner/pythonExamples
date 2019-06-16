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




# Functions Section
################################################################################################
sectionName = 'Functions'
print(f'{sectionName} Section')

#Append() adds a value to the end of the list, set, str, etc..
myList = []
myList.append('added value')

#Pop() removes the value at the end of the list,set, str, etc..
myList.pop()

#Help() prints the definition of functions and can help you learn functions on the go to use
#help(myList.count('e'))


#########################################################
#How to Create a Function
#########################################################

# Example of how to create a function
friend = 'Jason'

def sayHello():
    '''
    A function to print Hello to your friend.
    Input: no input
    Output: Hello friend's name!
    '''
    print('Hello ' + friend + '!')

sayHello()

#Add an input and have a default for input value incase one isn't added when the function is called
def findPercentage1(num = 0):
    num = num/100.00
    print(f'{num} %')

findPercentage1(93842.66)

#Make sure you return the result otherwise you can't save the result to a variable, etc...
def findPercentage2(num = 0):
    num = num/100.00
    return f'{num} %'



myPercent = findPercentage2(93842.66)
print(myPercent)

# Example of multiple inputs
def add(a,b):
    return a+b

add(30,30)

# Find out if there the word "car" is in the string even if "car" is capatalized
######### in - makes a boolean statement by itself so you don't need an if statement
def carCheck(str):
    return 'car' in str.lower()

# Pig Latin
def pigLatin(word):

    firstLetter = word[0]
    
    #Check if vowel
    if firstLetter.lower() in 'aeiou':
        pig_word = word + 'ay'
    else:
        pig_word = word[1:] + firstLetter + 'ay'

    return pig_word

print(pigLatin('Order'))


# *args and **kwargs Section
sectionName = '*args and **kwargs'
print(f'{sectionName} Section')

##### *args and **kwargs stand for Arguements and Keyword Arguements ####

# *args allow you to pass as many arguements as you would like
def argsFunc(*args):
    # Returns 5% of the sum of a and b
    return sum(args) * 0.05

# **kwargs handles an as many keyword arguements as you would like

def kwargsFunc(**kwargs):
    if 'fruit' in kwargs:
        print('My fruit of choice is {}'.format(kwargs['fruit']))
    else:
        print('I did not find any fruit here')

kwargsFunc(fruit='pineapple', veggie='asparagus')

# Can use both arguements at the same time
def combineArgsFunc(*args,**kwargs):
    print(args)
    print(kwargs)
    print('I would love to have {} of your best {} please!'.format(args[0], kwargs['meat']))

combineArgsFunc(2,5,6,8, meat='wagyu', dish='chicken parmesean')



# Lambda Expressions - Map & Filter Section
########################################################################################################
sectionName = 'Lambda Expressions - Map & Filter Section'
print(f'{sectionName} Section')

### Map function is used to be a simplified for loop for adding a function or making changes to all of a lists indexes more efficiently
def cubed(num):
    return num**3

my_nums = [1,2,3,4,5]

for index in map(cubed,my_nums):
    print(index)

# Or if you want the List back rather than each index

print(list(map(cubed,my_nums)))

def findEvenStr(myString):
    if len(myString) % 2 == 0:
        return 'Even'
    else:
        return myString[0]

names = ['Andy','Eve', 'Steve']

print(list(map(findEvenStr,names)))

# Filter function filters values if they are true or false regarding the statement

def check_even(num):
    return num%2 == 0

my_nums = [1,2,3,4,5,6]

print(list(filter(check_even,my_nums)))

for index in filter(check_even,my_nums):
    print(index)

# Lambda Expressions are like one time functions

lambda num: num**2

# Fast way to add simple functions in a map or filter functions
print(list(map(lambda num: num**2, my_nums)))

print(list(filter(lambda num: num%2 == 0, my_nums)))

print(list(map(lambda name: name[0:3], names)))












































































'''

##########################################################
#Function Exercises Section
##########################################################
sectionName = 'Function Exercises'
print('{} Section'.format(sectionName))

###### WARM UP #################

#LESSER OF TWO EVENS: Write a function that returns the lesser of two given numbers if both numbers are even, but returns the greater if one or both numbers are odd
#lesser_of_two_evens(2,4) --> 2
#lesser_of_two_evens(2,5) --> 5

def lesser_of_two_evens(a,b):
    if a % 2 == 0 and b % 2 == 0:
        return min(a,b)
    else:
        return max(a,b)


# Check
print(lesser_of_two_evens(2,4))

# Check
print(lesser_of_two_evens(2,5))

#ANIMAL CRACKERS: Write a function takes a two-word string and returns True if both words begin with same letter
#animal_crackers('Levelheaded Llama') --> True
#animal_crackers('Crazy Kangaroo') --> False

def animal_crackers(text):
    words = text.lower().split()
    return words[0][0] == words[1][0]

# Check
print(animal_crackers('Levelheaded Llama'))

# Check
print(animal_crackers('Crazy Kangaroo'))

#MAKES TWENTY: Given two integers, return True if the sum of the integers is 20 or if one of the integers is 20. If not, return False
#makes_twenty(20,10) --> True
#makes_twenty(12,8) --> True
#makes_twenty(2,3) --> False

def makes_twenty(n1,n2):
    return (n1 + n2) == 20 or n1 == 20 or n2 == 20


# Check
print(makes_twenty(20,10))

# Check
print(makes_twenty(2,3))


####### Level 1 Problems #################

#OLD MACDONALD: Write a function that capitalizes the first and fourth letters of a name
###old_macdonald('macdonald') --> MacDonald

#Note: 'macdonald'.capitalize() returns 'Macdonald'

def old_macdonald(name):
    firstLetter = name[0]
    fourthLetter = name[3]
    afterFirst = name[1:3]
    afterFourth = name[4:]
    return firstLetter.capitalize() + afterFirst + fourthLetter.capitalize() + afterFourth

# Check
print(old_macdonald('macdonald'))

#MASTER YODA: Given a sentence, return a sentence with the words reversed¶
###master_yoda('I am home') --> 'home am I'
###master_yoda('We are ready') --> 'ready are We'

def master_yoda(text):
    words = text.split()
    return ' '.join(words[::-1])

# Check
print(master_yoda('I am home'))

# Check
print(master_yoda('We are ready'))


#ALMOST THERE: Given an integer n, return True if n is within 10 of either 100 or 200
###almost_there(90) --> True
###almost_there(104) --> True
###almost_there(150) --> False
###almost_there(209) --> True

###NOTE: abs(num) returns the absolute value of a number

def almost_there(n):
    if n - 100 >= -10 and n - 100 <= 10:
        return True
    elif n - 200 >= -10 and n - 200 <= 10:
        return True
    else:
        return False 

# Check
print(almost_there(104))

# Check
print(almost_there(150))

# Check
print(almost_there(209))


############### Level 2 Problems ###############

#Given a list of ints, return True if the array contains a 3 next to a 3 somewhere.
###has_33([1, 3, 3]) → True
###has_33([1, 3, 1, 3]) → False
###has_33([3, 1, 3]) → False

def has_33(nums):
    for index in range(len(nums) -1):
        if (nums[index] == 3) and (nums[index + 1] == 3):
            return True
    return False


# Check
print(has_33([1, 3, 3]))

# Check
print(has_33([1, 3, 1, 3]))

# Check
print(has_33([3, 1, 3]))

#PAPER DOLL: Given a string, return a string where for every character in the original there are three characters
####aper_doll('Hello') --> 'HHHeeellllllooo'
####paper_doll('Mississippi') --> 'MMMiiissssssiiippppppiii'

def paper_doll(text):
    answer = ''
    for letter in text:
        answer = answer + (letter * 3)
    return answer

# Check
print(paper_doll('Hello'))

# Check
paper_doll('Mississippi')


#BLACKJACK: Given three integers between 1 and 11, if their sum is less than or equal to 21, return their sum. If their sum exceeds 21 and there's an eleven, reduce the total sum by 10. Finally, if the sum (even after adjustment) exceeds 21, return 'BUST'
####blackjack(5,6,7) --> 18
####blackjack(9,9,9) --> 'BUST'
####blackjack(9,9,11) --> 19

def blackjack(a,b,c):
    sum = a + b + c
    if sum <= 21:
        return sum
    elif sum > 21 and (a == 11 or b == 11 or c == 11):
        return sum - 10
    else:
        return 'BUST'

# Check
print(blackjack(5,6,7))

# Check
print(blackjack(9,9,9))

# Check
print(blackjack(9,9,11))


#SUMMER OF '69: Return the sum of the numbers in the array, except ignore sections of numbers starting with a 6 and extending to the next 9 (every 6 will be followed by at least one 9). Return 0 for no numbers.
###summer_69([1, 3, 5]) --> 9
###summer_69([4, 5, 6, 7, 8, 9]) --> 9
###summer_69([2, 1, 6, 9, 11]) --> 14

def summer_69(arr):
    
    sum = 0
    add = True
    
    for num in arr:
        while add:
            if num != 6:
                sum += num
                break
            else:
                add = False
        while not add:
            if num != 9:
                break
            else:
                add = True
                break
    return sum 
        

# Check
print(summer_69([1, 3, 5]))

# Check
print(summer_69([4, 5, 6, 7, 8, 9]))

# Check
print(summer_69([2, 1, 6, 9, 11]))


########## Challenging Problems ##########

#SPY GAME: Write a function that takes in a list of integers and returns True if it contains 007 in order
 ###spy_game([1,2,4,0,0,7,5]) --> True
 ###spy_game([1,0,2,4,0,5,7]) --> True
 ###spy_game([1,7,2,0,4,5,0]) --> False

def spy_game(nums):
    spy = [0,0,7,'done']
    for num in nums:
        if num == spy[0]:
            spy.pop(0)
    return len(spy) == 1

# Check
print(spy_game([1,2,4,0,0,7,5]))

# Check
print(spy_game([1,0,2,4,0,5,7]))

# Check
print(spy_game([1,7,2,0,4,5,0]))

#COUNT PRIMES: Write a function that returns the number of prime numbers that exist up to and including a given number
####count_primes(100) --> 25

#By convention, 0 and 1 are not prime.

def count_primes(num):
    if num < 2:
        return 0
    
    primes = [2]
    x = 3

    while x <= num:
        for y in range(3,x,2):
            if x%y == 0:
                x += 2
                break
        else:
            primes.append(x)
            x += 2
    print(primes)
    return len(primes)


# Check
print(count_primes(100))
'''































##########################################################
#Functions and Methods Homework Section
##########################################################
sectionName = 'Functions and Methods Homework'
print(f'{sectionName} Section')

# Write a function that computes the volume of a sphere given its radius

def vol(rad):
    result = round(4/3 * (3.14 *(rad**3)), 2)
    return f'The volume of a sphere with a radius of {rad} is {result}'

print(vol(1))


# Write a function that checks wheather a number is in a give range (Inclusive of high and low)

def ran_check(num,low,high):
    if num >= low and num <= high:
        return 'Your number is inside the given range of {} to {}'.format(low,high)
    else:
        return 'Your number was not found inside the range of {} to {}'.format(low,high)

print(ran_check(9,9,10))

# If you only wanted to return a Boolean

def ran_bool(num,low,high):
    return num in range(low, high + 1)

print(ran_bool(-11,-10,4))

# Write a function that accepts a string and calculates the number of upper and lowercase letters
##### I did it this way that way you if you would want a list to print or return the letters that are uppercase and lowercase ########
def up_lows(s):
    uppers = []
    lowers = []
    for index in s:
        if index.isupper():
            uppers.append(index)
        elif index.islower():
            lowers.append(index)
        else:
            pass
    return "There were {} uppercase letters and {} lowercase letters in the string '{}'".format(len(uppers),len(lowers),s)

print(up_lows('Hell0'))


# Write a function that takes a list and returns a new list with unique elements in the first list

def unique_list(l):
    return set(l)

print(unique_list([1,2,2,3,3,4,6,6,4,5,9,2]))

# Write a function that multiplies all the numbers in a list together

def mult_list(l):
    result = 1
    for index in l:
        result *= index
    return result

print(mult_list([2,3,6]))

# Write a function that is a palindrome (word or phrase that reads the same backwords)

def palindrome(s):
    return s.lower() == s[::-1].lower()
       

print(palindrome('helleh'))

# Write a function to check if a string is a panagram or not

import string

def ispanagram(str1, alphabet = string.ascii_lowercase):
    alphset = set(alphabet)
    return alphset <= set(str1.lower())

print(ispanagram('The quick brown fox jumps over the lazy dog'))
        



































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

