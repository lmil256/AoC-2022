def priority(item_type):
    if item_type.islower():
        return 1 + ord(item_type) - ord('a')
    else:
        return 27 + ord(item_type) - ord('A')

total = 0
with open('input.txt') as infile:
    while True:
        line1 = infile.readline().rstrip()
        line2 = infile.readline().rstrip()
        line3 = infile.readline().rstrip()
        if line1 == '' or line2 == '' or line3 == '':
            break
        total += priority((set(line1) & set(line2) & set(line3)).pop()) # :^)

print(total)
