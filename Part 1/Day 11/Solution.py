# -*- coding: utf-8 -*-


with open("input.txt") as f:
    mapping = []
    for line in f:
        x = list(map(int,line[:-1]))
        mapping.append(x)
        

c = 0

# lucorner = a[i-1][j-1] up = a[i-1][j] rucorner = a[i-1][j+1]
# left = a[i][j-1] mid = a[i][j] right = a[i][j+1] i = 1 j = 3
# ldcorner = a[i+1][j-1] down = a[i+1][j] rdcorner = a[i+1][j+1]
def flash(mapping,i,j):
    mapping[i][j] = -1
    if i < len(mapping)-1:
        if mapping[i+1][j] != -1:
            mapping[i+1][j] += 1 #down
        if mapping[i+1][j] > 9:
            flash(mapping,i+1,j)
        if j > 0 :
            if mapping[i+1][j-1] != -1:
                mapping[i+1][j-1] += 1 #ldcorner
            if mapping[i+1][j-1] > 9:
                flash(mapping,i+1,j-1)
            
        if j < len(mapping[0]) -1:
            if mapping[i+1][j+1] != -1:
                mapping[i+1][j+1] += 1 #rdcorner
            if mapping[i+1][j+1] > 9:
                flash(mapping,i+1,j+1)
            
    if i > 0:
        if mapping[i-1][j] != -1:
            mapping[i-1][j] += 1 # up
        if mapping[i-1][j] > 9:
            flash(mapping,i-1,j)
        if j > 0:
            if mapping[i-1][j-1] != -1:
                mapping[i-1][j-1] += 1 #lucorner
            if mapping[i-1][j-1] > 9:
                flash(mapping,i-1,j-1)
        if j < len(mapping[0]) -1:
            if mapping[i-1][j+1] != -1:
                mapping[i-1][j+1] += 1 #rucorner
            if mapping[i-1][j+1] > 9:
                flash(mapping,i-1,j+1)
            
    if j > 0:
        if mapping[i][j-1] != -1:
            mapping[i][j-1] += 1 #left
        if mapping[i][j-1] > 9:
            flash(mapping,i,j-1)
    if j < len(mapping[0])-1:
        if mapping[i][j+1] != -1:
            mapping[i][j+1] += 1 #right
        if mapping[i][j+1] > 9:
            flash(mapping,i,j+1)
        i = 0
    
        

step = 0

while step < 100:
    i = 0
    while i <len(mapping):
        j = 0
        while j < len(mapping[0]):
            mapping[i][j] += 1
            j += 1
        i += 1
    i = 0
    while i <len(mapping):
        j = 0
        while j < len(mapping[0]):
            if mapping[i][j] > 9:
                 flash(mapping,i,j)
            j += 1
        i += 1
    i = 0
    
    while i <len(mapping):
        j = 0
        while j < len(mapping[0]):
            if mapping[i][j] == -1:
                mapping[i][j] += 1
                c += 1
            j += 1
        i += 1
    step += 1
    
print(c)
    


    
   

