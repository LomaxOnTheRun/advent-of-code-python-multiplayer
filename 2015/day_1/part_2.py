with open("input_l.txt") as input_file:
    data = input_file.read()


position = 0
floor = 0
while floor != -1:
    character = data[position]

    if character == "(":
        floor += 1
    elif character == ")":
        floor -= 1

    position += 1

solution = position

# 

print(f"Solution is {solution}")
