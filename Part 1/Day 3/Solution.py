# -*- coding: utf-8 -*-

with open("input.txt") as f:
    n = []
    for line in f:
        n.append(line)


result = []
i = 0
j = 0
while j < 12:
    zero = 0
    one = 0
    while i < len(n):
        if n[i][j] == '0':
            zero += 1
        else:
            one += 1
        i += 1
    result.append([zero,one])
    i = 0
    j += 1
print(result)

epsilon = '' #min
gamma = '' #max
for x in result:
    gamma += str(x.index(max(x)))
    epsilon += str(x.index(min(x)))
    
print(int(gamma,2)*int(epsilon,2))
