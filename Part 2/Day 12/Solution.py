# -*- coding: utf-8 -*-
from collections import defaultdict
path = defaultdict(list)

for line in open("input.txt"):
    a, b = line.strip().split('-')
    path[a] += [b]
    path[b] += [a]

def search(part, seen=set(), cave='start'):
    if cave == 'end': return 1
    if cave in seen:
        if cave == 'start': return 0
        if cave.islower():
            if part == 1: return 0
            else: part = 1

    return sum(search(part, seen|{cave}, n)
                 for n in path[cave])

print(search(part=2))