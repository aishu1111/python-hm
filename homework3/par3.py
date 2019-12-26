def three_way_partition(a):
    return [x for x in a if x < a[0]] + [a[0]]*a.count(a[0]) + [x for x in a if x > a[0]]


def main():
    with open('rosalind_par3.txt') as input_data:
        input_data.readline() 
        a = map(int, input_data.readline().strip().split())

    a = map(str, three_way_partition(a))

    print ' '.join(a)
    with open('result.txt', 'w') as output_data:
        output_data.write(' '.join(a))


if __name__ == '__main__':
    main()