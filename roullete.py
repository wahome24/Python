# You are going to write a program which will select a random name from a list of names. The person selected will have to pay for everybody's food bill.

import random

print('welcome to russian roullete!')
print()
print('You get to randomly select who pays the bill!')
print()

#split function will store the names in a list

choice = input('Enter a list of names separated by comma:\n').split(',')
#Generates a random integer
result = random.randint(0,len(choice)-1)

#Using the random index to select who pays the bill.
print('Drum rolls please, {} you get to pay the bill. Happy spending!'.format(choice[result]))

