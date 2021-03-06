def Binary_search(Array, item):
    low = 0
    high = len(Array)-1
    while low <= high:
        index = (low + high) // 2
        if item == Array[index]:
            return index + 1
        elif item > Array[index]:
            low = index + 1
        else:
            high = index - 1
    return -1

with open('rosalind_bins.txt','r') as file:
    content = file.read().splitlines()

array = [int(i) for i in content[2].split()]
items = [int(i) for i in content[3].split()]
line = ''

for i in range(len(items)):
    line += str(Binary_search(array, items[i])) + ' '

print(line)