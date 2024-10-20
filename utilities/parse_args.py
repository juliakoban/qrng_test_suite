import argparse

def parse_arguments( ):
    parser = argparse.ArgumentParser( description = "Statistical Testing of binary/ascii random number files" )
    parser.add_argument( "--file", type = str, default = "./data/QNGFile.dat", help = "File path" )
    parser.add_argument( "--bits", type = int, default = 40000, help = "Number of bits in the sequence" )
    parser.add_argument( "--bitstreams", type = int, default = 100, help = "Number of bit streams" )
    return parser.parse_args()

def print_args( args ):
    print(f"File path: {args.file}")
    print(f"Number of bits in the sequence: {args.bits}")
    print(f"Number of bit streams: {args.bitstreams}")