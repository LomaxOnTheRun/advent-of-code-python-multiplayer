import math


with open("input_t.txt") as input_file:
    data = input_file.read()

#

total_length = 0
for line in data.split('\n'):
    sides = [int(side) for side in line.split("x")]
    body = sum(sorted(sides)[:2]) * 2
    bow = math.prod(sides)
    total_length += body + bow

#

print(f"Solution is {total_length}")
