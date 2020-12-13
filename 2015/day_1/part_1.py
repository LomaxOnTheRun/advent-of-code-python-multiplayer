import re


with open("input_l.txt") as input_file:
    data = input_file.read()

up = data.count("(")
down = data.count(")")

solution = up - down

print(f"Solution is {solution}")
