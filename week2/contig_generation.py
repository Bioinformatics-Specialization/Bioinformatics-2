import os
import sys
import random
import w2lib
from pathlib import Path
from copy import deepcopy
PROG_NAME = os.path.splitext(sys.argv[0])[0]
DATASET_DIR = os.path.join(os.getcwd(), "datasets/{}".format(PROG_NAME))
WEEK1_DIR = str(Path(__file__).resolve().parents[1]) + "/week1"
sys.path.insert(1, WEEK1_DIR)
from de_bruijn_graph_from_kmers import deBruijnFromKmers
# from maximal_nonbranching_paths import maximalNonBranchingPaths
from genome_path import genomePath

def isOnetoOneNode(node, graph) :
    indegree = 0
    outdegree = 0

    for k, v in graph.items() :
        if node in v :
            indegree += v.count(node)
        
        if k == node :
            outdegree += len(v)
    
    # print("Checking for node {} in the graph.".format(node))
    # print("Indegree: {}, Outdegree: {}".format(indegree, outdegree))

    if indegree == outdegree :
        return True
    
    return False     


def maximalNonBranchingPaths(graph) :
    paths = []
    graph_tracker = deepcopy(graph)
    

    for each_node in graph.keys() :        
        if len(graph_tracker[each_node]) == 0 :
            continue

        if not isOnetoOneNode(each_node, graph) :
            if 0 < len(graph[each_node]) :

                for each_outgoing_edge in graph[each_node] :    
                    nonbranching_path = [each_node, each_outgoing_edge]

                    graph_tracker[each_node].remove(each_outgoing_edge)

                    while isOnetoOneNode(each_outgoing_edge, graph) :
                        
                        nonbranching_path.append(graph[each_outgoing_edge][0])
                        
                        if graph[each_outgoing_edge][0] in graph_tracker[each_outgoing_edge]:
                            graph_tracker[each_outgoing_edge].remove(graph[each_outgoing_edge][0])
                        
                        each_outgoing_edge = graph[each_outgoing_edge][0]

                    paths.append(nonbranching_path)

    # Remove nodes with empty outgoing edges
    for k, v in graph.items() :
        if k in graph_tracker :
            if len(graph_tracker[k]) == 0 :
                del graph_tracker[k]
        
    print("After cleaning..")
    for k, v in graph_tracker.items() :
        print(k, v)

    print(paths)

    # Handle isolated cycles
    while graph_tracker :
        
        node = random.choice(list(graph_tracker))
        current_node = graph_tracker[node][0]
        graph_tracker[node].remove(current_node)
        cycle = [node, current_node]

        if current_node not in graph_tracker : continue

        while current_node != node :
            if current_node not in graph_tracker : 
                break

            next_node = graph_tracker[current_node][0]
            cycle.append(next_node)
            graph_tracker[current_node].remove(next_node)
            current_node = next_node
            
        # Remove nodes with empty outgoing edges
        for k, v in graph.items() :
            if k in graph_tracker :
                if len(graph_tracker[k]) == 0 :
                    del graph_tracker[k]
        
        paths.append(cycle)
    
    return paths


def generateContigs(kmers) :
    # Generate deBruijn graph
    deBruijn = deBruijnFromKmers(kmers)
    
    for k, v in deBruijn.items() :
        print(k, v)
    
    print("--------------------")

    paths = maximalNonBranchingPaths(deBruijn)

    # print(paths)

    for path in paths :
        print(genomePath(path))
    #     print(path)

    # print(genomePath(paths))



def main() :
    util = w2lib.Week2Library()
    description = '''\
        Generate the contigs from a collection of reads (with imperfect coverage).

        Input File format :
        ---------------------------------------
        ATG
        ATG
        TGT
        TGG
        CAT
        GGA
        GAT
        AGA
        
        Expected output :
        ---------------------------------------
        AGA ATG ATG CAT GAT TGGA TGT
        '''
    args = util.create_parser(__file__, description)

    dataset_path = "{}/real_dataset.txt".format(DATASET_DIR)

    # Default to the dataset folder, if not provided
    if not args.file : args.file = dataset_path

    
    # Read from dataset file
    with open(args.file, 'r') as f :
        contents = f.readlines()
        kmers = [_.strip() for _ in contents]
    
    print(kmers)

    result = generateContigs(kmers)

if __name__ == "__main__":
    main()