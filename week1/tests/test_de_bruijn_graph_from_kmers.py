import unittest
import os
import sys
from pathlib import Path
WEEK1_DIR = str(Path(__file__).resolve().parents[1])
sys.path.insert(1, WEEK1_DIR)

from de_bruijn_graph_from_kmers import deBruijnFromKmers
DATASET_DIR = os.path.join(os.getcwd(), 'datasets/de_bruijn_graph_from_kmers')


class TestDeBruijnGraphFromKmers(unittest.TestCase):
    def compare_outputs(self, expected_output, output) :
        if len(expected_output) != len(output) :
            return False
        
        keys = list(expected_output.keys())

        for key in keys :
            if key not in output :
                return False
            
            if sorted(output[key]) != sorted(expected_output[key]) :
                return False
        
        return True

    def read_input_data(self, in_data_path):
        texts = []
        with open(in_data_path, "r") as f :
            contents = f.readlines()
            [texts.append(_.strip())for _ in contents]
        
        return texts

    def read_output_data(self, out_data_path):
        contents = []
        with open(out_data_path, "r") as f :
            rows = f.readlines()
            for row in rows :
                contents.append(row.strip())

            
        return contents
    
    def test_de_bruijn_graph_from_kmers(self):
        NUM_TEST_FILES = 4

        ''' Test sample data '''
        sample_data_input_path = DATASET_DIR + "/inputs/sample.txt"
        sample_data_output_path = DATASET_DIR + "/outputs/sample.txt"

        # Read input/output file
        kmers = self.read_input_data(sample_data_input_path)
        expected_output_list = self.read_output_data(sample_data_output_path)
        
        # Format expected outputs into dictinoary
        expected_output = {}
        for _ in expected_output_list :
            row = _.split("->")
            expected_output[row[0].strip()] = row[1].strip().split(",")
        
        # Run my alg.
        output = deBruijnFromKmers(kmers)

        diff = self.compare_outputs(expected_output, output)
        self.assertTrue(diff)

        ''' Test test1,2,3,4 data '''
        for i in range(NUM_TEST_FILES) :
            input_path = DATASET_DIR + "/inputs/test{}.txt".format(i+1)
            output_path = DATASET_DIR + "/outputs/test{}.txt".format(i+1)
            
            # Read input/output file
            kmers = self.read_input_data(input_path)
            expected_output_list = self.read_output_data(output_path)
            
            # Format expected outputs into dictinoary
            expected_output = {}
            for _ in expected_output_list :
                row = _.split("->")
                expected_output[row[0].strip()] = row[1].strip().split(",")
            
            # Run my alg.
            output = deBruijnFromKmers(kmers)

            diff = self.compare_outputs(expected_output, output)
            self.assertTrue(diff)


if __name__ == "__main__" :
    unittest.main()