import re

def mul(x,y):
    return x*y


def read_file(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    return lines


lines = read_file('input.txt')


def calculate_line(line):
    find = re.findall(r'mul\(\d+,\d+\)', line)

    s = 0
    for f in find:
        s = s + eval(f)
    return s

sum = 0
for line in lines:
    sum = sum + calculate_line(line)

print(sum)
