def getPoints(round):
    if round == 'A X':
        return 3 + 0
    if round == 'A Y':
        return 1 + 3
    if round == 'A Z':
        return 2 + 6
    if round == 'B X':
        return 1 + 0
    if round == 'B Y':
        return 2 + 3
    if round == 'B Z':
        return 3 + 6
    if round == 'C X':
        return 2 + 0
    if round == 'C Y':
        return 3 + 3
    if round == 'C Z':
        return 1 + 6

#A X = Rock
#B Y = Paper
#C Z = Scissors

entries = list(open('./day-2/input.txt','r').read().split('\n'))

points = 0
for entry in entries:
    points += getPoints(entry)

print(points)
