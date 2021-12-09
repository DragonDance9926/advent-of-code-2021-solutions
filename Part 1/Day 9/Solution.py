# -*- coding: utf-8 -*-

with open("input.txt") as f:
    mapping = []
    for line in f:
        mapping.append(line[:-1])
c = 0
i = 0
while i < len(mapping):
    j = 0
    while j < len(mapping[0]):
        if i < len(mapping)-1:
            down = int(mapping[i+1][j])
        else:
            down = int(mapping[i][j])+1
        if i > 0:
            up = int(mapping[i-1][j])
        else:
            up = int(mapping[i][j])+1
        num = int(mapping[i][j])
        if j > 0:
            left = int(mapping[i][j-1])
        else:
            left = int(mapping[i][j])+1
            
        if j < (len(mapping[0])-1):
            right = int(mapping[i][j+1])
        else:
            right = int(mapping[i][j])+1
        if num < left and num < right and num < up and num < down:
            c += num+1
        j += 1
    i += 1
print(c)
        
            
