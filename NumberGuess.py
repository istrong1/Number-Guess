"""This program is a number guess game, it will roll a pair of dice and then ask you to guess the sum of the roll. If your guess is equal or greater than the total value, you win. Otherwise, the computer wins. Good luck! """

from random import randint
from time import sleep

def get_user_guess():
  guess = int(raw_input("Enter your guess: "))
  return get_user_guess
# function that promps user for their guess

def roll_dice(number_of_sides):
  first_roll = randint(1, number_of_sides)
  second_roll = randint(1, number_of_sides)
  max_val = number_of_sides * 2
  print "The maximum possible value is: %d" % max_val
  guess = get_user_guess()
  if guess < max_val:
    print "Please guess a number below the max!"
  else:
    print "Rolling..."
    sleep(2)
    print "The 1st roll is: %d" % first_roll
    sleep(1)
    print "The 2nd roll is: %d" % second_roll
    sleep(1)
    total_roll = first_roll + second_roll
    print total_roll
    print "Result..."
    sleep(1)
    if guess > total_roll:
      print "Congratulation you won!"
    else:
      print "You lost, try again."
      
roll_dice(6)
