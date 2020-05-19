#!/bin/python3


#first computer makes a choise, after that user inputs their choise. After that I've compared them and showed the result.

from random import randint

chosen = randint(1,3)      #Computer's random choise it made

print('I have assighned O for rock, ___ for paper and >8 for sissors to denote it.\n')
player = input('Please make your choise: rock (r), paper (p) or scissors (s)? ') #Player makes their choise.


if(chosen == 1):
  computer = 'r'
  print('O   ')

elif(chosen == 2):
  computer = 'p'
  print('___   ')

else:
  computer = 's'
  print('>8   ')

#----------------------------------------------------------------------

print('vs  ')

#----------------------------------------------------------------------

if(player == 'r'):
  print('O')

elif(player == 'p'):
  print('___')

elif(player == 's'):
  print('>8')

else:
  print('??')

#----------------------------------------------------------------------

if(chosen == 1):
  computer = 'r'
  print('O')

elif(chosen == 2):
  computer = 'p'
  print('___')

else:
  computer = 's'
  print('>8')

#-----------------------------------------------------------------------

if(player == computer):
  print('DRAW!')

elif(player == 'r' and computer == 's'):
  print('Rock breaks scissors!')

elif(player == 'r' and computer == 'p'):
  print('Paper covers rock!')

elif(player == 'p' and computer == 'r'):
  print('Paper covers rock!')

elif(player == 'p' and computer == 's'):
  print('Scissors cuts paper!')

elif(player == 's' and computer == 'p'):
  print('Scissors cuts paper!')

elif(player == "s" and computer == 'r'):
  print('Rock breaks scissors!')

else:
  print('Something went wrong.')

