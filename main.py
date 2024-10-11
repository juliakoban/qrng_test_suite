from tests.run import run_tests
from utilities.file_loader import *

def main():
    sequence = "1100100100001111110110101010001000100001011010001100001000110100110001001100011001100010100010111000"
    try:
        # sequence =  load_file( "./data/asciiFile.txt" ) 
        run_tests( sequence )
    except FileNotFoundError as e:
        print( e )

if __name__ == "__main__":
    main()