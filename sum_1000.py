#This program will be a counter up to 1000

import random
import sys
import os

i = 1

sumt = []

while (i <= 1000):
    sumt.append(int(i))
    print i
    i = i+1

print ('\nThe sum of the numbers from 1 to 1000 is ' + str(sum(sumt)) + '.')


#numbers = str(raw_input("Enter a filename: "))

#sums = int(raw_input("\nEnter the amount of numbers you want to add together: "))

#tablex = []

#upx = tablex

#i = 0

#n = 0

#while (i < sums):
#    tablex.append(int(raw_input("\nEnter a number: ")))
#    i = i+1

#f = numbers
#f = open (numbers, 'w')
#while (n < sums):
#    print >> f, upx[n]
#    n = n+1
##print the sum
#print >> f, sum(upx)
#f.close()

#print("\nThe sum of the numbers is " + str(sum(upx)) + '.')


    
 
