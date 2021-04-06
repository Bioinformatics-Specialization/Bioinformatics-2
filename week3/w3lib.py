import argparse

AA_MASS = {
    'G': 57,
    'A': 71,
    'S': 87,
    'P': 97,
    'V': 99,
    'T': 101,
    'C': 103,
    'I': 113,
    'L': 113,
    'N': 114,
    'D': 115,
    'K': 128,
    'Q': 128,
    'E': 129,
    'M': 131,
    'H': 137,
    'F': 147,
    'R': 156,
    'Y': 163,
    'W': 186
    }

AMINO_ACIDS = {
    'K': ['AAA', 'AAG'], 
    'N': ['AAC', 'AAT'], 
    'T': ['ACA', 'ACC', 'ACG', 'ACT'], 
    'R': ['AGA', 'AGG', 'CGA', 'CGC', 'CGG', 'CGT'], 
    'S': ['AGC', 'AGT', 'TCA', 'TCC', 'TCG', 'TCT'], 
    'I': ['ATA', 'ATC', 'ATT'], 
    'M': ['ATG'], 
    'Q': ['CAA', 'CAG'], 
    'H': ['CAC', 'CAT'], 
    'P': ['CCA', 'CCC', 'CCG', 'CCT'], 
    'L': ['CTA', 'CTC', 'CTG', 'CTT', 'TTA', 'TTG'], 
    'E': ['GAA', 'GAG'], 
    'D': ['GAC', 'GAT'], 
    'A': ['GCA', 'GCC', 'GCG', 'GCT'], 
    'G': ['GGA', 'GGC', 'GGG', 'GGT'], 
    'V': ['GTA', 'GTC', 'GTG', 'GTT'], 
    '*': ['TAA', 'TAG', 'TGA'], 
    'Y': ['TAC', 'TAT'], 
    'C': ['TGC', 'TGT'], 
    'W': ['TGG'], 
    'F': ['TTC', 'TTT']
    }

CODON_TABLE = {
    "UUU":"F", "UUC":"F", "UUA":"L", "UUG":"L",
    "UCU":"S", "UCC":"S", "UCA":"S", "UCG":"S",
    "UAU":"Y", "UAC":"Y", "UAA":"STOP", "UAG":"STOP",
    "UGU":"C", "UGC":"C", "UGA":"STOP", "UGG":"W",
    "CUU":"L", "CUC":"L", "CUA":"L", "CUG":"L",
    "CCU":"P", "CCC":"P", "CCA":"P", "CCG":"P",
    "CAU":"H", "CAC":"H", "CAA":"Q", "CAG":"Q",
    "CGU":"R", "CGC":"R", "CGA":"R", "CGG":"R",
    "AUU":"I", "AUC":"I", "AUA":"I", "AUG":"M",
    "ACU":"T", "ACC":"T", "ACA":"T", "ACG":"T",
    "AAU":"N", "AAC":"N", "AAA":"K", "AAG":"K",
    "AGU":"S", "AGC":"S", "AGA":"R", "AGG":"R",
    "GUU":"V", "GUC":"V", "GUA":"V", "GUG":"V",
    "GCU":"A", "GCC":"A", "GCA":"A", "GCG":"A",
    "GAU":"D", "GAC":"D", "GAA":"E", "GAG":"E",
    "GGU":"G", "GGC":"G", "GGA":"G", "GGG":"G"
    }

def combine_and_format(codons_list) :
    substrings = []

    for codon_pair in codons_list :
        dna_str = codon_pair[0] + codon_pair[1]
        substrings.append(dna_str)
    
    return substrings

def reverseComplement(text):
    rc_text = []
        
    for letter in text[::-1]:
        if letter.upper() == "A" :
            rc_text.append("T")
        elif letter.upper() == "C" :
            rc_text.append("G")
        elif letter.upper() == "G" :
            rc_text.append("C")
        else :
            rc_text.append("A")
        
    return "".join(rc_text)

def linearSubpeptides(peptide) :
    subpeptides = [""]
    pep = list(peptide)
    aa_mass_table = AA_MASS

    # Get all possible linear subpeptides
    for i, each_aa in enumerate(pep) :
        subpeptides.append(each_aa)
        subpeptide = [each_aa]

        for j in range(i+1, len(pep)) :
            subpeptide.append(pep[j])
            subpeptides.append("".join(subpeptide))

    return subpeptides

def prefixSubpeptides(subpeptides) :
    prefixes = []
    
    for subpeptide in subpeptides :
        if subpeptide == "" : 
            prefixes.append(max(subpeptides, key=len))
            continue

        if len(subpeptide) == 1 : 
            continue

        prefixes.append(subpeptide[:-1])

    return prefixes

class Week3Library() :
    def __init__(self) : 
        pass

    def create_parser(self, prog_name, description) :
        parser = argparse.ArgumentParser(
                prog="{}".format(prog_name),
                formatter_class=argparse.RawDescriptionHelpFormatter,
                description=description
                )
    
        parser.add_argument('-f', '--file', required=False, help="Input file path.")

        return parser.parse_args()
    
