import numpy as np

# Read the input file
with open("input4.txt", "r") as f:
    data = f.read()

l = np.empty((len(data.splitlines()), len(data.splitlines()[0])), dtype=str)
for a, line in enumerate(data.splitlines()):
    for b, char in enumerate(line):
        l[a, b] = char

## PART 1
count = 0
word = "XMAS"
word_len = len(word)
rows, cols = l.shape
count = 0

# 8 directions: right, left, down, up, diagonals
directions = [
    (0, 1),   # right
    (0, -1),  # left
    (1, 0),   # down
    (-1, 0),  # up
    (1, 1),   # down-right
    (-1, -1), # up-left
    (1, -1),  # down-left
    (-1, 1),  # up-right
]

for r in range(rows):
    for c in range(cols):
        for dr, dc in directions:
            match = True
            for k in range(word_len):
                nr, nc = r + dr*k, c + dc*k
                if not (0 <= nr < rows and 0 <= nc < cols) or l[nr, nc] != word[k]:
                    match = False
                    break
            if match:
                count += 1

print("Total XMAS occurences found:", count)

## PART 2
count = 0
patterns = [
    [(-1,-1,'M'), (-1,1,'S'), (1,-1,'M'), (1,1,'S'), (0,0,'A')],
    [(-1,-1,'S'), (-1,1,'S'), (1,-1,'M'), (1,1,'M'), (0,0,'A')],
    [(-1,-1,'M'), (-1,1,'M'), (1,-1,'S'), (1,1,'S'), (0,0,'A')],
    [(-1,-1,'S'), (-1,1,'M'), (1,-1,'S'), (1,1,'M'), (0,0,'A')]
]

for r in range(1, rows-1):
    for c in range(1, cols-1):
        for pattern in patterns:
            match = True
            for dr, dc, letter in pattern:
                nr, nc = r + dr, c + dc
                if l[nr, nc] != letter:
                    match = False
                    break
            if match:
                count += 1
                break  # stop checking other patterns for this center

print("Total X-MAS patterns found:", count)