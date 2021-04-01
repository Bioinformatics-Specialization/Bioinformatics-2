import argparse

AMINO_ACIDS = {
    "M" : ["ATG"],
    "I": ["ATA", "ATC", "ATT"],
    "A":["GCT", "GCA", "GCC", "GCG"],
    "S":["TCA", "TCC", "TCG", "TCT"],
    "F": ["TTC","TTT"],
    "P":["CCA", "CCC", "CCG", "CCT"],
    "C": ["TGC","TGT"],
    "K": ["AAG","AAA"],
    "H": ["CAT","CAC"],
    "D": ["GAT","GAC"],
    "V": ["GTA", "GTC", "GTG", "GTT"],
    "L": ["TTG","TTA","CTA", "CTC", "CTG", "CTT"],
    "W": ["TGG"],
    "T": ["ACA", "ACC", "ACG", "ACT"],
    "R": ["AGA", "AGG", "CGA", "CGG","CGT", "CGC"],
    "Y": ["TAT", "TAC"]
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
    
    def reverseComplement(self, text):
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