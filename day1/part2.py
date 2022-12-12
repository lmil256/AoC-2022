with open('input.txt') as infile:
    top3 = [0, 0, 0]
    current = 0
    for line in infile:
        if line != '\n':
            current += int(line)
        else:
            for i in range(3):
                if current > top3[i]:
                    top3.insert(i, current)
                    top3.pop()
                    break
            current = 0
print(sum(top3))
