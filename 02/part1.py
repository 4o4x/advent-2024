def is_safe(list):
    flag = 0
    for i in range(0, len(list)-1):
        if list[i] == list[i+1]:
            return False

        if list[i] > list[i+1]:
            if flag == 1:
                return False
            flag = -1

        if list[i] < list[i+1]:
            if flag == -1:
                return False
            flag = 1

        if abs(list[i] - list[i+1]) > 3:
            return False
    return True


def read_file(file_path):
    with open(file_path, 'r') as file:
        safe = 0
        lines = file.readlines()
        for line in lines:
            split_line = line.split()
            if is_safe([int(x) for x in split_line]):
                safe += 1
    return safe


print(read_file('input.txt'))
