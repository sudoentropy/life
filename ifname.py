# if name == if __name__ == "__main__":


# making a battleship class, don't know if will use this
# in the main program, but just using for development potential
class Battleship(object):

    @staticmethod
    def build(head, length, direction):
        body = []


    def __init__(self, coords):


# renders the stage of life

def renderStage(stageHeight, stageWidth, seed):
    ends = "+"+"-"*stageHeight+"+"
    print(ends)

    for y in range(stageHeight):
        row = []
        for x in range(stageWidth):
            if (x,y) in seed:
                cell = "@"
            else:
                cell = "."
            row.append(cell)
        print("|"+"".join(row)+"|")
    print(ends)


# main game loop
# inp takes user imput to place seeds on the grid
if __name__ == "__main__":
    seed = []

    while True:
        inp = input("Add starting blocks: ")
        xstr, ystr = inp.split(",")
        x = int(xstr)
        y = int(ystr)
        print(x+y)

        seed.append((x,y))
        renderStage(30, 30, seed)
