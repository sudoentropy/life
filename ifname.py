# if name == if __name__ == "__main__":


def renderStage(sheight, swidth):
    ends = ("+"+"-"*sheight+"+")
    print(ends)

    for i in range(sheight):
        print("|"+"-"*swidth+"|")

    print(ends)


if __name__ == "__main__":

    renderStage(10,10)

    inp = input("Add starting blocks: ")
    xstr, ystr = inp.split(",")
    x = int(xstr)
    y = int(ystr)
    print(x+y)
