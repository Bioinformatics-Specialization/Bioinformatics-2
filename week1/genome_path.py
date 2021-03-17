import random
import os
import sys
import random
import w1lib
PROG_NAME = os.path.splitext(sys.argv[0])[0]
DATASET_DIR = os.path.join(os.getcwd(), "datasets/{}".format(PROG_NAME))


def genomePath(kmers) :
    reconstructed_str = kmers[0]

    for kmer in kmers[1:] :
        reconstructed_str += kmer[-1]
    
    return reconstructed_str

def main() :
    util = w1lib.Week1Library()
    description = '''\
        Given collection of kmers, it will reconstruct the full genome.

        Input File format :
        ---------------------------------------
        ACCGA
        CCGAA
        CGAAG
        GAAGC
        AAGCT

        Expected output :
        ---------------------------------------
        ACCGAAGCT
        '''
    args = util.create_parser(__file__, description)

    dataset_path = "{}/real_dataset.txt".format(DATASET_DIR)

    # Default to the dataset folder, if not provided
    if not args.file : args.file = dataset_path

    kmers = []

    # Read from dataset file
    with open(args.file, 'r') as f :
        contents = f.readlines()
        [kmers.append(_.strip()) for _ in contents]

    path = genomePath(kmers)
    print(path)


if __name__ == "__main__":
    main()