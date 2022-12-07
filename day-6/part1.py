from collections import Counter

def isUnique(input, chars):
    return len(set(input)) == chars

entry = open(0).read()
chars = 4
for index, c in enumerate(entry):
    if index >= chars:
        x = entry[(index-chars):index]
        if isUnique(x, chars):
            print(index)
            break