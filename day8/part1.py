N = 99
def main():
    table = []
    with open('input.txt') as infile:
        line = infile.readline()
        while line != '':
            table.append([int(x) for x in line.rstrip()])
            line = infile.readline()

    count = 0

    for ypos in range(N):
        for xpos in range(N):
            if visible(ypos, xpos, table):
                count += 1
    print(count)

def visible(ypos, xpos, table):
    return left_visible(ypos, xpos, table)\
            or right_visible(ypos, xpos, table)\
            or top_visible(ypos, xpos, table)\
            or bottom_visible(ypos, xpos, table)

def left_visible(ypos, xpos, table):
    for xscan in range(xpos):
        if table[ypos][xscan] >= table[ypos][xpos]:
            return False
    return True

def right_visible(ypos, xpos, table):
    for xscan in range(N - 1, xpos, -1):
        if table[ypos][xscan] >= table[ypos][xpos]:
            return False
    return True

def top_visible(ypos, xpos, table):
    for yscan in range(ypos):
        if table[yscan][xpos] >= table[ypos][xpos]:
            return False
    return True

def bottom_visible(ypos, xpos, table):
    for yscan in range(N - 1, ypos, -1):
        if table[yscan][xpos] >= table[ypos][xpos]:
            return False
    return True

main()
