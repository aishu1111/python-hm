inputfile = open('rosalind_maj.txt', 'r')
data = inputfile.readlines()
k, n = data[0].split()
k = int(k)
n = int(n)

for i in range(1,k+1):
    arr = data[i].split()
    arr.sort()
    count = {}
    for e in range(len(arr)):
        arr[e] = int(arr[e])
        if arr[e] in count:
            count[arr[e]] += 1
        else:
            count[arr[e]] = 1

    mid = int(n/2)


    if count[arr[mid]] > mid:
        print(str(arr[mid]) + ' ')
    else:
        print(str(-1) + ' ')

inputfile.close()