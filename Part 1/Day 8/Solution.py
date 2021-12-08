# -*- coding: utf-8 -*-

with open("input.txt") as f:
    decoder = list()
    num = list()
    for line in f:
        text = line.split(" | ")
        decoder.append(text[0])
        num.append(text[1])



c = 0 
for y in num:
    a = y.split()
    for x in a:
        if len(x) == 2 or len(x) == 3 or len(x) == 4 or len(x) == 7:
            c += 1

print(c)
        
        
        
        
    



