from collections import defaultdict


def two_sum(a, x):
    elmt_hash = defaultdict(set)
    for index, e in enumerate(a):
        elmt_hash[e].add(index)

    for e in elmt_hash:
        if x-e in elmt_hash:
            if x-e == e and len(elmt_hash[e]) > 1:
                return sorted([elmt_hash[e].pop()+1, elmt_hash[e].pop()+1])
            elif x-e != e:
                return sorted([elmt_hash[e].pop()+1, elmt_hash[x-e].pop()+1])

    return -1


with open('rosalind_2sum.txt') as input_data:
    k, n = map(int, input_data.readline().strip().split())
    arrays = [map(int, line.strip().split()) for line in input_data.readlines()]

indices_2sum = [two_sum(a, 0) for a in arrays]
indices_2sum = [str(x) if type(x) is int else ' '.join(map(str, x)) for x in indices_2sum]

print '\n'.join(indices_2sum)
with open('result.txt', 'w') as output_data:
    output_data.write('\n'.join(indices_2sum))
