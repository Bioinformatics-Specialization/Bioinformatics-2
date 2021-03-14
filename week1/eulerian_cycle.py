import random
import os
import sys
import w1lib
DATASET_DIR = os.path.join(os.getcwd(), 'datasets')


def eulerCycle(adjacency_dict) :


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
        adjacency_dict[int(row[0])] = [int(r) for r in row[1].split(",")]
    
    cycle = eulerCycle(adjacency_dict)
    print(cycle)

if __name__ == "__main__":
    main()