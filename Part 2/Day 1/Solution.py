# -*- coding: utf-8 -*-
lis = []
with open("input.txt") as f:
    for line in f:
        lis.append(int(line))

lis2 = []
for i in range(1,len(lis)-1):
    lis2.append([lis[i-1],lis[i],lis[i+1]])

lis3 = [sum(x) for x in lis2]

i = 1
c = 0
while i < len(lis3):
    if lis3[i-1] < lis3[i]:
        c += 1
    i += 1


print(c)
    
