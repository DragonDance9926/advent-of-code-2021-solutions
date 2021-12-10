# -*- coding: utf-8 -*-



# -*- coding: utf-8 -*-

codes = [x for x in open('input.txt').read().strip().split('\n')]
        
match = {'[':']','(':')','<':'>','{':'}'}
costs = {']':2,')':1,'}':3,'>':4}
start = list(match.keys())
for (k,v) in list(match.items()):
    match[v] = k

c = []

for x in codes:
    stack = []
    fail = False 
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
            fail = True
            break
    if not fail:
        x = 0
        for ch in stack:
            x = x*5 + costs[match[ch]]
        c += [x]
c.sort()
print(c[len(c)//2])

