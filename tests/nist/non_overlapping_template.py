import math
import scipy.special as ss

# The focus of this test is the number of occurrences of pre-specified target strings. The purpose of this
# test is to detect generators that produce too many occurrences of a given non-periodic (aperiodic) pattern.
# For this test and for the Overlapping Template Matching test of Section 2.8, an m-bit window is used to
# search for a specific m-bit pattern. If the pattern is not found, the window slides one bit position. If the
# pattern is found, the window is reset to the bit after the found pattern, and the search resumes. 

BLOCK_LENGTH = 8

def non_overlaping_template_test( input, M = BLOCK_LENGTH ):
    n = len( input )
    N = math.floor( n / M ) # the number of independent blocks
    template_0 = [[0,1],[1,0]]
    m = len( template_0 )
    W = []
    
    blocks = []
    for i in range( N ):
        blocks.append( int( input[i * M:( i + 1 ) * M] ) )


    miu   = float( M - m + 1 ) / float( 2**m )
    sigma = M * ( ( 1. / 2**m ) - ( ( ( 2 * m ) - 1) / ( 2**( 2 * m ) ) ) )
    chi_squared = 0.
    # for i in range( N ): 
        # chi_squared += ( ( W[i] - miu )**2 ) / sigma
    # p_value = ss.gammaincc( N / 2., chi_squared / 2. )
    p_value = 0
    return p_value