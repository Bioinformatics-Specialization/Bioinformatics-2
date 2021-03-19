import random
import os
import sys
import random
import w2lib
from copy import deepcopy
DATASET_DIR = os.path.join(os.getcwd(), 'datasets')

def find_cycle(node, adjacency_dict) : 
    graph_dict = deepcopy(adjacency_dict)
    cycle = [node]

    while True :
        start_node = cycle[0] if len(cycle) == 1 else next_node
        next_nodes = graph_dict[start_node]
        # print("Starting with node {}".format(start_node))
        if 0 < len(next_nodes) :
            next_node = random.choice(next_nodes)
            # print("From {}, I picked node {}".format(next_nodes, next_node))
            cycle.append(next_node)
            # print("Deleting edge that goes to node {}".format(next_node))
            graph_dict[start_node].remove(next_node)
            # print("Now current node {} has outnode of {}".format(start_node, graph_dict[start_node]))

        else :
            # print("returning the cycle...")
            # if node in adjacency_dict[start_node] : cycle.append(node)
            return cycle


def update_adj_dict(adj_dict, cycle) :

    dummy_adj_dict = deepcopy(adj_dict)
    print("-------")
    for k, v in dummy_adj_dict.items() :
        print(k, v)
    print("-------")
    print(cycle)
    print("-------")
    for i in range(len(cycle)-1) :
        current_node = str(cycle[i])
        next_node = str(cycle[i+1])
        
        if next_node in dummy_adj_dict[current_node]  :
            dummy_adj_dict[current_node].remove(next_node)

        if len(dummy_adj_dict[current_node]) == 0 :
            dummy_adj_dict.pop(current_node, None)
    print("******")
    for k, v in dummy_adj_dict.items() :
        print(k, v)
    print("******")
    return dummy_adj_dict

def eulerCycle(adjacency_dict) :
    random.seed(40)
    # random.seed(98)
    available_nodes = list(adjacency_dict.keys())
    start_node = random.choice(available_nodes)
    num_edges = 0
    for k, v in adjacency_dict.items() :
        num_edges = num_edges + len(v)
    
    # Find initial cycle
    cycle = find_cycle(start_node, adjacency_dict)
    first_cycle = cycle.copy()
    # print("Initial Cycle : {}".format("->".join(cycle)))
    # euler_cycle  = euler_cycle + cycle

    unvisited_nodes = []
    
    # for node in cycle :
    #     # print(adjacency_dict[node])
    #     outnodes = adjacency_dict[node]
    #     [unvisited_nodes.append(node) for outnode in outnodes if outnode not in cycle]

    # update adj dict by removing nodes in cycle from adjacency_dict
    cycle = [2,4,2,3,2,1,2,0,3,4,3,0,4,0,2]
    print(cycle)

    dummy_adj_dict = update_adj_dict(adjacency_dict, cycle)

    # dummy_adj_dict = deepcopy(adjacency_dict)
    # for k, v in dummy_adj_dict.items() :
    #     print(k, v)
    # for i in range(len(cycle)-1) :
    #     current_node = str(cycle[i])
    #     next_node = str(cycle[i+1])
        
    #     if next_node in dummy_adj_dict[current_node]  :
    #         dummy_adj_dict[current_node].remove(next_node)

    #     if len(dummy_adj_dict[current_node]) == 0 :
    #         dummy_adj_dict.pop(current_node, None)

    unvisited_nodes = list(dummy_adj_dict.keys())
    # for k, v in dummy_adj_dict.items() :
    #     print(k, v)

    print("List of available nodes to pick...{}".format(unvisited_nodes))

    # If there are no available nodes, then return
    # if len(unvisited_nodes) == 0 : 
    #     print("???")
    #     for k, v in adjacency_dict.items() :
    #         print(k, v)
    #     return "->".join(cycle)
    
    graph_dict = deepcopy(adjacency_dict)
    cycles_dict = {}
    # update adjacency_dict
    counter = 3
    while len(unvisited_nodes) != 0 :
        # print("Still unvisited : {}".format(unvisited_nodes))
        start_node = random.choice(unvisited_nodes)

        # unvisited_nodes.remove(start_node)
        # unvisited_nodes = [_ for _ in unvisited_nodes if _ != start_node]
        print("Picking node {} from available nodes {}.".format(start_node, unvisited_nodes))
        
        for k, v in dummy_adj_dict.items() :
            print(k, v)
        
        cycle = find_cycle(start_node, dummy_adj_dict)  

        print("Cycle : {}".format("->".join(cycle)))

        d_dict = update_adj_dict(dummy_adj_dict, cycle)
        for k, v in d_dict.items() :
            print(k, v)


        unvisited_nodes = list(d_dict.keys())
        print("Unvisited nodes are {}".format(unvisited_nodes))
        
        # euler_cycle  = euler_cycle + cycle
        cycles_dict[cycle[0]] = cycle
        # if counter == 3 : break
    # euler_cycle = euler_cycle[::-1]
    
    # Iterate over
    # for k, v in cycles_dict.items() :
    #     print(k, v)
    
    traversal = []
    # dummy_cycles = deepcopy(cycles_dict)
    for node in first_cycle :
        traversal.append(node)
        if node in cycles_dict :
            for _ in cycles_dict[node][1:] :
                traversal.append(_)
            del cycles_dict[node]


    return "->".join(traversal)



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
    
    # for k, v in adjacency_dict.items() :
    #     print("{} -> {}".format(k, v))
    # print("_____________________________")
    cycle = eulerCycle(adjacency_dict)
    print(cycle)

if __name__ == "__main__":
    main()