def isInRange(range1, range2):
    return range1[0] in range2 and range1[-1] in range2

t = 0

for entry in open(0).read().split('\n'):
    pairs = entry.split(',')
    pa = pairs[0].split('-')
    pb = pairs[1].split('-')

    p1 = range(int(pa[0]), int(pa[1]) + 1)
    p2 = range(int(pb[0]), int(pb[1]) + 1)

    if isInRange(p1, p2):
        t += 1
    elif isInRange(p2, p1):
        t += 1
    
print(t)