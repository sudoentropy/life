# if name == if __name__ == "__main__":

def renderStage(sheight, swidth, seed):
    ends = "+"+"-"*sheight+"+"
    print(ends)


    seed_set = set(seed)
    for y in range(sheight):
        row = []
        for x in range(swidth):
            if (x,y) in seed_set:
                cell = "@"
            else:
                cell = "-"
            row.append(cell)
        print("|"+"".join(row)+"|")
    print(ends)


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
