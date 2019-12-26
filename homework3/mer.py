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


def main():

    with open('rosalind_mer.txt') as input_data:
        n, A, m, B = [int(line.strip()) if i % 2 == 0 else map(int, line.strip().split()) for i, line in enumerate(input_data.readlines())]

    C = merge_sorted_arrays(A, B)

    print ' '.join(map(str,C))
    with open('result.txt', 'w') as output_data:
        output_data.write(' '.join(map(str,C)))

if __name__ == '__main__':
    main()