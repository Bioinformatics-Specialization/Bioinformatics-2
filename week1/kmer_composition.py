import random
import os
import sys
import random
import w1lib
from copy import deepcopy
DATASET_DIR = os.path.join(os.getcwd(), 'datasets')


def get_composition(k, text) :
    return [text[i:i+k] for i in range(len(text)-k+1)]

def main() :
    util = w1lib.Week1Library()
    description = '''\
        This will list out all the kmers in a string.

        Input File format :
        ---------------------------------------
        5
        CAATCCAAC

        Expected output :
        ---------------------------------------
        CAATC
        AATCC
        ATCCA
        TCCAA
        CCAAC
        '''
    args = util.create_parser(__file__, description)

    dataset_path = "{}/{}_dataset.txt".format(DATASET_DIR, os.path.splitext(sys.argv[0])[0])

    # Default to the dataset folder, if not provided
    if not args.file : args.file = dataset_path

    adjacency_dict = {}

    # Read from dataset file
    with open(args.file, 'r') as f :
        k = f.readline().strip()
        text = f.readline()

    kmers = get_composition(int(k), text)

    output_file_path = "./output.txt"
    with open(output_file_path, 'w') as f :
        for _ in kmers :
            f.write(_)
    # [print(_) for _ in kmers]
    print('done')

if __name__ == "__main__":
    main()