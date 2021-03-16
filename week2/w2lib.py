import argparse


class Week2Library() :

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