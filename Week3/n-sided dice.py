"""
A program that takes as input the number of sides on a dice. 
Then, simulate rolling a dice with that many sides. 
Print the outcome of the roll.
"""
# imports a standard library
import random

def main():
    #user inputs the number of sided dice to be used
    n_side_dice = int(input("How many sides does your dice have?"))
    
    #Display a random number within the user's input
    print("Your roll is " + str(random.randint(1,n_side_dice)))

if __name__ == '__main__':
    main()
