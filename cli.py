# Command line interface to generate mazes

import mazegen
import sys

width = 12
height = 10

if len(sys.argv) >= 3:
    if int(sys.argv[1]) >= 3:
        width = int(sys.argv[1])
    if int(sys.argv[2]) >= 3:
        height = int(sys.argv[2])

maze = mazegen.generate_maze(height, width)

for row in maze:
    for cell in row:
        sys.stdout.write(2*('#' if cell.is_wall else ' '))
    sys.stdout.write('\n')
