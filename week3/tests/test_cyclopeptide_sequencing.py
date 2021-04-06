import unittest
import sys
from pathlib import Path
WEEK3_DIR = str(Path(__file__).resolve().parents[1])
sys.path.insert(1, WEEK3_DIR)
from cyclopeptide_sequencing import cyclopeptideSequencing


class TestCyclopeptideSequencing(unittest.TestCase) :
    def test_sequencing(self) :
        spectrum = ["0", "113", "128", "186", "241", "299", "314", "427"]
        exptected_result = ["186-128-113", "186-113-128", "128-186-113", "128-113-186", "113-186-128", "113-128-186"]

        result = cyclopeptideSequencing(spectrum)
        result = result.split(" ")
        
        self.assertCountEqual(exptected_result, result)

if __name__ == "__main__" :
    unittest.main()