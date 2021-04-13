import os
import sys
import itertools
import w4lib
from collections import OrderedDict
from copy import deepcopy
from pathlib import Path
PROG_NAME = os.path.splitext(sys.argv[0])[0]
DATASET_DIR = os.path.join(os.getcwd(), "datasets/{}".format(PROG_NAME))
WEEK3_DIR = str(Path(__file__).resolve().parents[1]) + "/week3"
sys.path.insert(1, WEEK3_DIR)
from linear_spectrum import linearSpectrum


def linearScoring(peptide, spectrum) :
    theoretical_spectrum = [int(_) for _ in linearSpectrum(peptide).split(" ")]
    theoretical_spectrum.sort(key=int)

   # Compare the two spectrums and count matches
    score = 0
    i = 0   # Pointer for theoretical_spectrum
    j = 0   # Pointer for spectrum
    while True :
    
        if (i == len(theoretical_spectrum)-1) or (j == len(spectrum)-1) :
            break
        # print(i, j)
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

def trim(leaderboard, spectrum, n) :
    linearScore = {}
    orderedScore = OrderedDict()
    num_candidates = len(leaderboard)

    for j in range(len(leaderboard)) :
        peptide = leaderboard[j]
        linearScore[peptide] = linearScoring(peptide, spectrum)
        
    linearScore = dict(sorted(linearScore.items(), key=lambda x: x[1], reverse=True))

    for k, v in linearScore.items() :
        orderedScore[k] = v
    
    dummy_orderedScore = deepcopy(orderedScore)

    for j in range(n+1, len(orderedScore)) :
        key = list(orderedScore.keys())[j]
        target_key = list(orderedScore.keys())[n]
        
        if orderedScore[key] < orderedScore[target_key] :
            del dummy_orderedScore[key]

    return list(dummy_orderedScore.keys())[:n]
        

def main() :
    util = w4lib.Week4Library()
    description = '''\
        Compute the score of a cyclic peptide against a spectrum.
        
        Input File format :
        ---------------------------------------
        LAST ALST TLLT TQAS
        0 71 87 101 113 158 184 188 259 271 372
        2
        
        Expected output :
        ---------------------------------------
        LAST ALST
        '''
    args = util.create_parser(__file__, description)

    dataset_path = "{}/real_dataset.txt".format(DATASET_DIR)

    # Default to the dataset folder, if not provided
    if not args.file : args.file = dataset_path

    # Read from dataset file
    with open(args.file, 'r') as f :
        leaderboard = f.readline().strip().split(" ")
        spectrum = [int(_) for _ in f.readline().strip().split(" ")]
        n = int(f.readline().strip())

    linear_peptides = trim(leaderboard, spectrum, n)

    print(" ".join(linear_peptides))

if __name__ == "__main__":
    main()