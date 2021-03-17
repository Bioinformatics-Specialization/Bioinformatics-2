import os
import sys
import copy
import w1lib
DATASET_DIR = os.path.join(os.getcwd(), 'datasets')


def overlapGraph(kmers) :
    graph = {kmer: [] for kmer in kmers}
        
    for i in range(len(kmers)) :
        dummy_kmers = kmers.copy()
        for j in range(len(dummy_kmers)) :
            if kmers[i] == dummy_kmers[j] : continue

            if kmers[i][1:] == dummy_kmers[j][:-1] :
                graph[kmers[i]].append(dummy_kmers[j])
    
    for k in list(graph.keys()) :
        if len(graph[k]) == 0 :
            del graph[k]

    return graph

def main() :
    util = w1lib.Week1Library()
    description = '''\
        Given collection of kmers, it will create adjacency list of the graph.

        Input File format :
        ---------------------------------------
        ATGCG
        GCATG
        CATGC
        AGGCA
        GGCAT
        GGCAC

        Expected output :
        ---------------------------------------
        CATGC -> ATGCG
        GCATG -> CATGC
        GGCAT -> GCATG
        AGGCA -> GGCAC,GGCAT
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

    graph = overlapGraph(kmers)
    
    output_file = "./output.txt"
    with open(output_file, 'w') as f :
        for k, v in graph.items() :
            f.write("{} -> {}\n".format(k, ",".join(v)))
    
    print("done")


if __name__ == "__main__":
    main()