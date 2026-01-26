import argparse
import sys

class MatamzonParser(argparse.ArgumentParser):
    def error(self, message):
        sys.stderr.write("Usage: python3 matamazon.py -l < matamazon_log > -s < matamazon_system > -o <output_file> -os <out_matamazon_system>\n")
        sys.exit(1)
        pass
    
    def get_parser():
        parser = MatamzonParser(description='Matamazon System', 
        usage="Usage: python3 matamazon.py -l < matamazon_log > -s < matamazon_system > -o <output_file> -os <out_matamazon_system>")
        parser.add_argument('-l', type=str, required=True, help='Path to matamazon log file')
        parser.add_argument('-s', type=str, required=False, help='Path to matamazon system file')
        parser.add_argument('-o', type=str, required=False, help='Output file path')
        parser.add_argument('-os', type=str, required=False, help='Output matamazon system file path')
        return parser
        pass

