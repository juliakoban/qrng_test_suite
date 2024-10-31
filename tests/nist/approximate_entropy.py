import math 
from itertools import product
import scipy.special as ss

# As with the Serial test, the focus of this test is the frequency of all possible overlapping
# m-bit patterns across the entire sequence. The purpose of the test is to compare the frequency of
# overlapping blocks of two consecutive/adjacent lengths (m and m+1) against the expected result for a
# random sequence

def generate_patterns( block_size ): 
    return [''.join( bits ) for bits in product('01', repeat = block_size )] 

def count_pattterns( input_prim, patterns, block_size ):
    frequencies = { pattern: 0 for pattern in patterns }
    for i in range( len( input_prim ) - block_size + 1 ):
        block = input_prim[i:( i + block_size )]
        frequencies[block] += 1
    return frequencies

def approximate_entropy_test( input ):
    n = len( input )
    if n < 1000000: return [0.] 
    
    M = 10
    p_values = []
    c_m_i = list( )
    f_m_i = list( )
    for block_size in range( M, ( M + 2 ) ):
        input_prim = input + input[:( block_size - 1 )]
        patterns = generate_patterns( block_size )
        frequencies = count_pattterns( input_prim, patterns, block_size )
        
        c_i = list( )
        f_i = 0.
        for _, count in frequencies.items( ):
            c_i.append( count / n )
        for i in range( len( c_i ) ):
            if c_i[i] > 0.: f_i += c_i[i] * math.log( c_i[i] )
        c_m_i.append( c_i )
        f_m_i.append( f_i )
    
    ap_en = f_m_i[0] - f_m_i[1]
    chi_squared = 2 * n * ( math.log( 2 ) - ap_en )
    p_value = ss.gammaincc( 2**( M - 1 ), chi_squared / 2. )
    p_values.append( p_value )
    return p_values