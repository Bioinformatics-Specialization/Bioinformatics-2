import unittest
import sys
from pathlib import Path
WEEK3_DIR = str(Path(__file__).resolve().parents[1])
sys.path.insert(1, WEEK3_DIR)
from linear_spectrum import linearSpectrum

class TestLinearSpectrum(unittest.TestCase) :
    def test_linear_spectrum(self) :
        peptide = "NQEL"
        exptected_result = "0 113 114 128 129 242 242 257 370 371 484"

        result = linearSpectrum(peptide)
        
        self.assertEqual(exptected_result, result)

if __name__ == "__main__" :
    unittest.main()