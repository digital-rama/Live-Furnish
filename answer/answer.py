import random

"""
Question Number 3 --->

Write a one line code to print the reverse of words in an input string. For eg. if input
is - “Me And You” then output will be “You And Me”.
"""

print(input("Enter a Sentence to Reverse\n\n")[::-1])





"""
Write an optimize solution -

Given a list of unique numbers for eg. - mylist = [1, 2, 3, 4, 5, 6, 7 ,8,9,10].
Write a function to iterate through the list and pick a random number in each
iteration. No number should repeat i.e. in each iteration the random number should
be unique and should not have been picked before.

Note - 
1. You can not use another list, array, dictionary etc. You can only use the
given list.

2. You can not remove any element from the given list (mylist).

3. This list can be of 100000 numbers or more than that so write an
optimized solution for this.
"""


my_list = [1, 2, 3, 4, 5, 6, 7 ,8 ,9 ,10]

# A function to generate a random values of List[] 
def randomize (arr): 
    for i in range(len(arr)-1,0,-1):  
        j = random.randint(0,i+1)
        arr[i],arr[j] = arr[j],arr[i] 
    return arr 

print(randomize(my_list)) 