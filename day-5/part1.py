import math
import re

def getStacks(lines):
    stack = []

    n = 4
    cols = len([lines[0][i:i+n] for i in range(0, len(lines[0]), n)])

    for o in range(0, cols):
        stack.append([])

    for line in lines:
        if line == '':
            break

        chunks = [line[i:i+n] for i in range(0, len(line), n)]

        for index, chunk in enumerate(chunks):
            k = re.search(r'[A-Z]', chunk)
            if k:
                stack[index].append(k.group())
                
    return stack

lines = open(0).read().split('\n')
stacks = getStacks(lines)

print(stacks)

movesstr = lines[lines.index('')+1:]

for movestr in movesstr:
    moves = [int(subitem) for subitem in movestr.split() if subitem.isdigit()]
    amount = moves[0]
    f = moves[1]
    t = moves[2]
    
    fromStack = stacks[f-1]
    toStack = stacks[t-1]
    
    toMove = fromStack[:amount]
    toMove.reverse()

    stacks[f-1] = fromStack[amount:]
    stacks[t-1] = toMove + toStack

t = ''    
for stack in stacks:
    if len(stack) > 0:
        t += stack[0]

print(t)