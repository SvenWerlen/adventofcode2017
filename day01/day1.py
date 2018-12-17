## Usage python day1.py input

import sys
from sets import Set

FILE = sys.argv[1]

puzzle = None
with open(FILE) as f:
    for line in f:
        puzzle = line[:-1]

print "Puzzle input is:"
print puzzle

total = 0
for idx in range(len(puzzle)):
    if puzzle[idx] == puzzle[(idx+1)%len(puzzle)]:
        total += int(puzzle[idx])

print "Puzzle result is %s" % total


## Part 2

total = 0
half = int(round(len(puzzle)/2))
for idx in range(len(puzzle)):
    if puzzle[idx] == puzzle[(idx+half)%len(puzzle)]:
        total += int(puzzle[idx])
        
print "Puzzle result (2nd part) is %s" % total
