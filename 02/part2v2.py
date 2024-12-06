def is_diff_bigger_than_3(list):
    for i in range(0, len(list)-1):
        if abs(list[i] - list[i+1]) > 3:
            return True
    return False

def is_descending(list):
    for i in range(0, len(list)-1):
        if list[i] <= list[i+1]:
            return False
    return True

def is_ascending(list):
    for i in range(0, len(list)-1):
        if list[i] >= list[i+1]:
            return False
    return True


def is_safe(list):
    if is_diff_bigger_than_3(list):
        return False
    if not is_descending(list) and not is_ascending(list):
        return False
    return True


def read_file(file_path):

    with open(file_path, 'r') as file:
        all_line = []
        lines = file.readlines()
        # print(len(lines))
        for line in lines:
            split_line = line.split()
            all_line.append([int(x) for x in split_line])
        return all_line



lines= read_file('input.txt')

clear_lines = []
not_clear_lines = []


for line in lines:
    if is_safe(line):
        clear_lines.append(line)
    else:
        not_clear_lines.append(line)

print(len(clear_lines))


for line in not_clear_lines:

    for i in range(0, len(line)-1):
        line_temp = line.copy()
        line_temp.pop(i)
        if is_safe(line_temp):
            clear_lines.append(line_temp)
            break
        line_temp = line.copy()
        line_temp.pop(i+1)
        if is_safe(line_temp):
            clear_lines.append(line_temp)
            break


print(len(clear_lines))
