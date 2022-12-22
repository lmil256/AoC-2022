N = 99
def main():
    table = []
    with open('input.txt') as infile:
        line = infile.readline()
        while line != '':
            table.append([int(x) for x in line.rstrip()])
            line = infile.readline()

    highest = 0

    for ypos in range(N):
        for xpos in range(N):
            score = get_score(ypos, xpos, table)
            if score >= highest:
                highest = score
    print(highest)

def get_score(ypos, xpos, table):
    curr = table[ypos][xpos]
    scores = [0] * 4
    for xscan in range(xpos + 1, N):
        scores[0] += 1
        if table[ypos][xscan] >= curr:
            break
    for xscan in range(xpos - 1, -1, -1):
        scores[1] += 1
        if table[ypos][xscan] >= curr:
            break
    for yscan in range(ypos + 1, N):
        scores[2] += 1
        if table[yscan][xpos] >= curr:
            break
    for yscan in range(ypos - 1, -1, -1):
        scores[3] += 1
        if table[yscan][xpos] >= curr:
            break

    return scores[0] * scores[1] * scores[2] * scores[3]

main()
