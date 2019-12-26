import urllib
import contextlib
from string import maketrans

def ParseFASTA(f):
        '''Extracts the Sequence Name and Nucleotide/Peptide Sequence from the a FASTA format file or website.'''
        fasta_list=[]
        for line in f:

                # If the line starts with '>' we've hit a new DNA strand, so append the old one and create the new one.
                if line[0] == '>':
                        
                        # Using try/except because intially there will be no current DNA strand to append.
                        try:
                                fasta_list.append(current_dna)
                        except UnboundLocalError:
                                pass

                        current_dna = [line.lstrip('>').rstrip('\n'),'']

                # Otherwise, append the current DNA line to the current DNA
                else:
                        current_dna[1] += line.rstrip('\n')
        
        # Append the final DNA strand after reading all the lines.
        fasta_list.append(current_dna)

        return fasta_list

def ReadFASTA(data_location):
        '''Determines the data type of the FASTA format data and passes the appropriate information to be parsed.'''
        
        # If given a list, return fasta information from all items in the list.
        if type(data_location) == list:
                fasta_list =[]
                for location in data_location:
                        fasta_list+=ReadFASTA(location)
                return fasta_list


        # Check for a text file, return fasta info from the text file.
        if data_location[-4:] == '.txt':
                with open(data_location) as f:
                        return ParseFASTA(f)
        
        # Check for a website, return fasta info from the website.
        elif data_location[0:4] == 'http':
                with contextlib.closing(urllib.urlopen(data_location)) as f:
                        return ParseFASTA(f)


def ReverseComplementDNA(dna):
    '''Returns the reverse complement of a given DNA strand.'''
    transtab = maketrans('ATCG', 'TAGC')
    return dna.translate(transtab)[::-1]

DNA_CODON_TABLE = {
    'TTT': 'F',     'CTT': 'L',     'ATT': 'I',     'GTT': 'V',
    'TTC': 'F',     'CTC': 'L',     'ATC': 'I',     'GTC': 'V',
    'TTA': 'L',     'CTA': 'L',     'ATA': 'I',     'GTA': 'V',
    'TTG': 'L',     'CTG': 'L',     'ATG': 'M',     'GTG': 'V',
    'TCT': 'S',     'CCT': 'P',     'ACT': 'T',     'GCT': 'A',
    'TCC': 'S',     'CCC': 'P',     'ACC': 'T',     'GCC': 'A',
    'TCA': 'S',     'CCA': 'P',     'ACA': 'T',     'GCA': 'A',
    'TCG': 'S',     'CCG': 'P',     'ACG': 'T',     'GCG': 'A',
    'TAT': 'Y',     'CAT': 'H',     'AAT': 'N',     'GAT': 'D',
    'TAC': 'Y',     'CAC': 'H',     'AAC': 'N',     'GAC': 'D',
    'TAA': 'Stop',  'CAA': 'Q',     'AAA': 'K',     'GAA': 'E',
    'TAG': 'Stop',  'CAG': 'Q',     'AAG': 'K',     'GAG': 'E',
    'TGT': 'C',     'CGT': 'R',     'AGT': 'S',     'GGT': 'G',
    'TGC': 'C',     'CGC': 'R',     'AGC': 'S',     'GGC': 'G',
    'TGA': 'Stop',  'CGA': 'R',     'AGA': 'R',     'GGA': 'G',
    'TGG': 'W',     'CGG': 'R',     'AGG': 'R',     'GGG': 'G'
}

dna_list = [ReadFASTA('rosalind_orf.txt')[0][1]]
dna_list.append(ReverseComplementDNA(dna_list[0]))
dna_dict = DNA_CODON_TABLE

protein_orf = set()
for dna in dna_list:
	for i in range(len(dna)-2):
		if dna[i:i+3] == 'ATG':
			j = i
			current_protein = ''
			while j+3 < len(dna)-1:
				if dna_dict[dna[j:j+3]] == 'Stop':
					protein_orf.add(current_protein)
					break
				else:
					current_protein += dna_dict[dna[j:j+3]]
				j += 3

protein_orf = map(str, protein_orf)

print '\n'.join(protein_orf)
with open('result.txt', 'w') as output_data:
	output_data.write('\n'.join(protein_orf))