from collections import Counter


def base_count_dna(dna):
    base_count = Counter(dna)
    return [base_count[base] for base in 'ACGT']


with open('rosalind_dna.txt') as input_data:
    dna = input_data.read().strip()


base_count = map(str, base_count_dna(dna))


print ' '.join(base_count)
with open('result.txt', 'w') as output_data:
    output_data.write(' '.join(base_count))