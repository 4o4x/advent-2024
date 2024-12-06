import re

def mul(x,y):
    return x*y


def read_file(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    return lines


lines = read_file('input.txt')


def calculate_line(line):
    find = re.findall(r'mul\(\d+,\d+\)|do\(\)|don\'t\(\)', line)

    result = 0
    flag = True
    for f in find:
        if f == 'do()':
            flag = True

        elif f == 'don\'t()':
            flag = False

        else:
            print(f + ' ' + str(flag))
            if flag:
                result = result + eval(f)


    return result

sum = 0
for line in lines:
    sum = sum + calculate_line(line)

print(sum)
