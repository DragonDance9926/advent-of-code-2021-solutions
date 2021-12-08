# -*- coding: utf-8 -*-
'''
0 : 6
1 : 2
2 : 5
3 : 5
4 : 4
5 : 5
6 : 6
7 : 3
8 : 7
9 : 6
unique = 1,7,4,8
group : 2,3,5 && 6,9,0
'''

with open("input.txt") as f:
    decoder = list()
    num = list()
    for line in f:
        text = line.split(" | ")
        decoder.append(text[0])
        num.append(text[1])


def decode(pattern, value):
    known = {}
    patterns = (pattern.split())
    values= value.split()
    for p in patterns:
        if len(p) == 2:
            known[1] = set(p)
        if len(p) == 3:
            known[7] = set(p)
        if len(p) == 4:
            known[4] = set(p)
        if len(p) == 7:
            known[8] = set(p)
    for p in patterns:
        if len(p) == 6:
            if len(set(p).intersection(known[1])) == 1:
                known[6] = set(p)
            elif len(set(p).intersection(known[4])) == 4:
                known[9] = set(p)
            else:
                known[0] = set(p)
    for p in patterns:
        if len(p) == 5:
            if len(set(p).intersection(known[1])) == 2:
                known[3] = set(p)
            elif len(set(p).intersection(known[6])) == 5:
                known[5] = set(p)
            else:
                known[2] = set(p)
    # print(known)
    decoded = []
    for v in values:
        for k in known:
            if known[k] == set(v):
                decoded.append(k)
    # print(decoded)
    return decoded[0] * 1000 + decoded[1] * 100 + decoded[2] * 10 + decoded[3]
i  =0
tot = 0
while i < len(num):
    x = decode(decoder[i],num[i])
    tot += x
    i += 1


print(tot)
    