for entry in open(0).read().split('\n'):
    for pairitem in entry.split(','):
        print(pairitem)