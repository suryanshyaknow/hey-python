"""
You will program a simple cleaning bot to perform the correct actions based on environmental input.
The bot here is positioned at the top left corner of a 5*5 grid. Your task is to move the bot to clean all the 
dirty cells.

############################### Input Format ####################################
The first line contains two space separated integers which indicate the current position of the bot.
5 lines follow representing the grid. Each cell in the grid is represented by any of the following 3 characters: 
'b' (ascii value 98) indicates the bot's current position, 'd' (ascii value 100) indicates a dirty cell and '-' 
(ascii value 45) indicates a clean cell in the grid.

Note If the bot is on a dirty cell, the cell will still have 'd' on it.

############################### Output Format ###################################
The output is the action that is taken by the bot in the current step, and it can be either one of the movements 
in 4 directions or cleaning up the cell in which it is currently located. The valid output strings are 
LEFT, RIGHT, UP and DOWN or CLEAN. 
If the bot ever reaches a dirty cell, output CLEAN to clean the dirty cell. Repeat this process until all the 
cells on the grid are cleaned.
"""

# A function to print out the current state of the grid
def print_grid(grid):
    try:
        for row in grid:
            print(row)
    except Exception as e:
        raise e
    
# A function to determine the current pos of the bot
def find_current_pos(grid):
    try:
        for row in range(len(grid)):
            for col in range(len(grid[row])):
                if grid[row][col] == 'b':
                    return (row, col)
    except Exception as e:
        raise e 

# A function to determine the next move of the bot
def next_move(posr, posc, grid):
    try:
        # if the current cell is dusty, CLEAN it
        if grid[posr][posc] == "d":
            # grid[posr][posc] = "C"  # "C" here stands for "Cleaned"
            return "CLEAN"
        
        # Gather co-ordinates of all dirty cells
        dirty_cells = [(row, col) for row in range(len(grid)) for col in range(len(grid[row])) if grid[row][col]=='d']

        # Find the nearest dirty cell
        # Decide in terms of Manhattan distance from the current pos to the nearest dirty cell
        nearest_dirty_cell = min(dirty_cells, key=lambda x: abs(x[0]-posr) + abs(x[1]-posc))

        if nearest_dirty_cell[0] > posr:
            return "DOWN"
        elif nearest_dirty_cell[0] < posr:
            return "UP"
        elif nearest_dirty_cell[1] > posc:
            return "RIGHT"
        else:
            return "LEFT"
        ...
    except Exception as e:
        raise e

# Current pos of the bot
grid = [
    ['-', 'd', '-', '-', '-'],
    ['-', 'b', '-', '-', '-'],
    ['-', '-', '-', 'd', '-'],
    ['-', '-', '-', '-', '-'],
    ['-', '-', '-', '-', 'd']
]
posr, posc = find_current_pos(grid)

# Clean the Grid
while 'd' in ''.join([ele for row in grid for ele in row]):
    print_grid(grid)
    action = next_move(posr, posc, grid)
    print("Bot Action: ", action)

    # Update bot pos in regard to the action taken
    if action == "RIGHT":
        posc += 1
    elif action == "LEFT":
        posc -= 1
    elif action == "UP":
        posr -= 1
    elif action == "DOWN":
        posr += 1
    else:
        grid[posr][posc] = "C"
        # pass

print_grid(grid)
print("GRID CLEANED!")