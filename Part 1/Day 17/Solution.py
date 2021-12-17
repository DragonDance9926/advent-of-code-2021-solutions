xmin = 236
xmax = 262
ymin = -78
ymax = -58

def simy(dy,ymin,ymax):
    y = 0
    pos = []
    while True:
        y += dy
        pos.append(y)
        dy -= 1
        if ymin >= y and y <= ymax:
            break
        if y < ymin:
            break
    if y < ymin:
        return -1
    else:
        return pos





for y in range(100):
    if simy(y,ymin,ymax) != -1:
        print(max(simy(y,ymin,ymax)))