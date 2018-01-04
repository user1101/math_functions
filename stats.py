#This program will be a statistical tool 

import random
import sys
import os
import math
import datetime

statslist = raw_input('Designate a name for the generated statistics file: ')

get = int(input('Enter the # of numbers of sample events for your problem: '))

i = 1

n = 0

sumt = []

sortsum = sumt

while (i <= get):
    x = int(input('\nEnter a number: '))
    sumt.append(x)
    #print ('You entered' + i + '.')
    i = i+1

a = mean(sumt)

b = median(sumt)

c = mode(sumt)

d = stdev(sumt)

e = variance(sumt)

# Printing the file for the statistical analysis

f = statslist
f = open (statslist, "w")
print >> f, ('\nThe following statistical measurements have printed at: ' + str(datetime.datetime.now()))

print >> f, ('\nThis is a list of your sample events from least to greatest.')
while (n < get):
    print ('\n' +[n] + '. ' + str(sumt[n]))
    n = n+1

print >> f, ('\nThe mean of your sample events is: ' + str(a) )
print >> f, ('\nThe median of your sample events is: ' + str(b) )
print >> f, ('\nThe mode of your sample events is: ' + str(c) )
print >> f, ('\nThe standard deviation of your sample events is: ' + str(d) )
print >> f, ('\nThe standard variance of your sampele events is: ' + str(e) )
f.close()

print ('The file: ' + str(statslist) + 'has been generated at: ' + str(datetime.datetime.now()) )




    
 
