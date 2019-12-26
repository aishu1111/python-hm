def insertion_sort_count(arr):
    count = 0
    n = len(arr)
    for i in range(0, n):
        j = i
        while j > 0 and arr[j] < arr[j-1]:
            arr[j], arr[j-1] = arr[j-1], arr[j]
            count += 1
            j -= 1

    return count

inputfile = open('rosalind_ins.txt', 'r')
data = inputfile.readlines()

n = int(data[0])
elements = list(map(int, data[1].split()))

result = insertion_sort_count(elements)
inputfile.close()
print (result)