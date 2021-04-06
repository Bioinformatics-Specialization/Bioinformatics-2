import os
import sys
import itertools
import w3lib
from copy import deepcopy
from pathlib import Path
PROG_NAME = os.path.splitext(sys.argv[0])[0]
DATASET_DIR = os.path.join(os.getcwd(), "datasets/{}".format(PROG_NAME))

from linear_spectrum import linearSpectrum


def convert_to_masses(peptides) :
    mass_spectrum = []

    for peptide in peptides :
        pep_mass = []
        for each_aa in peptide :
            pep_mass.append(str(w3lib.AA_MASS[each_aa]))
        
        pep_spectrum = "".join("-".join(pep_mass))
        if pep_spectrum not in mass_spectrum :
            mass_spectrum.append(pep_spectrum)

    return mass_spectrum


def is_consistent(peptide, spectrum) :
    dummy_spectrum = deepcopy(spectrum)
    masses = linearSpectrum(peptide).split(" ")[1:]
    masses = sorted(masses, key=int)

    for mass in masses :
        if mass in dummy_spectrum :
            dummy_spectrum.remove(mass)
        else :
            return False
    
    return True


def branch_and_bound(peptides, spectrum) :
    valid_peptides = []

    # Branching step
    extended_peptides = ["".join(_) for _ in itertools.product(peptides, w3lib.AA_MASS.keys())]

    # Bounding step
    for each_peptide in extended_peptides :
        if is_consistent(each_peptide, spectrum) :
            valid_peptides.append(each_peptide)

    return valid_peptides


def cyclopeptideSequencing(spectrum) :
    MASSES = w3lib.AA_MASS

    base_amino_acids = []

    # Get all the single amino acids from the spectrum
    for mass in spectrum :
        for k, v in MASSES.items() :
            if int(mass) == v : 
                base_amino_acids.append(k)

    candidates = branch_and_bound(list(set(base_amino_acids)), spectrum)

    while 0 < len(candidates) :
        validated_candidates = candidates

        candidates = branch_and_bound(candidates, spectrum)

    return " ".join(convert_to_masses(validated_candidates))


def main() :
    util = w3lib.Week3Library()
    description = '''\
        Given the length of the cyclic peptide, it will output the number of all
        subpeptides.

        Input File format :
        ---------------------------------------
        0 113 128 186 241 299 314 427
        
        Expected output :
        ---------------------------------------
        186-128-113 186-113-128 128-186-113 128-113-186 113-186-128 113-128-186
        '''
    args = util.create_parser(__file__, description)

    dataset_path = "{}/real_dataset.txt".format(DATASET_DIR)

    # Default to the dataset folder, if not provided
    if not args.file : args.file = dataset_path

    # Read from dataset file
    with open(args.file, 'r') as f :
        spectrum = f.readline().strip().split(" ")

    cyclopeptides = cyclopeptideSequencing(spectrum)
    print(cyclopeptides)

    
if __name__ == "__main__":
    main()