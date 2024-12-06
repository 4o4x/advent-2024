def read_rules(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
        rules = {}
        for line in lines:
            split_line = line[:-1].split('|')
            if rules.get(int(split_line[1])) == None:
                rules[int(split_line[1])] = [int(split_line[0])]
            else:
                rules[int(split_line[1])].append(int(split_line[0]))
        return rules

def read_line(file_path):
    with open(file_path, 'r') as file:
        all_line = []
        lines = file.readlines()
        for line in lines:
            split_line = line[:-1].split(',')
            all_line.append([int(x) for x in split_line])
        return all_line

sequences = read_line('input2.txt')
rules = read_rules('input1.txt')

sum = 0
for sequence in sequences:
    flag = True
    for i in range(len(sequence)-1):
        sub_sequence = sequence[i+1:]
        for rule in rules[sequence[i]]:
            if rule in sub_sequence:
                flag = False
                break

    if flag:
        sum = sum + sequence[len(sequence)//2]

print(sum)
