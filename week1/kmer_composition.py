import random
import os
import sys
import random
import w1lib
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
        text = f.readline().strip()

    kmers = get_composition(int(k), text)

    # Write answers to file.
    file_name = os.path.splitext(__file__)[0]
    output_file_path = "./{}_output.txt".format(file_name)
    
    with open(output_file_path, 'w') as f :
        for _ in kmers : f.write("{}\n".format(_))
    
    print('Output is created here : {}'.format(output_file_path))

if __name__ == "__main__":
    main()