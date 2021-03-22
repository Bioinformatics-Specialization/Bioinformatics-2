import os
import sys
import random
import w2lib
from copy import deepcopy
PROG_NAME = os.path.splitext(sys.argv[0])[0]
DATASET_DIR = os.path.join(os.getcwd(), "datasets/{}".format(PROG_NAME))


def isOnetoOneNode(node, graph) :
    indegree = 0
    outdegree = 0

    for k, v in graph.items() :
        if node in v :
            indegree += 1
        
        if k == node :
            outdegree += len(v)
    
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
                        graph_tracker[each_outgoing_edge].remove(graph[each_outgoing_edge][0])
                        each_outgoing_edge = graph[each_outgoing_edge][0]

                    paths.append(nonbranching_path)

    # Remove nodes with empty outgoing edges
    for k, v in graph.items() :
        if k in graph_tracker :
            if len(graph_tracker[k]) == 0 :
                del graph_tracker[k]
        
  
    # Handle isolated cycles
    while graph_tracker :

        node = random.choice(list(graph_tracker))
        current_node = graph_tracker[node][0]
        graph_tracker[node].remove(current_node)
        cycle = [node, current_node]

        while current_node != node :
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


def main() :
    util = w2lib.Week2Library()
    description = '''\
        Given adjacency list, it will reconstruct and output the Eulerian path.

        Input File format :
        ---------------------------------------
        1 -> 2
        2 -> 3
        3 -> 4,5
        6 -> 7
        7 -> 6
        
        Expected output :
        ---------------------------------------
        1 -> 2 -> 3
        3 -> 4
        3 -> 5
        7 -> 6 -> 7
        '''
    args = util.create_parser(__file__, description)

    dataset_path = "{}/real_dataset.txt".format(DATASET_DIR)

    # Default to the dataset folder, if not provided
    if not args.file : args.file = dataset_path

    # Read from dataset file
    with open(args.file, 'r') as f :
        contents = f.readlines()
    
    # Format into adjacency list
    adj_dict = {}
    for content in contents :
        row = content.split("->")
        left_node = row[0].strip()
        right_node = row[1].strip().split(",")        
        adj_dict[left_node] = right_node
    
    paths = maximalNonBranchingPaths(adj_dict)
    for path in paths :
        print(" -> ".join(path))

if __name__ == "__main__":
    main()