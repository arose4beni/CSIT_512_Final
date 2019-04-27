
def transcription(dna):
    rna = dna.replace('T', 'U')
    return rna


def main():
    with open('rosalind_rna.txt') as data:
        for line in data:
            dna = line
            print(transcription(dna))


main()