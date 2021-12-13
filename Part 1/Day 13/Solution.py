# -*- coding: utf-8 -*-
import numpy as np
with open("input.txt") as f:
    a = f.read().split("\n\n")
    coordinates = a[0]
    coordinates = coordinates.split("\n")
    folds = a[1]
    folds = folds.split("\n")
    
dots = np.zeros((2000,2000),dtype=int)

for s in coordinates:
    a = s.split(",")
    i = int(a[0])
    j = int(a[1])
    dots[j][i] = 1

fold = folds[0]

fold = fold.split()
folding = fold[-1]
folding = folding.split("=")
coor = int(folding[-1])
axis = folding[0]
if axis == 'x': #j ()
    x = coor
    for s in coordinates:
        a = s.split(",")
        i = int(a[0])
        j = int(a[1])
        if (dots[j][i] == 1 or dots[j][2*x-i] == 1)  and i > x:
            dots[j][2*x-i] = 1
            dots[j][i] = 0
elif axis == 'y': #i
    y = coor
    for s in coordinates:
        a = s.split(",")
        i = int(a[0])
        j = int(a[1])
        if (dots[j][i] == 1 or dots[2*y-j][i] == 1) and j > y:
            dots[2*y-j][i] = 1
            dots[j][i] = 0
            

print(np.count_nonzero(dots))           
