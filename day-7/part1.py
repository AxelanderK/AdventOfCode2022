entries = open(0).read().split('\n')

fs = []
steps = {}
curDir = ''

for entry in entries:
    if '$ cd' in entry:
        parameter = entry.replace('$ cd ', '')
        if parameter != '..':
            # steps[parameter] = []
            fs.pop()
            curDir = parameter
        else:
            fs.append(parameter)
    elif 'dir ' in entry:
        parameter = entry.replace('dir ', '')
        # steps[curDir].append(parameter)
    else:
        print(entry)
        
    print(curDir)
    

print(steps)
        