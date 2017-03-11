# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console

import simplegui
import random
import math

# helper function to start and restart the game
def new_game():
    global secret_number
    global guesses
    guesses =7
    update_display()
   
    
def update_display():
    global guesses
    print  "You have " + str(guesses) + " guesses remaining"

# define event handlers for control panel
def range100():
    # button that changes the range to [0,100) and starts a new game 
    global secret_number
    secret_number = random.randrange(0,100)
    global guesses
    guesses = 7
    new_game()
        
    

def range1000():
    # button that changes the range to [0,1000) and starts a new game     
    global secret_number
    secret_number = random.randrange(0,1000)
    new_game()
    
def input_guess(guess):
    guess = int(guess)
    print guess
    global guesses
     
    if guesses<1:
        print "YOU LOSE, GOOD DAY SIR!"
        
    if guess > secret_number:
        print "The number is lower"
        guesses = guesses - 1
        update_display()
        
    elif guess < secret_number:
        print "The number is higher"
        guesses= guesses -1
        update_display()
    else:
        print "Correct!"
        
       
# create frame
frame = simplegui.create_frame("Guess the Number",100,200)
input = frame.add_input("Guesses",input_guess,50)
frame.add_button("Range 100", range100, 50)
frame.add_button("Range 1000", range1000, 50)

# call new_game 
new_game()



