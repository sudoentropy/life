# experimental life simulator


# print a simple grid, commented out because for loop in line 6
# did not work, moving on to next solution

# board = [ ['-']] *3 for i in range(3) ]

# for i, line in enumerate(board):
 #    for char in line:
  #       print char,
   #  print


# next attempt at printing a grid

gridline = []
for i in range(5):
    gridline.append("")

grid = []
for i in range(5):
    grid.append(list(gridline))

print(grid)
print("\n")
print(gridline)
print("\n")


### this grid is the winner, it seems to print symmetrically without much
# muss and fuss
# above example works, but not exactly what I wanted
# but whatever, its progress, trying next example

width = int(input("width: "))
height = int(input("height: "))

grid2 = []

i = int(0)
for i in range(width):
    grid2.append("_")
for i in range(height):
    print(grid2)

