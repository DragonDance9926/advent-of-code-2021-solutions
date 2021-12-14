# -*- coding: utf-8 -*-

from collections import defaultdict

with open("input.txt") as f:
    lines = f.read().splitlines()

    rules = dict()
    template, _, *inRules = lines
    for r in inRules:
        a, b = r.split(" -> ")
        rules[a] = b

    pairCounter, elementCounter = defaultdict(int), defaultdict(int)

    # read pairs from template
    for a, b in zip(template, template[1:]):
        pairCounter[a+b] += 1
    for c in template:
        elementCounter[c] += 1
    steps = 40

    for i in range(steps):

        for (a, b), v in pairCounter.copy().items():
            newElement = rules[a+b]
            elementCounter[newElement] += v
            # create new pairs
            pairCounter[a + newElement] += v
            pairCounter[newElement + b] += v
            pairCounter[a+b] -= v



print(max(elementCounter.values()) - min(elementCounter.values()))


