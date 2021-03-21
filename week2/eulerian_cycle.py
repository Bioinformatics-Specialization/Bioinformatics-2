import os
import sys
import random
import w2lib
from copy import deepcopy
PROG_NAME = os.path.splitext(sys.argv[0])[0]
DATASET_DIR = os.path.join(os.getcwd(), "datasets/{}".format(PROG_NAME))


def eulerCycle(adjacency_dict) :
    if len(adjacency_dict) == 0 : return

    edge_tracker = {}
    nodes = list(adjacency_dict.keys())

    for node in nodes :
        edge_tracker[node] = len(adjacency_dict[node])
    
    curr_path = []
    path = []

    curr_node = random.choice(nodes)
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
    
    return path[::-1]


def main() :
    util = w2lib.Week2Library()
    description = '''\
        Given adjacency list, it will reconstruct and output the Eulerian cycle.

        Input File format :
        ---------------------------------------
        0 -> 3
        1 -> 0
        2 -> 1,6
        3 -> 2
        4 -> 2
        5 -> 4
        6 -> 5,8
        7 -> 9
        8 -> 7
        9 -> 6

        Expected output :
        ---------------------------------------
        6->8->7->9->6->5->4->2->1->0->3->2->6
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
    
    cycle = eulerCycle(adjacency_dict)
    print("->".join(cycle))
    

if __name__ == "__main__":
    main()