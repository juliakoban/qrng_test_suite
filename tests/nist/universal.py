import math

# The focus of this test is the number of bits between matching patterns (a measure that is related to the
# length of a compressed sequence). The purpose of the test is to detect whether or not the sequence can be
# significantly compressed without loss of information. A significantly compressible sequence is
# considered to be non-random. 

def universal_test( input ):
    return 0