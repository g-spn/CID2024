from karel.stanfordkarel import *

"""
File: Midpoint Karel..py
--------------------
Karel should be able to find
the midpoint regardless of world size
note: world size must have same height and width.
"""

def main():
    
    #creates a diagonal of beepers from
    #1,1 top right corner
    diagonal_of_beepers()
    #Moves to the bottom right corner
    #precursor to find midpoint
    move_bottom_right_corner()
    find_mid_point()
    place_mid_point()
    clean_up_diag()
    move_to_start()
    move_to_mid()


def diagonal_of_beepers():
    #Purpose is to create a diagonal of beepers
    #Pre: Starts at 1,1 with no beepers
    #Post: End top right corner with a diagonal of beepers
    while front_is_clear():
        put_beeper()
        move()
        turn_left()
        move()
        turn_right()
    #fense post
    put_beeper()

def move_bottom_right_corner():
    #move to the bottom right corner, a precursor to help find midpoint locations
    #pre: Karel is in the top right corner
    #post: Karel is bottom right corner facing west
    turn_right()
    while front_is_clear():
        move()
    turn_right()

def find_mid_point():
    #find the midpoint of the initial diagonal
    #pre: bottom right corner of the world
    #post: on top of the midpoint of the diagonal.
    while no_beepers_present():
        move()
        turn_right()
        if no_beepers_present():
            move()
        turn_left()

def place_mid_point():
    #Karel has found midpoint, and places beepers in the first row of the midpoint
    #Pre: Karel is on a beeper on the first diagonal line
    #post: Karel is in the first row at the midpoint

    turn_left()
    while front_is_clear():
        move()
    put_beeper()

def clean_up_diag():
    #clears up diag
    #pre: Karel is in the first row at the midpoint location
    #post: top right corner with the diag clear
    while not_facing_west():
        turn_right()
    while front_is_clear():
        move()
    turn_around()
    while front_is_clear():
        pick_beeper()
        move()
        turn_left()
        move()
        turn_right()
    #fense post
    pick_beeper()

def move_to_start():
    #After cleaning up the beepers Karel is at the top right corner
    #pre: Karel is top right
    #post: Karel is at the starting point 
    turn_around()
    while front_is_clear():
        move()
    turn_left()
    while front_is_clear():
        move()
    turn_left()

def move_to_mid():
    #Only one beeper is present which is the midpoint of the bottom row
    #pre: Karel is at the starting point 
    #post: on top of midpoint
    while no_beepers_present():
        move()

def turn_around():
  #purpose is to do an about-face. 
  #pre: Faces east(example)
  #post: Faces west(example) 
    for i in range(2):
        turn_left()

def turn_right():
  #turning right is not possible in karels. 
  #3 lefts make a right turn. 
    for i in range(3):
        turn_left()

if __name__ == '__main__':
    main()
