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

#GitHub = https://github.com/ingunn19/Hakuna_Matata/blob/master/tile_traveller.py


start_x = 1
start_y = 1
finish_x = 3
finish_y = 1

current_x = start_x
current_y = start_y

def paths():
    if current_x == 1 and current_y == 1:
        direction_str = "You can travel: (N)orth"
    if current_x == 1 and current_y == 2:
        direction_str = "You can travel: (N)orth or (S)outh or (E)ast"
    if current_x == 1 and current_y == 3:
        direction_str = "You can travel: (S)outh or (E)ast"
    if current_x == 2 and current_y == 1:
        direction_str = "You can travel: (N)orth"
    if current_x == 2 and current_y == 2:
        direction_str = "You can travel: (S)outh or (W)est"
    if current_x == 2 and current_y == 3:
        direction_str = "You can travel: (W)est or (E)ast"
    if current_x == 3 and current_y == 2:
        direction_str = "You can travel: (N)orth or (S)outh"
    if current_x == 3 and current_y == 3:
        direction_str = "You can travel: (S)outh or (W)est"
        
    return str(paths)


def move(direction):
    return move



while current_x != finish_x and current_y != finish_y:
    path_str = paths()
    direction = input("Direction: ")
    #move()
    print(path_str)

print("Victory!")

