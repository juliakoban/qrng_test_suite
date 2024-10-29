import scipy.special as ss
from itertools import product

# The focus of this test is the frequency of all possible overlapping m-bit patterns across the entire
# sequence. The purpose of this test is to determine whether the number of occurrences of the 2**m m-bit
# overlapping patterns is approximately the same as would be expected for a random sequence. Random
# sequences have uniformity; that is, every m-bit pattern has the same chance of appearing as every other
# m-bit pattern. Note that for m = 1, the Serial test is equivalent to the Frequency test.
 
def generate_patterns( block_size ): 
    return [''.join( bits ) for bits in product('01', repeat = block_size )] 

def count_pattterns( input_prim, patterns, block_size ):
    frequencies = { pattern: 0 for pattern in patterns }
    for i in range( len( input_prim ) - block_size + 1 ):
        block = input_prim[i:( i + block_size )]
        frequencies[block] += 1
    return frequencies

def psi_squared( block_size, input_size, frequencies ):
    result = 0. 
    for _, count in frequencies.items():
        result += count**2
    result  = result * ( 2**block_size / input_size ) - input_size
    return result

def compute( input, block_size, input_size ):
    input_prim = input + input[:( block_size - 1 )]
    patterns = generate_patterns( block_size )
    frequencies = count_pattterns( input_prim, patterns, block_size )
    return psi_squared( block_size, input_size, frequencies )

def serial_test( input ):
    p_values = []
    n = len( input )
    M = 16
    if n < 1000000: return [0.] 
    # if M < int( math.floor( math.log( n, 2 ) ) ) - 2:
    #    return 0
    
    psi_m_3 = compute( input, M, n )
    psi_m_2 = compute( input, M - 1, n )
    psi_m_1 = compute( input, M - 2, n )
    
    delta_psi = psi_m_3 - psi_m_2
    delta_2_psi = psi_m_3 - ( 2 * psi_m_2 ) + psi_m_1 
    
    p_value_1 = ss.gammaincc( 2**( M - 2 ) , delta_psi / 2. )
    p_value_2 = ss.gammaincc( 2**( M - 3 ) , delta_2_psi / 2. )
    p_values.append( p_value_1 )
    p_values.append( p_value_2 )
    return p_values 