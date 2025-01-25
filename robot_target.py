#Given a rebote on surface, write program to move the robote to target location
#Moving a robot on a surface to a target location. We'll define the surface as a 2D grid and assume the robot has simple movement commands like "up", "down", "left", and "right".
# The robot starts at an initial position (x, y) on the grid.
# The target location is specified as (target_x, target_y).
# The robot needs to determine the shortest path (using simple movements) to reach the target.

def move_robot(start_x, start_y, target_x, target_y):
    x, y = start_x, start_y
    moves = [] ## To store the sequence of moves.
    ##At any given position, robot can move either up, down for Y axis move, left and write for X axis move.
    while(y<target_y):
        moves.append("UP")
        y +=1

    while(y>target_y):
        moves.append("Down")
        y -=1

    while(x<target_x):
        moves.append("Right")
        x += 1

    while(x>target_x):
        moves.append("Left")
        x -= 1

    # Print the moves
    print(f"Moves to reach ({target_x}, {target_y}) from ({start_x}, {start_y}):")
    print(" -> ".join(moves))

move_robot(2, 3, 5, 1)

