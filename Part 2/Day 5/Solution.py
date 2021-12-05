# -*- coding: utf-8 -*-
"""
Created on Sun Dec  5 09:35:45 2021

@author: Casper
"""
import re
with open("input.txt") as f:
    c1 = []
    c2 = []
    for line in f:
        x = re.split(' -> ',line)
        c1.append(x[0])
        c2.append(x[1])
vent = [[0 for x in range(1000)] for y in range(1000)] 
        

i = 0
c = 0
while i < len(c1):
    a = c1[i].split(",")
    b = c2[i].split(",")
    x1 = int(a[0])
    x2 = int(b[0])
    y1 = int(a[1])
    y2 = int(b[1])
    if x1 == x2:
        ymin = min(y1,y2)
        ymax = max(y1,y2)
        while (ymin <= ymax):
            vent[x1][ymin] += 1
            ymin += 1
    elif y1 == y2:
        xmin = min(x1,x2)
        xmax = max(x1,x2)
        while xmin <= xmax:
            vent[xmin][y1] += 1
            xmin += 1
    elif ((y2-y1) // (x1-x2) == -1) or ((y2-y1) // (x1-x2) == 1):
        while x1 != x2 and y1 != y2:
            vent[x1][y1] += 1
            if x1 < x2:
                x1 += 1
            else:
                x1 -= 1
            if y1 < y2:
                y1 += 1
            else:
                y1 -= 1
        vent[x1][y1] += 1
    i += 1

for i in range(1000):
    for j in range(1000):
        if vent[i][j] > 1:
            c+= 1
        
print(c)