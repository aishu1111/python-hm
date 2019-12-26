def merge_sort(A):
    if len(A) <= 1:
        return A

    midpoint = len(A)/2

    lower = merge_sort(A[:midpoint])
    upper = merge_sort(A[midpoint:])

    return merge_sorted_arrays(lower, upper)

def merge_sorted_arrays(A, B):

    i, j = 0, 0
    C = []

    while i < len(A) and j < len(B):
        if A[i] < B[j]:
            C.append(A[i])
            i += 1
        else:
            C.append(B[j])
            j += 1

    C += A[i:] + B[j:]

    return C


with open('rosalind_ms.txt') as input_data:
    n = int(input_data.readline().strip())
    A = map(int, input_data.readline().strip().split())

B = merge_sort(A)

assert B == sorted(A)

print ' '.join(map(str,B))
with open('result.txt', 'w') as output_data:
    output_data.write(' '.join(map(str,B)))