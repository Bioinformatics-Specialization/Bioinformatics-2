import os
import sys
import itertools
import w3lib
from pathlib import Path
PROG_NAME = os.path.splitext(sys.argv[0])[0]
DATASET_DIR = os.path.join(os.getcwd(), "datasets/{}".format(PROG_NAME))




def theoreticalSpectrum(peptide) :
    mass_spectrum = []
    mass_table = w3lib.AA_MASS

    # Get prefixes of linear subpeptides of the prefix peptide
    # (ex. peptide=LEQN -> LEQ)
    linear_spectrum_prefixes = w3lib.linearSubpeptides(peptide[:-1])

    # Calculate mass difference (Total mass - each elem : LEQN - L = EQN)
    diff_peptides = []
    for each_prefix in linear_spectrum_prefixes :
        if each_prefix == peptide : continue

        idx = peptide.index(each_prefix) + len(each_prefix) - 1
        size = len(peptide) - len(each_prefix)

        if (len(peptide) - idx - 1 - size) < 0 :
            end_idx = (len(peptide) - idx - 1 - size) * -1
            diff_peptide = peptide[idx+1:idx+1+size] + peptide[0:end_idx]
            diff_peptides.append(diff_peptide)
            continue

        diff_peptide = peptide[idx+1:idx+1+size]
        diff_peptides.append(diff_peptide)

    circular_peptides = linear_spectrum_prefixes + diff_peptides

    for each_peptide in circular_peptides :
        if each_peptide == "" :
            mass_spectrum.append("0")
            continue
        
        mass = 0
        for each_aa in list(each_peptide) :
            mass = mass + mass_table[each_aa]
        
        mass_spectrum.append(str(mass))

    return " ".join(sorted(mass_spectrum, key=int))


def main() :
    util = w3lib.Week3Library()
    description = '''\
        Given a peptide, it will get all the mass of the circular subpeptides.

        Input File format :
        ---------------------------------------
        LEQN
        
        Expected output :
        ---------------------------------------
        0 113 114 128 129 227 242 242 257 355 356 370 371 484
        '''
    args = util.create_parser(__file__, description)

    dataset_path = "{}/real_dataset.txt".format(DATASET_DIR)

    # Default to the dataset folder, if not provided
    if not args.file : args.file = dataset_path

    # Read from dataset file
    with open(args.file, 'r') as f :
        peptide = f.readline().strip()

    result = theoreticalSpectrum(peptide)
    print(result)
    
if __name__ == "__main__":
    main()