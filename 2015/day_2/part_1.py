from itertools import combinations

with open("input_t.txt") as input_file:
    data = input_file.read()

#

lines = data.split('\n')
presents = [[2*int(x)*int(y) for (x,y) in combinations(line.split('x'), 2)] for line in lines]
solution = sum([sum(areas) + min(areas)/2 for areas in presents])

#

print(f"Solution is {solution}")
