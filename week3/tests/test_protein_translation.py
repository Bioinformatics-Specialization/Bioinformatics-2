import unittest
import sys
import os
from pathlib import Path
WEEK3_DIR = str(Path(__file__).resolve().parents[1])
sys.path.insert(1, WEEK3_DIR)

from protein_translation import proteinTranslation
DATASET_DIR = os.path.join(os.getcwd(), 'datasets/protein_translation')


class TestProteinTranlsation(unittest.TestCase) :

    def read_input_data(self, in_data_path):
        
        with open(in_data_path, "r") as f :
            rna = f.readline().strip()
            
        return rna

    def read_output_data(self, out_data_path):
        with open(out_data_path, "r") as f :
            contents = f.readline().strip()
            
        return contents

    def test_protein_translation(self) :
        ''' Test sample data '''
        sample_data_input_path = DATASET_DIR + "/inputs/sample.txt"
        sample_data_output_path = DATASET_DIR + "/outputs/sample.txt"

        # Read input/output file
        rna = self.read_input_data(sample_data_input_path)
        expected_output = self.read_output_data(sample_data_output_path)
        
        # Run my alg.
        output = proteinTranslation(rna)

        self.assertEqual(expected_output, output)


if __name__=="__main__" :
    unittest.main()