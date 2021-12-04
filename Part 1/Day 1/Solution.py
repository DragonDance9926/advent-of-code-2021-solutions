# -*- coding: utf-8 -*-
lis = []
with open("input.txt") as f:
    for line in f:
        lis.append(line)
i = 1
c = 0
while i < len(lis):
    if lis[i-1] < lis[i]:
        c += 1
    i += 1

print(c)
    
