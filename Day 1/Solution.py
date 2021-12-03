# -*- coding: utf-8 -*-
lis = []
with open("input.txt") as f:
    for line in f:
        lis.append(line)
i = 0
c = 0
while i < len(lis)-1:
    if lis[i] < lis[i+1]:
        c += 1
    i += 1
if lis[-2] < lis[-1]:
    c += 1


print(c)
    
