import os
import sys
import itertools
import w3lib
from pathlib import Path
PROG_NAME = os.path.splitext(sys.argv[0])[0]
DATASET_DIR = os.path.join(os.getcwd(), "datasets/{}".format(PROG_NAME))


def linearSpectrum(peptide) :
    subpeptides = []
    masses = ["0"]
    pep = list(peptide)
    aa_mass_table = w3lib.AA_MASS

    # Get all possible linear subpeptides
    for i, each_aa in enumerate(pep) :
        subpeptides.append(each_aa)
        subpeptide = [each_aa]

        for j in range(i+1, len(pep)) :
            subpeptide.append(pep[j])
            subpeptides.append("".join(subpeptide))

    # Calculate masses for each subpeptides
    for subpep in subpeptides :
        subpep = list(subpep)

        mass = 0
        for aa in subpep :
            mass = mass + aa_mass_table[aa]
        
        masses.append(str(mass))

    return " ".join(sorted(masses))


def main() :
    util = w3lib.Week3Library()
    description = '''\
        Given a peptide, it will give out mass spectrum of all the linear
        subpeptides.

        Input File format :
        ---------------------------------------
        NQEL
        
        Expected output :
        ---------------------------------------
        0 113 114 128 129 242 242 257 370 371 484
        '''
    args = util.create_parser(__file__, description)

    dataset_path = "{}/real_dataset.txt".format(DATASET_DIR)

    # Default to the dataset folder, if not provided
    if not args.file : args.file = dataset_path

    # Read from dataset file
    with open(args.file, 'r') as f :
        peptide = f.readline().strip()

    mass_spectrum = linearSpectrum(peptide)
    print(mass_spectrum)

      
if __name__ == "__main__":
    main()