import argparse


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