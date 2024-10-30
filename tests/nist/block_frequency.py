import math
import scipy.special as ss

# The focus of the test is the proportion of ones within M-bit blocks. The purpose of this test is to determine
# whether the frequency of ones in an M-bit block is approximately M/2, as would be expected under an
# assumption of randomness. For block size M=1, this test degenerates to test 1, the Frequency (Monobit)
# test. 

BLOCK_SIZE = 10000

def block_frequency_test( input ):
    p_values = []
    n = len( input )
    N = math.floor( n / BLOCK_SIZE ) # number of blocks
    if n < 100 or N > 100: 
        return [0.]
    
    chi_2 = 0.
    for i in range( N ):
        block = input[i * BLOCK_SIZE:( i + 1 ) * BLOCK_SIZE]
        ones = block.count( '1' )
        proportion =  float( ones ) / BLOCK_SIZE 
        chi_2 += 4 * BLOCK_SIZE * ( proportion - 0.5 )**2
        
    p_value = ss.gammaincc( ( N / 2. ), ( float( chi_2 ) / 2. ) )
    p_values.append( p_value )
    return p_values
