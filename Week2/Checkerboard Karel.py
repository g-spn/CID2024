from karel.stanfordkarel import *

"""
Karel will fill the world with a checkerboard pattern regardless of size. 
"""


def main():
    """
    Karel will fill the world with a checkerboard pattern
    """
    while left_is_clear():
        #odd number rows of Beeper
        #Purpose: Create a start point for each row regardless of size of world
        odd_row_beeper()
        #karel moves up a row
        karel_row_up()
        #even number rows
        #purpose: karel creates a row of beepers for even rows
        even_row_beeper()
        #karel moves up a row
        if left_is_clear():
            karel_row_up()
    #Checking to see if odd number row to fill the last row        
    check_make_top_row()
    #return to starting point
    return_start_point()

def check_make_top_row():
    """
    Karel makes the laws row for odd numbers
    pre:if row is clear due to odd number, makes row
    post: karel is at top row, first col with last row made.
    """
    if left_is_blocked():
        turn_right()
        move()
        if no_beepers_present():
            turn_around()
            move()
            turn_right()
            odd_row_beeper()
        else:
            turn_around()
            move()
            turn_right()

def return_start_point():
    """
    Returns to the initial starting point of the world
    pre: Karel is in the first column
    post: karel is in the first column in the first row. (starting point)
    """
    turn_right()
    while front_is_clear():
        move()
    turn_left()
def even_row_beeper():
    while front_is_clear():
        move()
        put_beeper()
        if front_is_clear():
            move()
    return_first_col()

def karel_row_up():
    """
    Karel moves up a row
    Pre: Karel is in the first column of a row
    Post: Karel is a row about in the first column
    """
    turn_left()
    move()
    turn_right()

def odd_row_beeper():
    """
    Karel will place beepers on the bottom row, leaving a space between each beepr
    #pre:Karel starts at bottom left.
    #post:Karel ends at bottom left, and beepers is placed in the romw
    """
    if front_is_blocked():
        put_beeper()
    while front_is_clear():
        put_beeper()
        move()
        if front_is_clear():
            move()
    check_last_col()
    return_first_col()

def check_last_col():
    """
    Karel checks if the last column of the row needs a beeper or not
    pre: Karel at the end of the row
    post:Karel at the end of the row with a beeper or without. 
    """
    if front_is_blocked():
        turn_around()
        if front_is_clear():
            move()
            if beepers_present():
                turn_around()
                move()
            else:
                turn_around()
                move()
                put_beeper()
        else:
            turn_around()

def return_first_col():
    turn_around()
    while front_is_clear():
        move()
    turn_around()

def turn_right():
    #Unable to turn right, we have Karel turn left 3 times.
    for i in range(3):
        turn_left()

def turn_around():
    #purpose it turns Karel around
    for i in range(2):
        turn_left()
    


# There is no need to edit code beyond this point
if __name__ == '__main__':
    main()
