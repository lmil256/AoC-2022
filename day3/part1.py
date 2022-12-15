def priority(item_type):
    if item_type.islower():
        return 1 + ord(item_type) - ord('a')
    else:
        return 27 + ord(item_type) - ord('A')

total = 0
with open('input.txt') as infile:
    for line in infile:
        comp1 = set(line[0:len(line) // 2])
        comp2 = set(line[len(line) // 2:])
        for item in comp1 & comp2:
            total += priority(item)

print(total)
