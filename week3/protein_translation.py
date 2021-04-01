import random
import os
import sys
import w3lib
from pathlib import Path
PROG_NAME = os.path.splitext(sys.argv[0])[0]
DATASET_DIR = os.path.join(os.getcwd(), "datasets/{}".format(PROG_NAME))


def proteinTranslation(rna) :
    CODON_LEN = 3
    genetic_code = w3lib.CODON_TABLE
    peptide = []

    for i in range(0, len(rna)-CODON_LEN+1, CODON_LEN) :
        codon = rna[i:i+CODON_LEN]

        if genetic_code[codon] != "STOP" :
            peptide.append(genetic_code[codon])
    
    return "".join(peptide)


def main() :
    util = w3lib.Week3Library()
    description = '''\
        Given a string of RNA, it will translate to sequence of amino acids.

        Input File format :
        ---------------------------------------
        AUGGCCAUGGCGCCCAGAACUGAGAUCAAUAGUACCCGUAUUAACGGGUGA
        
        Expected output :
        ---------------------------------------
        MAMAPRTEINSTRING
        '''
    args = util.create_parser(__file__, description)

    dataset_path = "{}/real_dataset.txt".format(DATASET_DIR)

    # Default to the dataset folder, if not provided
    if not args.file : args.file = dataset_path

    # Read from dataset file
    with open(args.file, 'r') as f :
        rna = f.readline().strip()

    peptide = proteinTranslation(rna)
    print(peptide)

if __name__ == "__main__":
    main()