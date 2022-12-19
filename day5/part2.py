import re
LETTER_DISTANCE = 4
with open('input.txt') as infile:
    # Read the crate diagram
    lines = []
    line = infile.readline().rstrip()
    while line != '':
        lines.insert(0, line)
        line = infile.readline().rstrip()
    num_stacks = int(lines[0].split(' ')[-1])
    stacks = [[] for i in range(num_stacks)]
    # Read the crate letters into the stacks
    for line in lines[1:]:
        for i in range(1, len(line), LETTER_DISTANCE):
            if line[i] != ' ':
                stacks[i//LETTER_DISTANCE].append(line[i])
    # Parse the movement instructions
    for line in infile:
        digits = [int(x) for x in re.findall(r'\d+', line)]
        num_crates = digits[0]
        source_stack = stacks[digits[1] - 1]
        dest_stack = stacks[digits[2] - 1]
        dest_stack += source_stack[-num_crates:]
        del source_stack[-num_crates:]
        
for stack in stacks:
    print(stack[-1], end='')
