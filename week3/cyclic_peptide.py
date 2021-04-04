import os
import sys
import itertools
import w3lib
from pathlib import Path
PROG_NAME = os.path.splitext(sys.argv[0])[0]
DATASET_DIR = os.path.join(os.getcwd(), "datasets/{}".format(PROG_NAME))


def main() :
    util = w3lib.Week3Library()
    description = '''\
        Given the length of the cyclic peptide, it will output the number of all
        subpeptides.

        Input File format :
        ---------------------------------------
        31315
        
        Expected output :
        ---------------------------------------
        980597910
        '''
    args = util.create_parser(__file__, description)

    dataset_path = "{}/real_dataset.txt".format(DATASET_DIR)

    # Default to the dataset folder, if not provided
    if not args.file : args.file = dataset_path

    # Read from dataset file
    with open(args.file, 'r') as f :
        cyclic_peptide_length = int(f.readline().strip())

    num_subpeptides = (cyclic_peptide_length-1) * cyclic_peptide_length
    print(num_subpeptides)
    
if __name__ == "__main__":
    main()