# Rock-paper-scissors-lizard-Spock template


# The key idea of this program is to equate the strings
# "rock", "paper", "scissors", "lizard", "Spock" to numbers
# as follows:
#
# 0 - rock
# 1 - Spock
# 2 - paper
# 3 - lizard
# 4 - scissors

# helper functions

import math
import random

def name_to_number(name):
    if name == "rock":
        return 0
    elif name == "Spock":
        return 1
    elif name=="paper":
        return 2
    elif name== "lizard":
        return 3
    elif name== "scissors":
        return 4
    else: print "Not a valid input string"
    

def number_to_name(number):
    if number == 0:
        return "rock"
    elif number ==1:
        return "Spock"
    elif number == 2:
        return "paper"
    elif number == 3:
        return "lizard"
    elif number ==4:
        return "scissors"
    

def rpsls(player_choice): 
    
    player_number = name_to_number(player_choice)
    comp_number= random.randrange(0,5)
    difference=( player_number - comp_number) % 5;
    if difference == 0:
        result="Player and computer tie!"
    elif difference == 1 or difference ==2:
        result = "Player wins!"
    else:
        result= "Computer wins!"
    print
    print "player chooses " + player_choice
    comp_choice = number_to_name(comp_number);
    print "computer chooses " + comp_choice
    print result

    
# test code 
rpsls("rock")
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")



