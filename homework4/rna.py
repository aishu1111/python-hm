def dna_to_rna(dna):
    return dna.replace('T', 'U')


with open('rosalind_rna.txt') as input_data:
    dna = input_data.read().strip()

rna = dna_to_rna(dna)

print rna
with open('result.txt', 'w') as output_data:
    output_data.write(rna)