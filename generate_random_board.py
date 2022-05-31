# Run this and copy the lines into the html file

from random import randint

mines = set()
i = 0
while len(mines) < 10:
    mines.add((randint(1, 9), randint(1, 9)))
for i in range(1, 10):
    for j in range(1, 10):
        if (i, j) in mines:
            print("cell({}, {}, {}, u)".format(i, j, "mine"))
        else:
            print("cell({}, {}, {}, u)".format(i, j, "b"))
