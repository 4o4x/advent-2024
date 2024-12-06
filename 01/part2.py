

# Read File there is two columns in the file with many space between them

map1 = {}
map2 = {}
def read_file(file_path):
    with open(file_path, 'r') as file:

        lines = file.readlines()
        for line in lines:
            split_line = line.split()

            if map1.get(split_line[0]) == None:
                map1[split_line[0]] = 1
            else:
                map1[split_line[0]] += 1
            if map2.get(split_line[1]) == None:
                map2[split_line[1]] = 1
            else:
                map2[split_line[1]] += 1

read_file('input.txt')

sum = 0
for key in map1:
    sum = sum + int(key) * map1[key] * (map2[key] if map2.get(key) != None else 0)

print(sum)
