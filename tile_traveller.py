"""
A simple game, the user is on a tile in a 3x3 grid. 
When the user reaches a certain tile he attains victory.
Each turn the user is told which directions he can travel.
If he tries to move in a direction that is not available he recieves an error message and can try again.

For each tile we define which directions the user can travel and what tiles it leads to.
We define the start and finish tiles.
Make a function that checks what tile the user is on and prints out possible travel directions.
Make a function that takes in the direction the user specifies and either moves him to the corresponding tile or tells him he can't move.

Start of the program the user gets directions and is asked for input.
A loop utilizes the functions and direction input from user until the player reaches the end goal.
"""

tile_11 = "(N)orth" 
tile_12 = "(N)orth, (E)ast, (S)outh"
tile_13 = "(E)ast, (S)outh"
tile_21 = "(N)orth"
tile_22 = "(W)est, (S)outh"
tile_23 = "(W)est, (E)ast"
tile_31 = "(N)orth"
tile_32 = "(N)orth, (S)outh"
tile_33 = "(W)est, (S)outh"

start_tile = tile_11
finish_tile = tile_31

def location():
    return location
def move():
    return move

current_location = start_tile

while current_location != finish_tile:
    location()
    direction = input("Direction: ")
    move()

print("Victory!")

