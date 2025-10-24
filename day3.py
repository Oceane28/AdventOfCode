import re

# Read the input file
with open("input3.txt", "r") as f:
    data = f.read()

## PART 1
pattern = r"mul\((\d{1,5}),(\d{1,5})\)"
matches = re.findall(pattern, data)

total = sum(int(x) * int(y) for x, y in matches)

print("Total sum of all mul:", total)

## PART 2
mul_pattern = re.compile(r"mul\((\d{1,5}),(\d{1,5})\)")
pattern = r"mul\(\d{1,5},\d{1,5}\)|do\(\)|don't\(\)"
tokens = re.findall(pattern, data)

enabled = True
total = 0

for token in tokens:
    if token == "do()":
        enabled = True
    elif token == "don't()":
        enabled = False
    else:
        m = mul_pattern.match(token)
        if m and enabled:
            x, y = map(int, m.groups())
            total += x * y

print("Total sum of enabled mul:", total)