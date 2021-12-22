
import re
with open("input.txt") as f:
    commands = list(f.read()[:-1].split('\n'))

coordinate = set()


for line in commands:
    m = re.search(r'(on|off) x=(-?\d+)..(-?\d+),y=(-?\d+)..(-?\d+),z=(-?\d+)..(-?\d+)', line)
    x0, x1, y0, y1, z0, z1 = [int(m.group(i)) for i in range(2, 8)]
    command = m.group(1)
    if (x0 >= -50 and x1 <= 50) and (y0 >= -50 and y1 <= 50) and (z0 >= -50 and z1 <= 50):
        if command == "on":
            for x in range(x0, x1+1):
                for y in range(y0, y1+1):
                    for z in range(z0, z1+1):
                        coordinate.add((x, y, z))
        else:
            for x in range(x0, x1+1):
                for y in range(y0, y1+1):
                    for z in range(z0, z1+1):
                        if (x,y,z) in coordinate:
                            coordinate.remove((x,y,z))


print(len(coordinate))


