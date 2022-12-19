import sys
target = int(sys.argv[1])
with open('input.txt') as infile:
    seq = ''
    numread = 0
    while len(seq) < target:
        # Read a character
        seq += infile.read(1)
        numread += 1
        # Search for the last character earlier in the sequence
        if (p := seq.find(seq[-1], 0, -1)) != -1:
            # If found, truncate the sequence past the match
            seq = seq[p+1:]

print(numread)
