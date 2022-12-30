class Vector():
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
    def __add__(self, vec):
        return Vector(self.x + vec.x, self.y + vec.y)
    def __sub__(self, vec):
        return Vector(self.x - vec.x, self.y - vec.y)
    def __eq__(self, vec):
        return self.x == vec.x and self.y == vec.y
    def __hash__(self):
        return hash((self.x, self.y))
    def __str__(self):
        return f'x: {self.x} y: {self.y}'
    def __repr__(self):
        return str(self)

def main():
    knots = [Vector() for _ in range(10)]
    unitvecs = {\
        'R': Vector(1, 0),
        'U': Vector(0, 1),
        'L': Vector(-1, 0),
        'D': Vector(0, -1)
        }
    visited = {knots[0]: True}
    with open('input.txt') as infile:
        for line in infile:
            direction, num = line.rstrip().split(' ')
            for _ in range(int(num)):
                knots[0] += unitvecs[direction]
                for i in range(1, len(knots)):
                    move = knots[i - 1] - knots[i]
                    if abs(move.x) <= 1 and abs(move.y) <= 1:
                        break
                    if abs(move.x) > 1:
                        move.x //= 2
                    if abs(move.y) > 1:
                        move.y //= 2
                    knots[i] += move

                if knots[-1] not in visited:
                    visited[knots[-1]] = True
                    
    print(len(visited))

# Thing I wrote for debugging
def draw(knots):
    xmin = xmax = knots[0].x
    ymin = ymax = knots[0].y
    for knot in knots[1:]:
        if knot.x < xmin: xmin = knot.x
        elif knot.x > xmax: xmax = knot.x
        if knot.y < ymin: ymin = knot.y
        elif knot.y > ymax: ymax = knot.y
    grid = [[' '] * (xmax - xmin + 1) for _ in range(ymax - ymin + 1)]
    for num, knot in enumerate(reversed(knots)):
        grid[knot.y - ymin][knot.x - xmin] = str(num)
    for line in reversed(grid):
        print(''.join(line))

main()
