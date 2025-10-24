# Read the input file
with open("input2.txt", "r") as f:
    lines = f.readlines()

# Split each line into left and right numbers
lns = []
for line in lines:
    l = line.split()
    for i in range(len(l)):
        l[i] = int(l[i])
    lns.append(l)

def is_safe(report):
    x = 0
    for i in range(len(report)-1):
        d = report[i+1] - report[i]
        if abs(d) < 1 or abs(d) > 3:
            return False
        if x == 0:
            x = d / abs(d)
        elif x * d < 0:
            return False
    return True

## PART 1
count_sure = 0
count_nsure = 0
for line in lns:
    if is_safe(line):
        count_sure += 1
    else:
        count_nsure += 1
    
print("Sure:", count_sure)
print("Not sure:", count_nsure)


## PART 2
safe_count = 0
for line in lns:
    if is_safe(line):
        safe_count += 1
    else:
        for i in range(len(line)):
            temp = line[:i] + line[i+1:]
            if is_safe(temp):
                safe_count += 1
                break

print("Safe reports:", safe_count)