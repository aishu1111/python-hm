def merge_sorted_arrays_counting_inversions(A, B):
    i, j = 0, 0
    count = 0
    C = []

    while i < len(A) and j < len(B):
        if A[i] <= B[j]:
            C.append(A[i])
            i += 1
        else:
            C.append(B[j])
            count += len(A) - i
            j += 1

    C += A[i:] + B[j:]

    return C, count


def merge_sort_inversion_count(A):
    if len(A) <= 1:
        return A, 0

    midpoint = len(A)/2

    lower, lower_inv = merge_sort_inversion_count(A[:midpoint])
    upper, upper_inv = merge_sort_inversion_count(A[midpoint:])

    combined, combined_inv = merge_sorted_arrays_counting_inversions(lower, upper)

    return combined, lower_inv+upper_inv+combined_inv


def main():
    with open('rosalind_inv.txt') as input_data:
        input_data.readline()
        A = map(int, input_data.readline().strip().split())

    inversions = str(merge_sort_inversion_count(A)[1])

    print inversions
    with open('result.txt', 'w') as output_data:
        output_data.write(inversions)

if __name__ == '__main__':
    main()