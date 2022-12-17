total = 0
with open('input.txt') as infile:
    for line in infile:
        pair = line.rstrip().split(',')
        r1 = pair[0].split('-') # first range
        r2 = pair[1].split('-') # second range
        r1 = [int(r1[0]), int(r1[1])]
        r2 = [int(r2[0]), int(r2[1])]
        if (r1[0] <= r2[1]) and (r1[1] >= r2[0]):
            total += 1

print(total)
