# -*- coding: utf-8 -*-

with open("input.txt") as f:
    fish = list(map(int,f.read().split(",")))
    fishes = [0]*9
    for f in fish:
        fishes[f] += 1
        
        

for i in range(256):
    six = fishes.pop(0)
    fishes[6] += six
    fishes.append(six)
    
print(sum(fishes))