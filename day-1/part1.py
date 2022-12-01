from itertools import groupby

entries = list(open('./day-1/input.txt','r').read().split('\n'))

elfs = [list(sub) for ele, sub in groupby(entries, key = bool) if ele]

max = 0
for elf in elfs:
    elfNumbers = [eval(i) for i in elf]
    total = sum(elfNumbers)
    if total > max:
        max = total

print(max)

