from string import maketrans


def reverse_complement_dna(dna):
    transtab = maketrans('ATCG', 'TAGC')
    return dna.translate(transtab)[::-1]


with open('rosalind_revc.txt') as input_data:
    dna = input_data.read().strip()


rev_comp = reverse_complement_dna(dna)


print rev_comp
with open('result.txt', 'w') as output_data:
    output_data.write(rev_comp)