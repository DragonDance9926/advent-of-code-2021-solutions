
def enhance(i,j,mapping):
    str = ""
    if i > 0:
        if j > 0:
            if mapping[i - 1][j - 1] == '#':
                str += '1'  # lucorner
            else:
                str += '0'
        if mapping[i - 1][j] == '#':
            str += '1'  # up
        else:
            str += '0'
        if j < len(mapping[0]) - 1:
            if mapping[i - 1][j + 1] == '#':
                str += '1'  # rucorner
            else:
                str += '0'
    if j > 0:
        if mapping[i][j - 1] == '#':
            str += '1'  # left
        else:
            str += '0'

    if mapping[i][j] == '#':  # middle
        str += '1'
    else:
        str += '0'

    if j < len(mapping[0]) - 1:
        if mapping[i][j + 1] == '#':  # right
            str += '1'
        else:
            str += '0'
    if i < len(mapping) - 1:
        if j > 0:
            if mapping[i + 1][j - 1] == '#':
                str += '1'  # ldcorner
            else:
                str += '0'
        if mapping[i + 1][j] == '#':
            str += '1'  # down
        else:
            str += '0'
        if j < len(mapping[0]) - 1:
            if mapping[i + 1][j + 1] == '#':
                str += '1'  # rdcorner
            else:
                str += '0'
    return int(str,2),len(str)




with open('input.txt') as f:
    a = f.read().split('\n\n')
    decoder = a[0]
    decoder = '.'.join(decoder.split("\n"))
    image = list(a[1][:-1].split('\n'))

imagew = len(image[0])
imageh = len(image)
expand = [['.' for _ in range(imagew+100)] for _ in range(imageh+100)]


i2 = 100
i = 0
while i < imageh:
    j = 0
    j2 = 100
    while j < imagew:
        expand[i2][j2] = image[i][j]
        j += 1
        j2 += 1
    i += 1
    i2 += 1
changes = []
jlast = j2
ilast = i2
k = 0
while k < 2:
    dec = 0
    i = 0
    while i < len(expand):
        j = 0
        while j < len(expand[0]):
            new_element,l = enhance(i, j, expand)  # index
            if l == 9 :
                print(i, j, decoder[new_element], new_element)
                changes.append((i, j, decoder[new_element]))
            else:
                dec += 1
            j += 1
        i += 1
    for (i, j, replace) in changes:
        expand[i][j] = replace
    k += 1
c = 0
for line in expand:
    for x in line:
        if x == '#':
            c += 1
print(c)











