# -*- coding: utf-8 -*-

codes = [x for x in open('input.txt').read().strip().split('\n')]
        
match = {'[':']','(':')','<':'>','{':'}'}
costs = {']':57,')':3,'}':1197,'>':25137}
start = list(match.keys())
for (k,v) in list(match.items()):
    match[v] = k

c = 0

for x in codes:
    stack = []
    for ch in x:
        if ch in start:
            stack = [ch] + stack
        else:
            if not stack:
                break
            expected = match[stack[0]]
            stack = stack[1:]
            if expected == ch:
                continue
            c += costs[ch]
            break
        
print(c)

