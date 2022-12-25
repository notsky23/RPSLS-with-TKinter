# GUI-based version of RPSLS

###################################################
# Student should add code where relevant to the following.


import random
from tkinter import *

# Functions that compute RPSLS
def name_to_number(name):
    if name.lower() == "rock":
        return 0
    elif name.lower() == "spock":
        return 1
    elif name.lower() == "paper":
        return 2
    elif name.lower() == "lizard":
        return 3
    elif name.lower() == "scissors":
        return 4
    else:
        return "Error: invalid name!"
    
def number_to_name(number):
    if number == 0:
        return "rock"
    elif number == 1:
        return "Spock"
    elif number == 2:
        return "paper"
    elif number == 3:
        return "lizard"
    elif number == 4:
        return "scissors"
    else:
        return "Error: invalid number!"    
     
    
# Handler for input field
def get_guess(guess):
    print()
    print("Player Choice is... " + guess)
    player_number = name_to_number(guess)
    computer_number = random.randrange(0, 5)
    computer_name = number_to_name(computer_number)
    print("Computer Choice is... " + computer_name)

    if isinstance(player_number, int):
        difference = (player_number - computer_number) % 5

        if (difference > 0) and (difference <= 2):
            print("The winner is... Player!")
        elif (difference > 2) and (difference <= 4):
            print("The winner is... Computer!")
        elif (difference == 0):
            print("It's a draw... try again!")

    else:
        print("Error: invalid input")


    # if not isinstance(difference, int):
    #     print("Error: invalid input")
    # elif (difference > 0) and (difference <=2):
    #     print("The winner is... Player!")
    # elif (difference > 2) and (difference <=4):
    #     print("The winner is... Computer!")
    # elif (difference == 0):
    #     print("It's a draw... try again!")


def main():
    # Create frame and assign callbacks to event handlers
    window = Tk()
    window.title("ROCK-PAPER_SCISSORS_LIZZARD-SPOCK")
    window.geometry('150x150')

    # Label
    lbl = Label(window, text="Enter guess for RPSLS")
    lbl.grid(column=0, row=0)

    # Input text
    txt = Entry(window, width=20)
    txt.grid(column=0, row=1)
    txt.focus()

    def process(event=None):
        content = txt.get() # get contents of entry widget
        get_guess(content)
        txt.delete(0, END)

    txt.bind('<Return>', process)

    # Start the frame animation
    print("GAME START:")
    window.mainloop()


if __name__ == "__main__":
    main()


###################################################
# Test

# get_guess("Spock")
# get_guess("dynamite")
# get_guess("paper")
# get_guess("lazer")

###################################################
# Sample expected output from test
# Note that computer's choices may vary from this sample.

#Player chose Spock
#Computer chose paper
#Computer wins!
#
#Error: Bad input "dynamite" to rpsls
#
#Player chose paper
#Computer chose scissors
#Computer wins!
#
#Error: Bad input "lazer" to rpsls
#