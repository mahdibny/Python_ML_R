

# For loop in python
price = 20
for x in range (10):  
    price = price + 1
print (price)

# For loop startes at 1, goes to 10, step of 2
for x in range (1,10,2):
    print (x)

# Accepting input from the user and pringing it out
name = input ('What is your name? ')
print ('Hi '+ name)

# Accepting input, converting string to int, do some math
birth_year = input ('Birthyear: ')
age = 2023 - int (birth_year)
print (age)
print (type(age))

# Formated string, better way to print large messages
first = 'John'
last = 'Smith'
msg = f'{first} [{last}] is a coder'
print (msg)

# String methonds
course = 'Python for Beginners'
print (len(course)) # returns lenght of string, course
# Course. --> will give you all functions that can be used in string

# Math
import math
#then do math. --> can show off the math functions

# Lists, small array, if you do list_variable name. --> methods for list
# 2D Lists, like a matrix
TD_m = [
    [1,2,3,4],
    [5,6,7,8],
    [9,10,11,12]
]

for x in TD_m:
    for y in x:
        print (y)

'''
for x in range (len(TD_m)):
    for y in range (len(TD_m[x])):
        print (TD_m[:y])
'''

# Tuple --> data structure where the values will be unchanged
coordinates = [1,2,3]
n,m,o = coordinates

# Dictonaries
# can put in multiple values that are paired

customer = {
    "name":"John Smith",
    "age": 30,
    "is_verified": True
}

print (customer.get("name")) # access of values, but will give none is not a variable in dictonary


# Creating a function
# functions can have aruments that can be used in the program
# can have *args as multiple parameters without a limit
def greet_user():
    print ('Hello there')
    print ('Welcome aboard')

greet_user()

def square (number):
    return (number*number)
print (square(10))

# Classes
class Point:
    def __init__(self, x_cord, y_cord):
        self.x_cord=x_cord
        self.y_cord=y_cord

    def move(self):
        print ("move")

    def draw(self):
        print("draw")

point1 = Point(10,1)
point1.draw()

# Inheritence 
# create a class with argument (of parent class)
# print (help (class_name))) --> can give you information about parent class
class Coordinate(Point):
    def __init__(self, x_cord, y_cord,continent):
        super().__init__(x_cord, y_cord)
        self.continent=continent



