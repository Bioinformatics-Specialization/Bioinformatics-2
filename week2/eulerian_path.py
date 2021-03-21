import os
import sys
import random
import w2lib
from copy import deepcopy
PROG_NAME = os.path.splitext(sys.argv[0])[0]
DATASET_DIR = os.path.join(os.getcwd(), "datasets/{}".format(PROG_NAME))


def eulerPath(adjacency_dict) :
    if len(adjacency_dict) == 0 : return

    adj_dict_values = [v for val in list(adjacency_dict.values()) for v in val]
    adj_dict_keys = list(adjacency_dict.keys())
    end_node = ""
    start_node = ""

    # Search for start and end node for the path (unbalanced node)
    for k, v in adjacency_dict.items() :
        outdegree = len(v)
        indegree = adj_dict_values.count(k)

        # If odd degree, it's either start or end node
        if (indegree + outdegree) % 2 != 0 :
            if outdegree < indegree :
                # end node
                end_node = k
            else :
                start_node = k
    
    if end_node == "" :
        for node in list(set(adj_dict_values)) :
            if node not in adj_dict_keys :
                end_node = node
                break
            
    # Create edge from end_node -> start_node which will create
    # euler_cycle, which then we can just run euler_cycle to find
    # the euler_path.
    if end_node in adjacency_dict.keys() :
        adjacency_dict[end_node].append(start_node)
    else :
        adjacency_dict[end_node] = [start_node]

    # Create dictionary to track down edges
    edge_tracker = {}
    nodes = list(adjacency_dict.keys())
    for node in nodes :
        edge_tracker[node] = len(adjacency_dict[node])
    
    curr_path = []
    path = []

    curr_node = start_node 
    curr_path.append(curr_node)
    
    while len(curr_path) :
        if edge_tracker[curr_node] :
            # If there's still outgoing edge
            curr_path.append(curr_node)

            # Choose next node
            next_node = random.choice(adjacency_dict[curr_node])

            # Remove visited edge
            edge_tracker[curr_node] -= 1
            adjacency_dict[curr_node].remove(next_node)

            curr_node = next_node

        else :
            path.append(curr_node)

            # back tracking
            curr_node = curr_path[-1]
            curr_path.pop()

    
    end_node_idx = path.index(end_node)
    
    # Need to reorganize the path
    path = path[end_node_idx:] + path[1:end_node_idx]
    
    return path[::-1]


def main() :
    util = w2lib.Week2Library()
    description = '''\
        Given adjacency list, it will reconstruct and output the Eulerian path.

        Input File format :
        ---------------------------------------
        0 -> 2
        1 -> 3
        2 -> 1
        3 -> 0,4
        6 -> 3,7
        7 -> 8
        8 -> 9
        9 -> 6
        
        Expected output :
        ---------------------------------------
        6->7->8->9->6->3->0->2->1->3->4
        '''
    args = util.create_parser(__file__, description)

    dataset_path = "{}/real_dataset.txt".format(DATASET_DIR)

    # Default to the dataset folder, if not provided
    if not args.file : args.file = dataset_path

    adjacency_dict = {}

    # Read from dataset file
    with open(args.file, 'r') as f :
        rows = f.readlines()

    for row in rows : 
        row = row.replace(" ", "").strip().split("->")
        adjacency_dict[row[0]] = [r for r in row[1].split(",")]
    
    path = eulerPath(adjacency_dict)
    print("->".join(path))
    

if __name__ == "__main__":
    main()