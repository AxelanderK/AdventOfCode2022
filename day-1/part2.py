from itertools import groupby

entries = list(open('./day-1/input.txt','r').read().split('\n'))

print(str(groupby(entries, key = bool)))

elfs = [list(sub) for ele, sub in groupby(entries, key = bool) if ele]

elfSum = []
for elf in elfs:
    elfNumbers = [eval(i) for i in elf]
    elfSum.append(sum(elfNumbers))

elfSum.sort(reverse=True)
print(sum(elfSum[:3]))

