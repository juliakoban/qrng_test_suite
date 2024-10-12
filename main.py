from tests.run import run_tests
from utilities.file_loader import *
from utilities.parse_args import *

def main():
    args = parse_arguments( )
    try:
        sequence = load_file( args.file ) 
        run_tests( sequence )
    except FileNotFoundError as e:
        print( e )

if __name__ == "__main__":
    main()