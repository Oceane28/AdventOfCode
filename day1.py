# Read the input file
with open("input1.txt", "r") as f:
    lines = f.readlines()

# Split each line into left and right numbers
left = []
right = []
for line in lines:
    l, r = line.split()
    left.append(int(l))
    right.append(int(r))

left.sort()
right.sort()

## PART 1
total_distance = sum(abs(l - r) for l, r in zip(left, right))

print("Total distance:", total_distance)


## PART 2
from collections import Counter
right_counter = Counter(right)

similarity_score = sum(l * right_counter[l] for l in left)
print("Similarity score:", similarity_score)