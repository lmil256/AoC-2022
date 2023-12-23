with open('input.txt') as infile:
    highest = 0
    current = 0
    for line in infile:
        if line != '\n':
            current += int(line)
        else:
            if current > highest:
                highest = current
            current = 0
print(highest)
