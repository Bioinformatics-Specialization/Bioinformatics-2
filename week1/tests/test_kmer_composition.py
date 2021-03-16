import unittest
import os
import sys
from pathlib import Path
WEEK1_DIR = str(Path(__file__).resolve().parents[1])
sys.path.insert(1, WEEK1_DIR)

from kmer_composition import get_composition
DATASET_DIR = os.path.join(os.getcwd(), 'datasets/kmer_composition_dataset')


class TestKmerComposition(unittest.TestCase) :
    def test_kmer_composition(self):
        ''' Test sample data '''
        sample_data_input_path = DATASET_DIR + "/inputs/sample.txt"
        sample_data_output_path = DATASET_DIR + "/outputs/sample.txt"
        expected_output = []

        # Read input file
        with open(sample_data_input_path, "r") as f :
            k = f.readline().strip()
            text = f.readline().strip()
        
        # Read output file
        with open(sample_data_output_path, "r") as f :
            contents = f.readlines()
            [expected_output.append(_.strip()) for _ in contents]

        # Run my alg.
        composition = get_composition(int(k), text)
        
        # Make sure items are equal and orders are equal
        self.assertListEqual(expected_output, composition)

        ''' Test test1 data '''



if __name__ == "__main__" :
    unittest.main()


