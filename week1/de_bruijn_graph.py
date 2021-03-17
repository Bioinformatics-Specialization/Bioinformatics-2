import os
import sys
import copy
import w1lib
DATASET_DIR = os.path.join(os.getcwd(), 'datasets')


def deBruijn(k, text) :
    adjacent_dict = {}
    
    for i in range(len(text)-k+1) :
        pattern = text[i:i+k]
        prefix = pattern[:-1]
        suffix = pattern[1:]

        if prefix not in adjacent_dict :
            adjacent_dict[prefix] = [suffix]
        else :
            adjacent_dict[prefix].append(suffix)

    return adjacent_dict        


def main() :
    util = w1lib.Week1Library()
    description = '''\
        Given collection of kmers, it will create adjacency list of the graph.

        Input File format :
        ---------------------------------------
        4
        AAGATTCTCTAAGA

        Expected output :
        ---------------------------------------
        AAG -> AGA,AGA
        AGA -> GAT
        ATT -> TTC
        CTA -> TAA
        CTC -> TCT
        GAT -> ATT
        TAA -> AAG
        TCT -> CTA,CTC
        TTC -> TCT
        '''
    args = util.create_parser(__file__, description)

    dataset_path = "{}/{}_dataset.txt".format(DATASET_DIR, os.path.splitext(sys.argv[0])[0])

    # Default to the dataset folder, if not provided
    if not args.file : args.file = dataset_path

    # Read from dataset file
    with open(args.file, 'r') as f :
        k = f.readline().strip()
        text = f.readline().strip()

    graph = deBruijn(int(k), text)
    
    # Write answers to file.
    file_name = os.path.splitext(__file__)[0]
    output_file_path = "./{}_output.txt".format(file_name)
    
    with open(output_file_path, 'w') as f :
        for k, v in sorted(graph.items()) : 
            f.write("{} -> {}\n".format(k, ",".join(v)))
    
    print('Output is created here : {}'.format(output_file_path))

if __name__ == "__main__":
    main()