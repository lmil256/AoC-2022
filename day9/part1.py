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
    def copy(self):
        return Vector(self.x, self.y)
        

def main():
    head = Vector()
    tail = Vector()
    unitvecs = {\
        'R': Vector(1, 0),
        'U': Vector(0, 1),
        'L': Vector(-1, 0),
        'D': Vector(0, -1)
        }
    visited = {tail: True}
    with open('input.txt') as infile:
        for line in infile:
            direction, num = line.rstrip().split(' ')
            for _ in range(int(num)):
                prevhead = head.copy()
                head += unitvecs[direction]
                diff = head - tail
                if abs(diff.x) > 1 or abs(diff.y) > 1:
                    tail = prevhead
                    if tail not in visited:
                        visited[tail] = True

    print(len(visited))

main()
