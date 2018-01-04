#This program will be a counter up to 1000

import random
import sys
import os

get = int(input('Enter the # of numbers you want to count and sum: '))

i = 1

n = 0

sumt = []

sortsum = sumt

while (i <= get):
    x = int(input('\nEnter a number: '))
    sumt.append(x)
    #print ('You entered' + i + '.')
    i = i+1

print ('\nThe sum of your numbers is ' + str(sum(sumt)) + '.')

sumt.sort()

print ('\nThis is a list of your numbers from least to greatest.')

while (n < get):
    print ('\n' + str(sumt[n]) )
    n = n+1




    
 
