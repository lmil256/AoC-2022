total = 0
with open('input.txt') as infile:
    for line in infile:
        pair = line.rstrip().split(',')
        r1 = [int(x) for x in pair[0].split('-')] # first range
        r2 = [int(x) for x in pair[1].split('-')] # second range
        if (r1[0] <= r2[1]) and (r1[1] >= r2[0]):
            total += 1

print(total)
