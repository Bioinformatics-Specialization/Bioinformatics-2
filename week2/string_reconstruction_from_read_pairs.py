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


def stringSpelledByGappedPatterns(k, d, paired_kmers) :

    pref_pattern = ""
    suff_pattern = ""

    for pair in paired_kmers[:-1] :
        pref_pattern += pair[0][0]
        suff_pattern += pair[1][0]
    
    pref_pattern += paired_kmers[-1][0]
    suff_pattern += paired_kmers[-1][1]
    
    string_length = 2 * k + d + len(paired_kmers) - 2
    read_length = len(pref_pattern)
    match_length = string_length - read_length

    if pref_pattern[match_length:] == suff_pattern[:-1*match_length] :
        return pref_pattern + suff_pattern[len(suff_pattern)-match_length:]

    return ""


def stringReconstructionFromReadPairs(k, d, pr) :
    adj_list = {}

    for _ in pr :
        reads = _.split("|")
        read1 = reads[0]
        read2 = reads[1]
        prefix1 = read1[:-1]
        suffix1 = read1[1:]
        prefix2 = read2[:-1]
        suffix2 = read2[1:]
        prefix = prefix1 + prefix2
        suffix = suffix1 + suffix2
        prefix_pair = "{}|{}".format(prefix1, prefix2)
        suffix_pair = "{}|{}".format(suffix1, suffix2)


        if prefix in adj_list : 
            adj_list[prefix_pair].append(suffix_pair)
        else :
            adj_list[prefix_pair] = [suffix_pair]
        
    
    eulerpath = eulerPath(adj_list)
    
    # Reformat the path so that stringSpelledByGappedPatterns can accept the input.
    paired_path = []
    for _ in eulerpath :
        paired_path.append(_.split("|"))

    result = stringSpelledByGappedPatterns(k, d, paired_path)

    return result

def main() :
    util = w2lib.Week2Library()
    description = '''\
        Given adjacency list, it will reconstruct and output the Eulerian path.

        Input File format :
        ---------------------------------------
        4 2
        GAGA|TTGA
        TCGT|GATG
        CGTG|ATGT
        TGGT|TGAG
        GTGA|TGTT
        GTGG|GTGA
        TGAG|GTTG
        GGTC|GAGA
        GTCG|AGAT
        
        Expected output :
        ---------------------------------------
        GTGGTCGTGAGATGTTGA
        '''
    args = util.create_parser(__file__, description)

    dataset_path = "{}/real_dataset.txt".format(DATASET_DIR)

    # Default to the dataset folder, if not provided
    if not args.file : args.file = dataset_path

    # Read from dataset file
    with open(args.file, 'r') as f :
        k, d = f.readline().strip().split(" ")
        contents = f.readlines()
        
    paired_reads = [_.strip() for _ in contents]
    
    text = stringReconstructionFromReadPairs(int(k), int(d), paired_reads)
    print(text)


if __name__ == "__main__":
    main()