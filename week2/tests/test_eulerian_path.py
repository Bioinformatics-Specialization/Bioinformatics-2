import unittest
import os
import sys
from pathlib import Path
WEEK2_DIR = str(Path(__file__).resolve().parents[1])
sys.path.insert(1, WEEK2_DIR)

from eulerian_path import eulerPath
DATASET_DIR = os.path.join(os.getcwd(), 'datasets/eulerian_path')


class TestEulerPath(unittest.TestCase) :
    def loose_comparison(self, expected_output, output) :
        if len(expected_output) != len(output) :
            return False
        
        if expected_output[0] != output[0] :
            return False

        if expected_output[-1] != output[-1] :
            return False

        return True

    def read_input_data(self, in_data_path):
        adjacency_dict = {}

        # Read from dataset file
        with open(in_data_path, 'r') as f :
            rows = f.readlines()

        for row in rows : 
            row = row.replace(" ", "").strip().split("->")
            adjacency_dict[row[0]] = [r for r in row[1].split(",")]
        
        return adjacency_dict

    def read_output_data(self, out_data_path):

        with open(out_data_path, "r") as f :
            path = f.readline().strip()

        return path

    def test_euler_cycle(self):
        NUM_TEST_FILES = 5

        ''' Test sample data '''
        sample_data_input_path = DATASET_DIR + "/inputs/sample.txt"
        sample_data_output_path = DATASET_DIR + "/outputs/sample.txt"

        # Read input/output file
        adj_dict = self.read_input_data(sample_data_input_path)
        expected_output = self.read_output_data(sample_data_output_path)
        expected_output = expected_output.split("->")
        
        # Run my alg.
        output = eulerPath(adj_dict)

        result = self.loose_comparison(expected_output, output)
        self.assertTrue(result)


        ''' Test test1,2,3,4,5,6 data '''
        for i in range(NUM_TEST_FILES) :
            input_path = DATASET_DIR + "/inputs/test{}.txt".format(i+1)
            output_path = DATASET_DIR + "/outputs/test{}.txt".format(i+1)
            
            # Read input/output file
            adj_dict = self.read_input_data(input_path)
            expected_output = self.read_output_data(output_path)
            expected_output = expected_output.split("->")

            # Run my alg.
            output = eulerPath(adj_dict)

            result = self.loose_comparison(expected_output, output)
            self.assertTrue(result)


if __name__ == "__main__" :
    unittest.main()


