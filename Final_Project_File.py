# ======================================================================================================================
# Class:    CSIT-512
# Author:   Caleb Timmons, Paula
# Due Date:
# Software/ Program Reference Number:
# Software/ Program Description:        Will take a given txt file with a DNA strand on every line and transcribe than
#                                       translate those DNA strands
#
# Ver no.         Name        Date        Description
# ========        =========   ==========  ============
#
# ======================================================================================================================


# Reads DNA data from a given file
def dna_read(data_file):
    # Create a blank list to hold the dna strands
    dna_list = []
    # Opens the file given
    with open(data_file) as data:
        # Adds each line of the file to the list as a dna strand
        for line in data:
            dna_list.append(line.rstrip())

    return dna_list


# Transcribes the dna strand of
def transcribe(dna):
    # Create an empty list to store the rna strands
    rna_list = []
    for x in dna:
        # Replace all T in dna strand with U
        rna_strand = x.replace('T', 'U')
        # Add RNA strand to the list
        rna_list.append(rna_strand)
    return rna_list


RNA_CODON_TABLE= {
    'UUU': 'F',    'CUU': 'L',    'AUU': 'I',    'GUU': 'V',
    'UUC': 'F',    'CUC': 'L',    'AUC': 'I',    'GUC': 'V',
    'UUA': 'L',    'CUA': 'L',    'AUA': 'I',    'GUA': 'V',
    'UUG': 'L',    'CUG': 'L',    'AUG': 'M',    'GUG': 'V',
    'UCU': 'S',    'CCU': 'P',    'ACU': 'T',    'GCU': 'A',
    'UCC': 'S',    'CCC': 'P',    'ACC': 'T',    'GCC': 'A',
    'UCA': 'S',    'CCA': 'P',    'ACA': 'T',    'GCA': 'A',
    'UCG': 'S',    'CCG': 'P',    'ACG': 'T',    'GCG': 'A',
    'UAU': 'Y',    'CAU': 'H',    'AAU': 'N',    'GAU': 'D',
    'UAC': 'Y',    'CAC': 'H',    'AAC': 'N',    'GAC': 'D',
    'UAA': 'Stop', 'CAA': 'Q',    'AAA': 'K',    'GAA': 'E',
    'UAG': 'Stop', 'CAG': 'Q',    'AAG': 'K',    'GAG': 'E',
    'UGU': 'C',    'CGU': 'R',    'AGU': 'S',    'GGU': 'G',
    'UGC': 'C',    'CGC': 'R',    'AGC': 'S',    'GGC': 'G',
    'UGA': 'Stop', 'CGA': 'R',    'AGA': 'R',    'GGA': 'G',
    'UGG': 'W',    'CGG': 'R',    'AGG': 'R',    'GGG': 'G'
}


def translate(rna_list):
    protein_list = []

    for x in rna_list:
        protein = ''
        for i in range(0, len(x), 3):
            symbol = RNA_CODON_TABLE[x[i:i+3]]
            if symbol == 'Stop':
                break
            protein += symbol
        protein_list.append(protein)
    return protein_list


def main():
    # Asks the user for the name of a file for dna data
    data_file = input('Enter the name of the file to use (include file extension): ')

    # Reads the file for dna data
    dna_list = dna_read(data_file)
    print(dna_list)

    # Sends DNA data to be transcribed
    rna_list = transcribe(dna_list)
    print(rna_list)

    # Sends RNA data to be translated
    protein_list = translate(rna_list)
    print(protein_list)

main()
