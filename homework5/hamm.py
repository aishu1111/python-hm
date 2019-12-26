from itertools import imap
from operator import ne


def hamming_distance(seq1, seq2):
    if len(seq1) != len(seq2):
        raise ValueError('Undefined for sequences of unequal length.')
    return sum(imap(ne, seq1, seq2))


with open('rosalind_hamm.txt') as input_data:
    seq1, seq2 = [line.strip() for line in input_data]

    
h_dist = str(hamming_distance(seq1,seq2))

print h_dist
with open('result.txt', 'w') as output_data:
    output_data.write(h_dist)