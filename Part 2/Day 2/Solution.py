with open("input.txt") as f:
    x = 0
    y = 0
    a = 0
    for lin in f:
        line = lin.split()
        if line[0] == "forward":
            x += int(line[-1])
            y += (int(line[-1])*a)
        elif line[0] == "up":
            a -= int(line[-1])
        elif line[0] == "down":
            a += int(line[-1])


print(y*x)


