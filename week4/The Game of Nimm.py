"""
File: The Game of Nimm.py
The ancient game of Nimm:
Win: doesn't pick up the last stone
Lose: picks up the last stone
"""

def main():
    #initializing variables to act as counters
    stones = 20
    turn_counter = 0
    
    while stones > 0:
        print("There are "+str(stones)+" stones left.")  # prints how many stones left
        
        #Turn counter
        turn_counter += 1
        
        #Used to determine current players' turn
        if turn_counter % 2 == 0:
            player = 1
        else:
            player = 2
        
        #asks the user how many stones to remove
        remove_stones = int(input("Player " + str(player) +" would you like to remove 1 or 2 stones? "))
   
        #verifies proper input
        while remove_stones != 1 and remove_stones != 2:
            remove_stones = int(input("Please enter 1 or 2: "))

        #create a line break between each player's turn
        print("")
        
        #calculates the remaining amount of stones
        stones = stones - remove_stones
        
    
    #when stones hit 0, the game is finished
    #announce winner
    if player == 1:
        winner = 2
    else:
        winner = 1
    print("Player " + str(winner) +" wins!")
