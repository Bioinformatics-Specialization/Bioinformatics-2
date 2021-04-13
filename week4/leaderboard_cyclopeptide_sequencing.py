import os
import sys
import itertools
import w4lib
from copy import deepcopy
from pathlib import Path
PROG_NAME = os.path.splitext(sys.argv[0])[0]
DATASET_DIR = os.path.join(os.getcwd(), "datasets/{}".format(PROG_NAME))
WEEK3_DIR = str(Path(__file__).resolve().parents[1]) + "/week3"
sys.path.insert(1, WEEK3_DIR)
from theoretical_spectrum import theoreticalSpectrum
from linear_spectrum import linearSpectrum
from cyclopeptide_scoring import cyclopeptideScoring
from trim import trim


def convert_to_masses(peptides) :
    mass_spectrum = []

    for peptide in peptides :
        pep_mass = []
        for each_aa in peptide :
            pep_mass.append(str(w4lib.AA_MASS[each_aa]))
        
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

def get_mass(peptide) :
    mass = 0
    for aa in peptide :
        mass = mass + w4lib.AA_MASS[aa]

    return mass

def leaderboardCyclopeptideSequencing(spectrum, n) :
    MASSES = w4lib.AA_MASS

    base_amino_acids = []

    # Get all the single amino acids from the spectrum
    for mass in spectrum :
        for k, v in MASSES.items() :
            if int(mass) == v : 
                base_amino_acids.append(k)
    
    leaderboard = list(set(base_amino_acids))
    dummy_leaderboard = deepcopy(leaderboard)
    
    leaderpeptide = ""
    validated_candidates = []

    while 0 < len(leaderboard) :
        # Expand
        leaderboard = ["".join(_) for _ in itertools.product(leaderboard, w4lib.AA_MASS.keys())]
        dummy_leaderboard = deepcopy(leaderboard)

        for each_peptide in leaderboard :
            if get_mass(each_peptide) == spectrum[-1] :
                if cyclopeptideScoring(leaderpeptide, spectrum) < cyclopeptideScoring(each_peptide, spectrum) :
                    leaderpeptide = each_peptide

            if spectrum[-1] < get_mass(each_peptide) :
                dummy_leaderboard.remove(each_peptide)
        

        leaderboard = trim(dummy_leaderboard, spectrum, n)
        dummy_leaderboard = deepcopy(leaderboard)

    print(leaderpeptide)

    return "-".join(convert_to_masses(leaderpeptide))


def main() :
    util = w4lib.Week4Library()
    description = '''\
        Compute the score of a cyclic peptide against a spectrum.
        
        Input File format :
        ---------------------------------------
        10
        0 71 113 129 147 200 218 260 313 331 347 389 460
        
        Expected output :
        ---------------------------------------
        113-147-71-129
        '''
    args = util.create_parser(__file__, description)

    dataset_path = "{}/real_dataset.txt".format(DATASET_DIR)

    # Default to the dataset folder, if not provided
    if not args.file : args.file = dataset_path

    # Read from dataset file
    with open(args.file, 'r') as f :
        n = int(f.readline().strip())
        spectrum = [int(_) for _ in f.readline().strip().split(" ")]

    score = leaderboardCyclopeptideSequencing(spectrum, n)
    print(score)
    
if __name__ == "__main__":
    main()