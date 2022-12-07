from collections import Counter

def isUnique(input, chars):
    return len(set(input)) == chars

entry = open(0).read()
chars = 4
for index, c in enumerate(entry):
    x = entry[index:index+chars]
    if isUnique(x, chars):
        print(index + chars)
        break