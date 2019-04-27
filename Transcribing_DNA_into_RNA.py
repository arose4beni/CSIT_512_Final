#Transcribing DNA into RNA

#Defining the Transcription Method
def Transcription(dna):
    rna = dna.replace('T', 'U')
    return rna

#So far I'm just having trouble with the data import
#I get an error when trying to import the data with method below:
#dna_data = open('rosalind_rna.txt', 'r')
#But when I just type a string the method works...
dna_data = 'ACGT'
rna_data = Transcription(dna_data)
print('RNA String: ', rna_data)
