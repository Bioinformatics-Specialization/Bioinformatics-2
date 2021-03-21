import random
import os
import sys
import itertools
import w2lib
from pathlib import Path
PROG_NAME = os.path.splitext(sys.argv[0])[0]
DATASET_DIR = os.path.join(os.getcwd(), "datasets/{}".format(PROG_NAME))
WEEK1_DIR = str(Path(__file__).resolve().parents[1]) + "/week1"
sys.path.insert(1, WEEK1_DIR)
from eulerian_cycle import eulerCycle
from de_bruijn_graph_from_kmers import deBruijnFromKmers
from genome_path import genomePath

def universalCircularString(k) :
    ucs = [list(_) for _ in list(itertools.product([0, 1], repeat=k))]
    binaries = []
    for binary_str in ucs :
        bin_str = []
        for _ in binary_str :
            bin_str.append(str(_))
        binaries.append("".join(bin_str))
    
    adj_list = deBruijnFromKmers(binaries)

    cycle = eulerCycle(adj_list)
    
    path = genomePath(cycle)
    
    # Exclude last k because it will be reundundant and this needs to cycle around.
    path = path[:len(path)-k+1]
    
    return path


def main() :
    util = w2lib.Week2Library()
    description = '''\
        Given a kmer length, it will create all binary combinations with that length.
        (ex. k=3, 000, 001, 010, 011, 100, 101, 110, 111)
        It then takes the kmer, and construct a cycle that covers all of kmers to
        construct the universal circular string.

        Input File format :
        ---------------------------------------
        4
        
        Expected output :
        ---------------------------------------
        0000110010111101
        '''
    args = util.create_parser(__file__, description)

    dataset_path = "{}/real_dataset.txt".format(DATASET_DIR)

    # Default to the dataset folder, if not provided
    if not args.file : args.file = dataset_path

    # Read from dataset file
    with open(args.file, 'r') as f :
        k = f.readline().strip()

    circular_string = universalCircularString(int(k))
    print(circular_string)

if __name__ == "__main__":
    main()