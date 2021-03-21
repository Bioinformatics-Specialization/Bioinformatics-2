import random
import os
import sys
import w2lib
from pathlib import Path
PROG_NAME = os.path.splitext(sys.argv[0])[0]
DATASET_DIR = os.path.join(os.getcwd(), "datasets/{}".format(PROG_NAME))


def stringSpelledByGappedPatterns(k, d, paired_kmers) :

    pref_pattern = ""
    suff_pattern = ""

    for pair in paired_kmers[:-1] :
        pref_pattern += pair[0][0]
        suff_pattern += pair[1][0]
    
    pref_pattern += paired_kmers[-1][0]
    suff_pattern += paired_kmers[-1][1]
    
    string_length = 2 * k + d + len(paired_kmers) - 1
    read_length = len(pref_pattern)
    match_length = string_length - read_length
    
    if pref_pattern[match_length:] == suff_pattern[:-1*match_length] :
        return pref_pattern + suff_pattern[len(suff_pattern)-match_length:]

    return ""


def main() :
    util = w2lib.Week2Library()
    description = '''\
        Given k-length, distance of the paired reads, and the paired reads itself,
        it will try to align the paired reads to reconstruct the full string. 

        Input File format :
        ---------------------------------------
        4 2
        GACC|GCGC
        ACCG|CGCC
        CCGA|GCCG
        CGAG|CCGG
        GAGC|CGGA
        
        Expected output :
        ---------------------------------------
        GACCGAGCGCCGGA
        '''
    args = util.create_parser(__file__, description)

    dataset_path = "{}/real_dataset.txt".format(DATASET_DIR)

    # Default to the dataset folder, if not provided
    if not args.file : args.file = dataset_path

    # Read from dataset file
    with open(args.file, 'r') as f :
        k, d = f.readline().strip().split(" ")
        contents = f.readlines()
        paired_reads = []

        for _ in contents :
            reads = _.split("|")
            read1 = reads[0].strip()
            read2 = reads[1].strip()
            paired_reads.append([read1, read2])
            
    text = stringSpelledByGappedPatterns(int(k), int(d), paired_reads)
    print(text)


if __name__ == "__main__" :
    main()