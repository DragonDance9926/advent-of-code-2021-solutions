# -*- coding: utf-8 -*-


with open("input.txt") as f:
    x = 0
    y = 0
    for lin in f:
        line = lin.split()
        if line[0] == "forward":
            x += int(line[-1])
        elif line[0] == "up":
            y -= int(line[-1])
        elif line[0] == "down":
            y += int(line[-1])


print(x*y)


