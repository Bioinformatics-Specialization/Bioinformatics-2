import unittest
import os
import sys
from pathlib import Path
WEEK1_DIR = str(Path(__file__).resolve().parents[1])
sys.path.insert(1, WEEK1_DIR)

from genome_path import genomePath
DATASET_DIR = os.path.join(os.getcwd(), 'datasets/genome_path')


class TestGenomePath(unittest.TestCase):
    def read_input_data(self, in_data_path):
        texts = []
        with open(in_data_path, "r") as f :
            contents = f.readlines()
            [texts.append(_.strip())for _ in contents]
        
        return texts

    def read_output_data(self, out_data_path):
        with open(out_data_path, "r") as f :
            contents = f.readline().strip()
            
        return contents
    
    def test_genome_path(self):
        NUM_TEST_FILES = 3

        ''' Test sample data '''
        sample_data_input_path = DATASET_DIR + "/inputs/sample.txt"
        sample_data_output_path = DATASET_DIR + "/outputs/sample.txt"

        # Read input/output file
        patterns = self.read_input_data(sample_data_input_path)
        expected_output = self.read_output_data(sample_data_output_path)
        
        # Run my alg.
        output = genomePath(patterns)
        
        self.assertEqual(expected_output, output)

        ''' Test test1,2,3 data '''
        for i in range(NUM_TEST_FILES) :
            input_path = DATASET_DIR + "/inputs/test{}.txt".format(i+1)
            output_path = DATASET_DIR + "/outputs/test{}.txt".format(i+1)
            
            # Read input/output file
            patterns = self.read_input_data(input_path)
            expected_output = self.read_output_data(output_path)
            
            # Run my alg.
            output = genomePath(patterns)
            
            self.assertEqual(expected_output, output)


if __name__ == "__main__" :
    unittest.main()