import os
import sys
import itertools
import w3lib
from pathlib import Path
PROG_NAME = os.path.splitext(sys.argv[0])[0]
DATASET_DIR = os.path.join(os.getcwd(), "datasets/{}".format(PROG_NAME))


def peptideEncoding(dna, peptide) :
    encoded_dna = []
    rc_dna = w3lib.reverseComplement(dna)
    aa_code = w3lib.AMINO_ACIDS
    CODON_LEN = 3
    WINDOW = len(peptide) * CODON_LEN

    # Get all combinations of DNA that will encode the peptide
    possible_encodings = [ aa_code[aa] for aa in peptide ]
    possible_encodings = [ "".join(_) for _ in list(itertools.product(*possible_encodings))]
    
    # Consinder the reading frame, which you can shift 3 times.
    for i in range(CODON_LEN) :
        ref_dna = dna[i:]
        ref_rc_dna = rc_dna[i:]
        
        indices = []
        for j in range(0, len(ref_dna)-WINDOW+1, CODON_LEN) :
            current_window = ref_dna[j:j+WINDOW]
            
            if current_window in possible_encodings :
                encoded_dna.append(current_window)

        for j in range(0, len(ref_rc_dna)-WINDOW+1, CODON_LEN) :
            current_window = ref_rc_dna[j:j+WINDOW]

            if current_window in possible_encodings :
                encoded_dna.append(w3lib.reverseComplement(current_window))

    return encoded_dna



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
    for patt in patterns :
        print(patt)
    
if __name__ == "__main__":
    main()