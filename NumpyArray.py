#array arange zeros ones linspace eye random


#create an array from an existing list or tuples
#To make use of the rray wwe need to import the numpy tool
'''
Numpy has the following tools in it
1. array        2. arange
3. Zeros        4. ones
5. linspace     5. Random
'''

#creating an array
'''
an array is almost the same as a list. However, unlike in lists where we can store different data types,
 arrays are used to store files of the same data type. Example: Imagine storing an array of the goalkeepers in a team:
 
An array can be created from a list or a tuple
'''
import numpy as np

goalkeepers = ['De Gea', 'Henderson', 'Lee Grant', 'Tom Heaton',]
print(type(goalkeepers)) #this gives us a list data type

#To convert to an array: we make use of "np.array" example below:

goalkeepers = np.array(['De Gea', 'Henderson', 'Lee Grant', 'Tom Heaton',])   #using a list
print(goalkeepers)
print(type(goalkeepers))

#using a tuple
b = ('De Gea', 'Henderson', 'Lee Grant', 'Tom Heaton',)
print(type(b))
#converting it to a tuple
b = np.array(('De Gea', 'Henderson', 'Lee Grant', 'Tom Heaton',))
print(b)
#use type to know the data type
print(type(b))



#creating a matrix with lists

strikers = ['Cavani', 'Benzema', 'Aguero', 'Werner']
goals = [16, 23, 15, 9]
strongfoot =  ['right', 'right', 'right', 'left']

strikermatrix = [strikers, goals, strongfoot]
print(np.array(strikermatrix))

#Numpy arange
#works just as the range function

a = np.arange(0,15, 3)
print(a)
#where 0 is the start point - optional, 15 is the end point - is exclusive and must be included,
# 3 is the step - the number it increments by, and dtype - optional. when step is not added, it is important to include
#the word "dtype = ".
# Note: the quotes should not be added. But if steps is included, "dtype" does not need to be added.

#3. Zeros - creates as array filled with zeros. Example:
g = np.zeros(3) #this requires one positional argument. The 3 in the brackets refers to the shape of the array
print(g)

#when a second argument is passed, it is necessary to include another outside set of brackets
g = np.zeros((3,4)) #this creates a matrix where 3 is the row and 4 becomes the column, the default value is a
print(g)                #float data type. to change the data type,

g = np.zeros((3,4), int)
print(g)

#the ones tool works the same way as zeros, creates an array filled with ones
f = np.ones(3)
print(f)

f = np.ones((3,4))
print(f)                     #this creates a matrix where 3 is the row and 4 becomes the column, the default value is a
                             #float data type. to change the data type,


f = np.zeros((3,4), int)
print(f)


'''
Random data with arrays
'''

print(np.random.rand()) #gives a random number between 0 and 0.9999999~.
print(np.random.rand(5,2)) #passing an argument into the brackets specify the shape of the array.
print(np.random.rand(5,5, 2)) #three arguments are passed in the brackets, this creates a 5 by 2 matrix in 5 places
print(np.random.randint(1, 5, 4,)) #passing an third argument here creates a 4 column single matrix
print(np.random.choice(f))
'''
strikers = ['Cavani', 'Benzema', 'Aguero', 'Werner']
goals = [16, 23, 15, 9]
strongfoot =  ['right', 'right', 'right', 'left']

np.array(strikers)
print(type(strikers))
goals = np.array(goals)
strongfoot = np.array(strongfoot)
print(type(goals))

print(goals.max())
print(goals.min())
print(goals.argmax())
print(goals.argmin())
f = strikers[goals.argmax()]
print(f)'''