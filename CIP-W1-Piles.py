# Code in Place 2024 
# Exercise name: Piles

from karel.stanfordkarel import *

# File: piles.py
# -----------------------------
# The warmup program defines a "main"
# function which should make Karel
# pick up all the beepers in the world.
def main():
    # Continuesly moves forwards while picking up all beepers.
    while front_is_clear():
        move()
        while beepers_present():
            pick_beeper()
   
   
# don't edit these next two lines
# they tell python to run your main function
if __name__ == '__main__':
    main()
