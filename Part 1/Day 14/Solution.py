# -*- coding: utf-8 -*-

import re
with open("input.txt") as f:
    text = f.read()
    x = text[:-1].split("\n\n")
    letters = x[0]
    patterns = x[1]
    patterns = patterns.split("\n")

new_pattern = dict()
for match in patterns:
    match = re.split(" -> ",match)
    new_pattern[match[0]] = match[1]


for a in range(10):
    newletters = ""
    i = 1
    while i < len(letters):
        if (letters[i-1] +letters[i] in new_pattern):
            replace = letters[i-1] +new_pattern[letters[i-1] +letters[i]] +letters[i]
            if i != 1:
                newletters += replace[1:]
            else:
                newletters += replace
        i += 1
    letters = newletters
            
print(letters)
counts = set(letters)
print(max([letters.count(i) for i in letters])-min([letters.count(i) for i in letters]))

