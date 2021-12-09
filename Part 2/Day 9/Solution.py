# -*- coding: utf-8 -*-

from collections import Counter
mapping = [[int(y) for y in x] for x in open('input.txt').read().strip().split('\n')]

def basin (i,j):
    downhill = None
    for (di,dj) in [(i-1,j), (i+1,j), (i,j-1), (i,j+1)]:
        if di in range(len(mapping)) and dj in range(len(mapping)):
            if mapping[i][j] > mapping[di][dj]:
                downhill = (di, dj)
    if downhill is None:
        return (i,j)
    ret = basin(*downhill)
    return ret

basins = []

for i in range(len(mapping)):
	for j in range(len(mapping[0])):
		if mapping[i][j] != 9:
			basins.append(basin(i, j))
            
ret = 1
for basin, common in Counter(basins).most_common(3):
	ret *= common
print(ret)