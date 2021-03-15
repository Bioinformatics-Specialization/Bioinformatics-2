import random
import os
import sys
import random
import w1lib
from copy import deepcopy
DATASET_DIR = os.path.join(os.getcwd(), 'datasets')

def find_cycle(node, adjacency_dict) : 
    graph_dict = deepcopy(adjacency_dict)
    cycle = [node]

    while True :
        start_node = cycle[0] if len(cycle) == 1 else next_node
        next_nodes = graph_dict[start_node]
        
        if 0 < len(next_nodes) :
            next_node = random.choice(next_nodes)
            cycle.append(next_node)
            graph_dict[start_node].remove(next_node)
        else :
            if node in adjacency_dict[start_node] : cycle.append(node)
            return cycle

def eulerCycle(adjacency_dict) :
    # random.seed(33)
    available_nodes = list(adjacency_dict.keys())
    start_node = random.choice(available_nodes)

    # Find cycle
    cycle = find_cycle(start_node, adjacency_dict)  
    print("Cycle : {}".format("->".join(cycle)))

def main() :
    util = w1lib.Week1Library()
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

    dataset_path = "{}/{}_dataset.txt".format(DATASET_DIR, os.path.splitext(sys.argv[0])[0])

    # Default to the dataset folder, if not provided
    if not args.file : args.file = dataset_path

    adjacency_dict = {}

    # Read from dataset file
    with open(args.file, 'r') as f :
        rows = f.readlines()

    for row in rows : 
        row = row.replace(" ", "").strip().split("->")
        adjacency_dict[row[0]] = [r for r in row[1].split(",")]
    
    for k, v in adjacency_dict.items() :
        print("{} -> {}".format(k, v))
    print("_____________________________")
    cycle = eulerCycle(adjacency_dict)
    

if __name__ == "__main__":
    main()