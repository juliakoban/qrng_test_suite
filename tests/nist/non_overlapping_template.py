import math
import scipy.special as ss

# The focus of this test is the number of occurrences of pre-specified target strings. The purpose of this
# test is to detect generators that produce too many occurrences of a given non-periodic (aperiodic) pattern.
# For this test and for the Overlapping Template Matching test of Section 2.8, an m-bit window is used to
# search for a specific m-bit pattern. If the pattern is not found, the window slides one bit position. If the
# pattern is found, the window is reset to the bit after the found pattern, and the search resumes. 

NUM_OF_BLOCKS = 8 # < 100

def non_overlaping_template_test( input, N = NUM_OF_BLOCKS ):
    p_values = []
    n = len( input )
    if n < 1000: return [0.] 
    M = math.floor( n / N ) # block length, M > 0.01 * N
    template = [0, 0, 0, 0, 0, 0, 0, 0, 1]
    m = len( template ) # m should be 9 or 10 for best results 
    
    blocks = list()
    for i in range( N ):
        block = list()
        for j in range( M ):
            block.append( int( input[i * M + j], 2 ) )
        blocks.append( block )

    W = []
    for block in blocks:
        position = 0
        count = 0
        while position <= ( M - m ):
            if block[position:( position + m )] == template:
                position += m
                count += 1
            else:
                position += 1
        W.append( count )
        
    miu = float( M - m + 1 ) / float( 2**m ) 
    sigma = M * ( ( 1.0 / float( 2**m ) ) - ( float( ( 2 * m ) - 1 ) / float( 2**( 2 * m ) ) ) )
   
    chi_squared = 0.0  
    for i in range( N ):
        chi_squared += ( ( W[i] - miu )**2 ) / sigma

    p_value = ss.gammaincc( N / 2.0, chi_squared / 2.0 ) 
    p_values.append( p_value )
    return p_values