p1 = 9
p2 = 6

p1point = 0
p2point = 0
die = 1
roll = 0
while (p1point < 1000 and p2point < 1000 ):
    tot = 0
    for i in range(3):
        tot += die
        die += 1
        roll += 1
        if die == 101:
            die = 1
    p1 = (p1 + tot)%10
    if p1 == 0:
        p1point += 10
    else:
        p1point += p1

    if p1point >= 1000:
        break
    tot2 = 0
    for i in range(3):
        tot2 += die
        die += 1
        roll += 1
        if die == 101:
            die = 1
    p2 = (p2 + tot2) % 10
    if p2 == 0:
        p2point += 10
    else:
        p2point += p2
    if p2point >= 1000:
        break



if p1point < 1000:
    print(p1point*roll)
else:
    print(p2point*roll)