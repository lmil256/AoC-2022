class Directory():
    def __init__(self, parent):
        # Parent directory
        self.parent = parent
        # Dict of subdirectories
        self.directories = {}
        # Dict of files
        self.files = {}
        self.size = 0

    def cd(self, name):
        self.calc_size()
        try:
            return self.directories[name]
        except KeyError:
            if name == '/':
                return self if self.parent == None else self.parent.cd(name)
            if name == '..':
                return self.parent

    def calc_size(self):
        self.size = 0
        for dirname in self.directories:
            self.size += self.directories[dirname].size
        for filename in self.files:
            self.size += self.files[filename]

def main():
    pwd = Directory(None)
    numlines = 0
    with open('input.txt') as infile:
        line = infile.readline()
        numlines += 1
        while line != '':
            tokens = line.rstrip().split(' ')
            # Parse command
            if tokens[0] == '$':
                if tokens[1] == 'cd':
                    pwd = pwd.cd(tokens[2])
            # Parse directory
            elif tokens[0] == 'dir':
                pwd.directories[tokens[1]] = Directory(pwd)
            # Parse file
            elif tokens[0].isnumeric():
                pwd.files[tokens[1]] = int(tokens[0])
            else:
                raise Exception(f"Could not parse line {numlines}")
            line = infile.readline()
    pwd = pwd.cd('/')

    TARGET = pwd.size - 40000000
    smallest = pwd.size
    stack = [pwd]
    while len(stack) > 0:
        curr = stack.pop()
        if curr.size <= smallest:
            smallest = curr.size
        for dirname in curr.directories:
            if curr.directories[dirname].size >= TARGET:
                stack.append(curr.directories[dirname])

    print(smallest)

main()
