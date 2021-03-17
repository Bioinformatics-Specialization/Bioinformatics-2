import os
import sys
import copy
import w1lib
DATASET_DIR = os.path.join(os.getcwd(), 'datasets')


def deBruijnFromKmers(kmers) :
    adj_dict = {}

    # Get unique prefix/suffix 
    for i in range(len(kmers)) :
        prefix = kmers[i][:-1]
        suffix = kmers[i][1:]

        if prefix not in adj_dict :
            adj_dict[prefix] = []
        
        if suffix not in adj_dict :
            adj_dict[suffix] = []

    # Iterate kmer once more to actually fill up the adj dict
    for i in range(len(kmers)) :
        prefix = kmers[i][:-1]
        suffix = kmers[i][1:]

        adj_dict[prefix].append(suffix)
        
    # for k, v in sorted(adj_dict.items()) :
    #     print("{} | {}".format(k, v))
    for k in list(adj_dict.keys()) :
        if len(adj_dict[k]) == 0 :
            del adj_dict[k]

    return adj_dict

def main() :
    util = w1lib.Week1Library()
    description = '''\
        Given collection of kmers, it will create adjacency list of the graph.

        Input File format :
        ---------------------------------------
        GAGG
        CAGG
        GGGG
        GGGA
        CAGG
        AGGG
        GGAG

        Expected output :
        ---------------------------------------
        AGG -> GGG
        CAG -> AGG,AGG
        GAG -> AGG
        GGA -> GAG
        GGG -> GGA,GGG
        '''
    args = util.create_parser(__file__, description)

    dataset_path = "{}/{}_dataset.txt".format(DATASET_DIR, os.path.splitext(sys.argv[0])[0])

    # Default to the dataset folder, if not provided
    if not args.file : args.file = dataset_path

    kmers = []

    # Read from dataset file
    with open(args.file, 'r') as f :
        contents = f.readlines()
        [kmers.append(_.strip()) for _ in contents]
            
    graph = deBruijnFromKmers(kmers)
    
    # Write answers to file.
    file_name = os.path.splitext(__file__)[0]
    output_file_path = "./{}_output.txt".format(file_name)
    
    with open(output_file_path, 'w') as f :
        for k, v in sorted(graph.items()) : 
            f.write("{} -> {}\n".format(k, ",".join(v)))
    
    print('Output is created here : {}'.format(output_file_path))

if __name__ == "__main__":
    main()