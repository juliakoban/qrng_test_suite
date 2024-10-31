import math
import scipy.special as ss
import numpy as np
# The focus of the Overlapping Template Matching test is the number of occurrences of pre-specified target
# strings. Both this test and the Non-overlapping Template Matching test use an m-bit
# window to search for a specific m-bit pattern. As with the previous test, if the pattern is not found,
# the window slides one bit position. The difference between this test and the other test is that
# when the pattern is found, the window slides only one bit before resuming the search. 

NUM_OF_BLOCKS = 968
DEGREES_OF_FREEDOM = 5
BLOCK_LENGTH = 1032

def lgamma(x):
    return math.log( ss.gamma( x ) )
    
def probability( u, eta ):
    if ( u == 0 ):
        p = math.exp( -eta )
    else:
        sum = 0.0
        for l in range( 1, u + 1 ):
            sum += math.exp( -eta - ( u * math.log( 2 ) ) + ( l * math.log( eta ) ) - lgamma( l + 1 ) + lgamma( u ) - lgamma( l ) - lgamma( u - l + 1 ) )
        p = sum
    return p

def generate_blocks( input, N, M ):
    input_array = np.frombuffer( input.encode( 'utf-8' ), dtype = np.uint8 ) - ord( "0" )  
    required_length = N * M
    input_array = input_array[:required_length]
    blocks = input_array.reshape( N, M )  
    return blocks.tolist()  

def count_template_occurrences( blocks, M, K, m, template ):
    v = np.zeros( K + 1, dtype=int )
    for block in blocks:
        count = 0
        for position in range( M - m + 1 ):
            if block[position:( position + m )] == template:
                count += 1
        if count >= ( K ):
            v[K] += 1
        else:
            v[count] += 1
    return v

def calculate_statistics( pi, K, N, M, m, v ):
    lambd = ( M - m + 1 ) / ( 2**m )
    eta = lambd / 2.0
    
    sum = 0.0
    for i in range( K ): 
       pi[i] = probability( i, eta )
       sum += pi[i]
    pi[K] = 1 - sum
    
    chi_squared = 0.0 
    for i in range( K + 1 ):
        chi_squared += ( ( v[i] - ( N * pi[i] ) )**2 / ( N * pi[i] ) )
    p_value = ss.gammaincc(  5.0 / 2.0 , chi_squared / 2.0 )
    return p_value

def overlapping_template_test( input, N = NUM_OF_BLOCKS, K = DEGREES_OF_FREEDOM, M = BLOCK_LENGTH ):
    n = len( input )
    if n < M * N:
        return [0.]
      
    p_values = []  
    template = [1, 1, 1, 1, 1, 1, 1, 1, 1]
    m = len( template ) # should be 9 or 10 due to NIST manual 
    pi = [0.364091, 0.185659, 0.139381, 0.100571, 0.0704323, 0.139865]
    blocks = generate_blocks( input, N, M )
    
    v = count_template_occurrences( blocks, M, K, m, template )
    p_value = calculate_statistics( pi, K, N, M, m, v )    
    p_values.append( p_value )
    return p_values