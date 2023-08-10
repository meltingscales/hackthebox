with open('numbers.md', 'r') as f:
    for line in f.readlines():
        print(line)

        split = line.split(' ')

        for decimal in split:
            character = chr(int(decimal))
            print(character, sep='', end='')
