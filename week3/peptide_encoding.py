import os
import sys
import itertools
import w3lib
from pathlib import Path
PROG_NAME = os.path.splitext(sys.argv[0])[0]
DATASET_DIR = os.path.join(os.getcwd(), "datasets/{}".format(PROG_NAME))


def peptideEncoding(dna, peptide) :
    encoded_dna = []
    aa_code = w3lib.AMINO_ACIDS
    genetic_code = w3lib.CODON_TABLE
    CODON_LEN = 3
    WINDOW = len(peptide) * CODON_LEN
    print("Window size : {}".format(WINDOW))

    rna = dna.replace("T", "U")

    encoded_codons = []

    for aa in peptide :
        encoded_codons.append(aa_code[aa])
    
    # [('ATG', 'GCT'), ('ATG', 'GCA'), ('ATG', 'GCC'), ('ATG', 'GCG')]
    dna_combinations = list(itertools.product(*encoded_codons))
    dna_combinations = w3lib.combine_and_format(dna_combinations)
    print(dna_combinations)

    for i in range(0, len(dna)-CODON_LEN+1, CODON_LEN) :
        substr = dna[i:i+WINDOW]
        if substr in dna_combinations :
            encoded_dna.append(substr)
    
    print(encoded_dna)
    # indices = []
    # for i in range(0, len(rna)-CODON_LEN+1, CODON_LEN) :
    #     codon = rna[i:i+CODON_LEN]
        
    #     if genetic_code[codon] == peptide[0] :
    #         indices.append(i)
    
    # print(indices)
    # for idx in indices :
    #     substring = rna[idx:idx+WINDOW]
    #     pep = []
    #     for i in range(0, len(substring)-CODON_LEN+1, CODON_LEN) :
    #         # print("{} -> {}".format(substring[i:i+CODON_LEN], genetic_code[substring[i:i+CODON_LEN]]))
    #         pep.append(genetic_code[substring[i:i+CODON_LEN]])
        
    #     if "".join(pep) == peptide :
    #         encoded_dna.append(substring.replace("U", "T"))
        
    #     print(substring)
    
    # print(encoded_dna)



def main() :
    util = w3lib.Week3Library()
    description = '''\
        Given a string of RNA, it will translate to sequence of amino acids.

        Input File format :
        ---------------------------------------
        ATGGCCATGGCCCCCAGAACTGAGATCAATAGTACCCGTATTAACGGGTGA
        MA
        
        Expected output :
        ---------------------------------------
        ATGGCC
        GGCCAT
        ATGGCC
        '''
    args = util.create_parser(__file__, description)

    dataset_path = "{}/real_dataset.txt".format(DATASET_DIR)

    # Default to the dataset folder, if not provided
    if not args.file : args.file = dataset_path

    # Read from dataset file
    with open(args.file, 'r') as f :
        dna = f.readline().strip()
        peptide = f.readline().strip()


    patterns = peptideEncoding(dna, peptide)
    print(patterns)

    rev_dna = util.reverseComplement(dna)
    print(rev_dna)
    patterns = peptideEncoding(rev_dna, peptide)
    print(patterns)

if __name__ == "__main__":
    main()