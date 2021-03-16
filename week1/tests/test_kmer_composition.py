import unittest
import os
import sys
from pathlib import Path
WEEK1_DIR = str(Path(__file__).resolve().parents[1])
sys.path.insert(1, WEEK1_DIR)

from kmer_composition import get_composition
DATASET_DIR = os.path.join(os.getcwd(), 'datasets/kmer_composition_test_dataset')


class TestKmerComposition(unittest.TestCase) :
    def read_input_data(self, in_data_path):
        with open(in_data_path, "r") as f :
            k = f.readline().strip()
            text = f.readline().strip()
        
        return k, text

    def read_output_data(self, out_data_path):
        output = []

        with open(out_data_path, "r") as f :
            contents = f.readlines()
            [output.append(_.strip()) for _ in contents]

        return output

    def test_kmer_composition(self):
        NUM_TEST_FILES = 4

        ''' Test sample data '''
        sample_data_input_path = DATASET_DIR + "/inputs/sample.txt"
        sample_data_output_path = DATASET_DIR + "/outputs/sample.txt"

        # Read input/output file
        k, text = self.read_input_data(sample_data_input_path)
        expected_output = self.read_output_data(sample_data_output_path)

        # Run my alg.
        composition = get_composition(int(k), text)
        
        # Make sure items are equal and orders are equal
        self.assertListEqual(expected_output, composition)

        ''' Test test1,2,3,4 data '''
        for i in range(NUM_TEST_FILES) :
            input_path = DATASET_DIR + "/inputs/test{}.txt".format(i+1)
            output_path = DATASET_DIR + "/outputs/test{}.txt".format(i+1)
            
            # Read input/output file
            k, text = self.read_input_data(input_path)
            expected_output = self.read_output_data(output_path)
            
            # Run my alg.
            composition = get_composition(int(k), text)
            
            # Make sure items are equal and orders are equal
            self.assertListEqual(expected_output, composition)


if __name__ == "__main__" :
    unittest.main()


