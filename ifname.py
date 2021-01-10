# if name == if __name__ == "__main__":

def renderStage(sheight, swidth, seed):
    ends = "+"+"-"*sheight+"+"
    print(ends)

    for y in range(sheight):
        print("|"+"-"*swidth+"|")
        row = []
        for x in range(swidth):
            if (x,y) in seed:
                cell = "@"
            else:
                cell = "-"
            row.append(cell)
        print("|"+"".join(row)+"|")
    print(ends)


if __name__ == "__main__":

    renderStage(10,10, [(3,1),(4,5),(8,1)])

    inp = input("Add starting blocks: ")
    xstr, ystr = inp.split(",")
    x = int(xstr)
    y = int(ystr)
    print(x+y)
