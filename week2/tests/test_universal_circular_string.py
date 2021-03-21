import unittest
import itertools
import sys
from pathlib import Path
WEEK2_DIR = str(Path(__file__).resolve().parents[1])
sys.path.insert(1, WEEK2_DIR)

from universal_circular_string import universalCircularString


class TestUniversalCircularString(unittest.TestCase) :
    
    def verify_circular_string(self, k, user_ucs) :
        ucs = [list(_) for _ in list(itertools.product([0, 1], repeat=k))]
        binaries = []
        for binary_str in ucs :
            bin_str = []
            for _ in binary_str :
                bin_str.append(str(_))
            binaries.append("".join(bin_str))

        for i in range(len(user_ucs)-k+1) : 
            kmer = user_ucs[i:i+k]

            if kmer in binaries :
                binaries.remove(kmer)

        for i in range(i+1, len(user_ucs)) :
            offset = k - abs(len(user_ucs)-i)
            
            kmer = user_ucs[i:] + user_ucs[:offset]
            
            if kmer in binaries :
                binaries.remove(kmer)

        if len(binaries) == 0 :
            return True

        return False


    def test_universal_circular_string(self) :
        klengths = [3,5,7,9]
        
        for k in klengths :
            ucs = universalCircularString(k)
            result = self.verify_circular_string(k, ucs)
            self.assertTrue(result)        


if __name__=="__main__" :
    unittest.main()