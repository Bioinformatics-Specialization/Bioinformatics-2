import os
import sys
import random
import w2lib
from pathlib import Path
from itertools import chain

PROG_NAME = os.path.splitext(sys.argv[0])[0]
DATASET_DIR = os.path.join(os.getcwd(), "datasets/{}".format(PROG_NAME))
WEEK1_DIR = str(Path(__file__).resolve().parents[1]) + "/week1"
sys.path.insert(1, WEEK1_DIR)
from de_bruijn_graph_from_kmers import deBruijnFromKmers
from genome_path import genomePath


def find_nonbranching_path(path, graph, node, recurse) :
    out_nodes = graph[node]
    
    # Base Case : End of graph (no outnodes)
    if len(out_nodes) == 0 :
        path.append(out_nodes[0])
        return path

    paths = []

    for out_node in out_nodes :
        if not recurse :
            path = [node]
        
        # Check if it's the end of graph
        if out_node not in graph :
            path.append(out_node)
            paths.append(path)
            continue

        # Check if subnode (1,1)
        in_edge = list(chain.from_iterable(graph.values())).count(out_node)
        out_edge = len(graph[out_node])
        
        if (in_edge == 1) and (out_edge == 1) :
            path.append(out_node)
            
            # recursion
            path = find_nonbranching_path(path, graph, out_node, True)

            paths.append(path)

        else :
            path.append(out_node)

            paths.append(path)
        
    if recurse :
        return path

    return paths



def maximalNonBranchingPaths(graph) :
    random.seed(39839)
    # Create dictionary of nodes and in/out degree
    degree_dict = {}
    graph_keys = list(graph.keys())
    graph_vals = list(chain.from_iterable(graph.values()))
    nodes = set(graph_keys + graph_vals)
    
    for node in nodes :
        if node not in degree_dict :
            try :
                outdegree = len(graph[node])
            except :
                outdegree = 0
            indegree = graph_vals.count(node)
            degree_dict[node] = (indegree, outdegree)

    unvisited_node = list(degree_dict.keys())
    current_node = random.choice(unvisited_node)
    contigs = []
    main_nodes = []

    # Iterate through the nodes and find path.
    while True :
        # If node has no outdegree, skip
        if degree_dict[current_node][1] == 0 :
            current_node = random.choice(unvisited_node)

            if len(unvisited_node) == 1 :
                break

            continue

        # Skip nodes that are part of a larger path (indegree==outdegree==1)
        if degree_dict[current_node] == (1,1) :
            unvisited_node.remove(current_node)
            current_node = random.choice(unvisited_node)
            continue
        
        main_nodes.append(current_node)
        
        if len(unvisited_node) == 1 :
            break

        unvisited_node.remove(current_node)
        current_node = random.choice(unvisited_node)
    
    for each_node in main_nodes :        
        paths = find_nonbranching_path([], graph, each_node, False)
        
        for path in paths :
            contig = genomePath(path)
            contigs.append(contig)

    return sorted(contigs)

def generateContigs(kmers) :
    # Generate deBruijn graph
    deBruijn = deBruijnFromKmers(kmers)

    contigs = maximalNonBranchingPaths(deBruijn)

    return contigs
    
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
    
    result = generateContigs(kmers)
    print(" ".join(result))

if __name__ == "__main__":
    main()