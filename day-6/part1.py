from collections import Counter

def hasDuplicates(input):
    wc = Counter(input)

    for letter, count in wc.items():
        if (count > 1):
            return True
    return False

entry = open(0).read()
chars = 4
for index, c in enumerate(entry):
    if index >= chars:
        x = entry[(index-chars):index]
        if not hasDuplicates(x):
            print(index)
            break