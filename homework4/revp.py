from string import maketrans


def ReverseComplementDNA(dna):
    '''Returns the reverse complement of a given DNA strand.'''
    transtab = maketrans('ATCG', 'TAGC')
    return dna.translate(transtab)[::-1]

def parse_fasta(s):
    strings = s.strip().split('>')

    for s in strings:
        if len(s) == 0:
            continue

        parts = s.split()
        label = parts[0]
        bases = ''.join(parts[1:])

        results = bases
        
    return results

def reverse_palindromes(dna):
    for length in range(4,13):
	for index in range(len(dna)-length+1):
		if dna[index:index+length] == ReverseComplementDNA(dna[index:index+length]):
			print index+1, length
			locations.append(str(index+1)+' '+str(length))

    with open('result.txt', 'w') as output_data:
        for location in locations:
            output_data.write(location+'\n')

locations = []

large_dataset = open('rosalind_revp.txt').read().strip()
input = parse_fasta(large_dataset)
results = reverse_palindromes(input)