# Maze generation via randomized Prim's algorithm

from random import Random

class Cell(object):
    def __init__(self, is_wall):
        self.is_wall = is_wall
        if not is_wall:
            self.in_maze = False  # This is only looked at if it's not a wall

def generate_maze(height, width):
    # Width and height including walls:
    full_width = width*2 + 1
    full_height = height*2 + 1

    maze = [[Cell(col % 2 == 0 or row % 2 == 0)  # even-numbered row/col => wall
            for col in xrange(full_width)]
            for row in xrange(full_height)]
    wall_list = []

    random = Random()
    random.seed()

    start_col = 2*random.randint(0, width-1) + 1
    start_row = 2*random.randint(0, height-1) + 1
    maze[start_row][start_col].in_maze = True
    maze[start_row][start_col].is_wall = False

    class Wall(object):
        def __init__(self, row, col, visited_row, visited_col):
            # row, col are of the wall; visited_* are of the cell we were visiting
            # when we added this wall.
            self.row = row
            self.col = col

            # row, col of the cell on the "opposite" side, if applicable.
            if (0 < row and row < full_height-1
                    and 0 < col and col < full_width-1):
                self.opp_row = row + (row - visited_row)
                self.opp_col = col + (col - visited_col)
            else:
                self.opp_row = self.opp_col = None

    wall_list += [Wall(start_row-1, start_col, start_row, start_col),
                  Wall(start_row+1, start_col, start_row, start_col),
                  Wall(start_row, start_col-1, start_row, start_col),
                  Wall(start_row, start_col+1, start_row, start_col)]

    while len(wall_list) != 0:
        wall = random.choice(wall_list)
        wall_list.remove(wall)

        # If the wall is still a wall, and there's a cell on the opposite side,
        # and that opposite cell isn't in the maze yet...
        if (wall.opp_row is not None
                and maze[wall.row][wall.col].is_wall
                and not maze[wall.opp_row][wall.opp_col].in_maze):
            new_row = wall.opp_row
            new_col = wall.opp_col

            # ...then strike down the wall and put that opposite cell in the maze,
            maze[wall.row][wall.col].is_wall = False
            maze[new_row][new_col].in_maze = True

            # ...then add the new cell's walls to the wall list.
            for new_wall in [(new_row+1, new_col), (new_row-1, new_col),
                            (new_row, new_col+1), (new_row, new_col-1)]:
                if maze[new_wall[0]][new_wall[1]].is_wall:
                    wall_list.append(Wall(new_wall[0], new_wall[1],
                                    new_row, new_col))

    # Create an entrance (top left) and exit (bottom right).
    maze[0][1].is_wall = False
    maze[full_height-1][full_width-2].is_wall = False

    return maze
