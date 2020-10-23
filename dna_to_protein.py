dna_to_rna_bases = {"G" : "C", "C" : "G", "A" : "U", "T" : "A"}
amino_acids = {"UUU" : "Phe", "UUC" : "Phe", "UUA" : "Leu", "UUG" : "Leu", "CUU" : "Leu", "CUC" : "Leu",\
               "CUA" : "Leu", "CUG" : "Leu", "AUU" : "Ile", "AUC" : "Ile", "AUA" : "Ile", "AUG" : "Met",\
               "GUU" : "Val", "GUC" : "Val", "GUA" : "Val", "GUG" : "Val", "UCU" : "Ser", "UCC" : "Ser",\
               "UCA" : "Ser", "UCG" : "Ser", "CCU" : "Pro", "CCC" : "Pro", "CCA" : "Pro", "CCG" : "Pro",\
               "ACU" : "Thr", "ACC" : "Thr", "ACA" : "Thr", "ACG" : "Thr", "GCU" : "Ala", "GCC" : "Ala",\
               "GCA" : "Ala", "GCG" : "Ala", "UAU" : "Tyr", "UAC" : "Tyr", "UAA" : "STOP", "UAG" : "STOP",\
               "CAU" : "His", "CAC" : "His", "CAA" : "Gln", "CAG" : "Gln", "AAU" : "Asn", "AAC" : "Asn",\
               "AAA" : "Lys", "AAG" : "Lys", "GAU" : "Asp", "GAC" : "Asp", "GAA" : "Glu", "GAG" : "Glu",\
               "UGU" : "Cys", "UGC" : "Cys", "UGA" : "STOP", "UGG" : "Trp", "CGU" : "Arg", "CGC" : "Arg",\
               "CGA" : "Arg", "CGG" : "Arg", "AGU" : "Ser", "AGC" : "Ser", "AGA" : "Arg", "AGG" : "Arg",\
               "GGU" : "Gly", "GGC" : "Gly", "GGA" : "Gly", "GGG" : "Gly"}

def check_dna(dna):
    n = 0
    while n < len(dna):
        if dna[n]  not in dna_to_rna_bases or (len(dna)%3) != 0 :
            string = False
        else:
            string = True
        n += 1
    return string    
        
def dna_to_rna(dna):
    n = 0
    rna = ''
    while n < len(dna):
        rna += dna_to_rna_bases[dna[n]]
        n += 1
    return rna
         

def rna_to_protein(rna):
    i = 0
    all_amino = []
    while i < len(rna):
        amino = amino_acids[rna[i:i+3]]
        if amino == 'STOP':
            amino = '*'
            all_amino.append(amino)
        else:
            all_amino.append(amino)
        i += 3
        
    if i > 3:
        space = '-'
        all_amino = space.join(all_amino)
    return all_amino

def count_amino_number(rna):
    def condition (x):
        return x != '*'
    amino_number = int(sum(condition(x) for x in rna)/3)    
    return amino_number

def main():
    dna = input('Enter the DNA sequence:\n')
    dna = dna.upper()
    print (len(dna)%3)
    
    if check_dna(dna) == True:
        print ('DNA: {}'.format(dna))
    
        completed_rna = dna_to_rna(dna)
        print ('RNA: {}'.format(completed_rna))
    
        protein = rna_to_protein(completed_rna)    
        print ('Protein: {}'.format(protein))        
    
        number = count_amino_number(completed_rna)
        print ('The protein has {} amino acids in total'.format(number))
    else :
        print ('Sorry, {} is not a valid DNA sequence for protein synthesis'.format(dna))
        
main()






















