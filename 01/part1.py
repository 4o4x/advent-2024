

# Read File there is two columns in the file with many space between them
list1 = []
list2 = []
def read_file(file_path):
    with open(file_path, 'r') as file:

        lines = file.readlines()
        for line in lines:
            split_line = line.split()
            list1.append(split_line[0])
            list2.append(split_line[1])

read_file('input.txt')

sorted_list1 = sorted(list1)
sorted_list2 = sorted(list2)

substracted_list = [abs(int(sorted_list2[i]) - int(sorted_list1[i])) for i in range(len(sorted_list1))]

sum_of_substracted_list = sum(substracted_list)

print(sum_of_substracted_list)
