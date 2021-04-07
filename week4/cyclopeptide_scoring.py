import os
import sys
import itertools
import w4lib
from pathlib import Path
PROG_NAME = os.path.splitext(sys.argv[0])[0]
DATASET_DIR = os.path.join(os.getcwd(), "datasets/{}".format(PROG_NAME))
WEEK3_DIR = str(Path(__file__).resolve().parents[1]) + "/week3"
sys.path.insert(1, WEEK3_DIR)
from theoretical_spectrum import theoreticalSpectrum

def cyclopeptideScoring(peptide, spectrum) :
    theoretical_spectrum = [int(_) for _ in theoreticalSpectrum(peptide).split(" ")]
    
   # Compare the two spectrums and count matches
    score = 0
    i = 0   # Pointer for theoretical_spectrum
    j = 0   # Pointer for spectrum
    while True :
    
        if (i == len(theoretical_spectrum)-1) or (j == len(spectrum)-1) :
            break

        if theoretical_spectrum[i] == spectrum[j] :
            score = score + 1
            i = i + 1
            j = j + 1
            continue

        if spectrum[j] < theoretical_spectrum[i] :
            j = j + 1
            continue
            
        if theoretical_spectrum[i] < spectrum[j] :
            
            i = i + 1
            continue
            
    if theoretical_spectrum[i] == spectrum[j] :
        score = score + 1
    
    return score


def main() :
    util = w4lib.Week4Library()
    description = '''\
        Compute the score of a cyclic peptide against a spectrum.
        
        Input File format :
        ---------------------------------------
        NQEL
        0 99 113 114 128 227 257 299 355 356 370 371 484
        
        Expected output :
        ---------------------------------------
        11
        '''
    args = util.create_parser(__file__, description)

    dataset_path = "{}/real_dataset.txt".format(DATASET_DIR)

    # Default to the dataset folder, if not provided
    if not args.file : args.file = dataset_path

    # Read from dataset file
    with open(args.file, 'r') as f :
        peptide = f.readline().strip()
        spectrum = [int(_) for _ in f.readline().strip().split(" ")]

    score = cyclopeptideScoring(peptide, spectrum)
    print(score)
    
if __name__ == "__main__":
    main()