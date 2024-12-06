import numpy as np

def read_file(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
        return np.array([list(line)[:-1] for line in lines])


matrix = read_file('input.txt')

word = ['X', 'M', 'A', 'S']


def search_word(matrix):
    """
    search word in 3x3 matrix
    Middle element should be 'A'
    Diagonal elements should be 'M,A,S' can be reverse order too
    """
    print(matrix.shape)
    flag = 0
    if matrix[1][1] != 'A':
        return False
    if matrix[0][0] == 'M' and matrix[2][2] == 'S':
        flag = flag + 1

    if matrix[0][2] == 'M' and matrix[2][0] == 'S':
        flag = flag + 1

    if matrix[0][0] == 'S' and matrix[2][2] == 'M':
        flag = flag + 1

    if matrix[0][2] == 'S' and matrix[2][0] == 'M':
        flag = flag + 1

    if flag == 2:
        return True

    return False

sum = 0
m , n = matrix.shape

for i in range(m-2):
    for j in range(n-2):
        if search_word(matrix[i:i+3, j:j+3]):
            sum += 1

print(sum)
