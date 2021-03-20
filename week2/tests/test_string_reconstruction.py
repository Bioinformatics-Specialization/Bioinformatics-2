import unittest
import os
import sys
from pathlib import Path
WEEK2_DIR = str(Path(__file__).resolve().parents[1])
sys.path.insert(1, WEEK2_DIR)

from string_reconstruction import stringReconstruction
DATASET_DIR = os.path.join(os.getcwd(), 'datasets/string_reconstruction')


class TestStringReconstruction(unittest.TestCase) :

    def read_input_data(self, in_data_path):
        # Read from dataset file
        with open(in_data_path, 'r') as f :
            k = f.readline()
            kmers = [_.strip() for _ in f.readlines()]

        return k, kmers

    def read_output_data(self, out_data_path):

        with open(out_data_path, "r") as f :
            path = f.readline().strip()

        return path

    def test_euler_cycle(self):
        NUM_TEST_FILES = 6

        ''' Test sample data '''
        sample_data_input_path = DATASET_DIR + "/inputs/sample.txt"
        sample_data_output_path = DATASET_DIR + "/outputs/sample.txt"

        # Read input/output file
        k, kmers = self.read_input_data(sample_data_input_path)
        expected_output = self.read_output_data(sample_data_output_path)
        
        # Run my alg.
        output = stringReconstruction(int(k), kmers)

        self.assertEqual(expected_output, output)


        ''' Test test1,2,3,4,5,6 data '''
        for i in range(NUM_TEST_FILES) :
            input_path = DATASET_DIR + "/inputs/test{}.txt".format(i+1)
            output_path = DATASET_DIR + "/outputs/test{}.txt".format(i+1)
            
            # Read input/output file
            k, kmers = self.read_input_data(sample_data_input_path)
            expected_output = self.read_output_data(sample_data_output_path)

            # Run my alg.
            output = stringReconstruction(int(k), kmers)

            self.assertEqual(expected_output, output)


if __name__ == "__main__" :
    unittest.main()


