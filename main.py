from utilities.run_tests import run_all_tests
from utilities.file_loader import load_file
from utilities.parse_args import parse_arguments
from tests.tests_list import nist_tests, diehard_tests

def main():
    args = parse_arguments( )
    try:
        file_content = load_file( args.file, args.bits, args.bitstreams ) 
        sequences = [file_content[i:i + args.bits] for i in range( 0, len( file_content ), args.bits)]
        run_all_tests( nist_tests, diehard_tests, sequences, args.file )
    except FileNotFoundError as e:
        print( e )

if __name__ == "__main__":
    main()