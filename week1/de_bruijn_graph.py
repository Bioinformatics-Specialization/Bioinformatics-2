import os
import sys
import copy
import w1lib
DATASET_DIR = os.path.join(os.getcwd(), 'datasets')


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

    print(k)
    print(text)
    
    # output_file = "./output.txt"
    # with open(output_file, 'w') as f :
    #     for k, v in graph.items() :
    #         f.write("{} -> {}\n".format(k, ",".join(v)))
    
    # print("done")


if __name__ == "__main__":
    main()