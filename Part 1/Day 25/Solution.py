with open('input.txt') as f:
    map = []
    for line in f:
        map.append(list(line)[:-1])

step = 0
moving = 1
w = len(map[0]) #width
h = len(map) #height
while(moving == 1):
    moving = 0
    i = 0
    moved = []
    while (i < h):
        j = 0
        while (j < w):
            if (map[i][j] == '>'):
                moved.append((i,j))
            j += 1
        i += 1


    moved2 = []
    i =0
    while (i < h):
        j = 0
        while (j < w):
            if (map[i][j] == 'v'):
                moved2.append((i, j))
            j += 1
        i += 1

    shifted = []
    for (i,j) in moved:
        if (map[i][(j+1)%w] == '.' and (i,(j+1)%w) not in shifted):
            map[i][j] = '.'
            map[i][(j+1)%w] = '>'
            moving = 1
            shifted.append((i,j))
    shifted = []
    for (i, j) in moved2:
        if (map[(i + 1)%h][j] == '.' and ((i + 1)%h,j) not in shifted):
            map[i][j] = '.'
            map[(i + 1)%h][j] = 'v'
            moving = 1
            shifted.append((i, j))
    step += 1
    print(step)






