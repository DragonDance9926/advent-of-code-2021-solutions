# -*- coding: utf-8 -*-

with open("input.txt") as f:
    fish = list(map(int,f.read().split(",")))
    
day = 0

while day < 80:
    for i in range(len(fish)):
        if fish[i] == 0:
            fish[i] = 6
            fish.append(8)
        else:
            fish[i] -= 1
    day += 1

print(len(fish))


