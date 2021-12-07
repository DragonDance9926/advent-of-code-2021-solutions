# -*- coding: utf-8 -*-
with open("input.txt") as f:
    crabs = list(map(int,f.read().split(",")))
lpos = max(crabs)
fuel = []
i = 0
while i < lpos:
    tot = 0
    for x in crabs:
        diff = abs(x-i)
        tot += (diff)*(diff+1) // 2
    fuel.append(tot)
    i += 1
print(min(fuel))