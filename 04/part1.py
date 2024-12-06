def read_file(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
        return [list(line)[:-1] for line in lines]


matrix = read_file('input.txt')

word = ['X', 'M', 'A', 'S']

def right(matrix, i, j):
    for k in range(len(word)):
        if j+k >= len(matrix[i]) or matrix[i][j+k] != word[k]:
            return False
    return True

def left(matrix, i, j):
    for k in range(len(word)):
        if j-k < 0 or matrix[i][j-k] != word[k]:
            return False
    return True

def up(matrix, i, j):
    for k in range(len(word)):
        if i-k < 0 or matrix[i-k][j] != word[k]:
            return False
    return True

def down(matrix, i, j):
    for k in range(len(word)):
        if i+k >= len(matrix) or matrix[i+k][j] != word[k]:
            return False
    return True

def right_down(matrix, i, j):
    for k in range(len(word)):
        if i+k >= len(matrix) or j+k >= len(matrix[i]) or matrix[i+k][j+k] != word[k]:
            return False
    return True

def right_up(matrix, i, j):
    for k in range(len(word)):
        if i-k < 0 or j+k >= len(matrix[i]) or matrix[i-k][j+k] != word[k]:
            return False
    return True

def left_down(matrix, i, j):
    for k in range(len(word)):
        if i+k >= len(matrix) or j-k < 0 or matrix[i+k][j-k] != word[k]:
            return False
    return True

def left_up(matrix, i, j):
    for k in range(len(word)):
        if i-k < 0 or j-k < 0 or matrix[i-k][j-k] != word[k]:
            return False
    return True

sum = 0
for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        if right(matrix, i, j):
            sum += 1
        if left(matrix, i, j):
            sum += 1
        if up(matrix, i, j):
            sum += 1
        if down(matrix, i, j):
            sum += 1
        if right_down(matrix, i, j):
            sum += 1
        if right_up(matrix, i, j):
            sum += 1
        if left_down(matrix, i, j):
            sum += 1
        if left_up(matrix, i, j):
            sum += 1

print(sum)
