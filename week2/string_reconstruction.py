import os
import sys
import random
import w2lib
from copy import deepcopy
from pathlib import Path
PROG_NAME = os.path.splitext(sys.argv[0])[0]
DATASET_DIR = os.path.join(os.getcwd(), "datasets/{}".format(PROG_NAME))
WEEK1_DIR = str(Path(__file__).resolve().parents[1]) + "/week1"
sys.path.insert(1, WEEK1_DIR)
from eulerian_path import eulerPath
from de_bruijn_graph_from_kmers import deBruijnFromKmers
from genome_path import genomePath

def stringReconstruction(k, kmers) :
    debruijn = deBruijnFromKmers(kmers)
    
    eulerpath = eulerPath(debruijn)
    
    genomepath = genomePath(eulerpath)
    
    return genomepath

def main() :
    util = w2lib.Week2Library()
    description = '''\
        Given adjacency list, it will reconstruct and output the Eulerian path.

        Input File format :
        ---------------------------------------
        4
        CTTA
        ACCA
        TACC
        GGCT
        GCTT
        TTAC
        
        Expected output :
        ---------------------------------------
        GGCTTACCA
        '''
    args = util.create_parser(__file__, description)

    dataset_path = "{}/real_dataset.txt".format(DATASET_DIR)

    # Default to the dataset folder, if not provided
    if not args.file : args.file = dataset_path

    # Read from dataset file
    with open(args.file, 'r') as f :
        k = f.readline()
        kmers = [_.strip() for _ in f.readlines()]

        genome = stringReconstruction(int(k), kmers)
        print(genome)

if __name__ == "__main__":
    main()