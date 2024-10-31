import math

# The focus of this test is the number of bits between matching patterns (a measure that is related to the
# length of a compressed sequence). The purpose of the test is to detect whether or not the sequence can be
# significantly compressed without loss of information. A significantly compressible sequence is
# considered to be non-random. 

def get_block_length( n ):
    if 387840 <= n < 904960:
        return 6
    elif 904960 <= n < 2068480:
        return 7
    elif 2068480 <= n < 4654080:
        return 8
    elif 4654080 <= n < 10342400:
        return 9
    elif 10342400 <= n < 22753280:
        return 10
    elif 22753280 <= n < 49643520:
        return 11
    elif 49643520 <= n < 107560960:
        return 12
    elif 107560960 <= n < 231669760:
        return 13
    elif 231669760 <= n < 496435200:
        return 14
    elif 496435200 <= n < 1059061760:
        return 15
    elif n >= 1059061760:
        return 16
    return None

def initialize_patterns( input, M, Q ):
    nsymbols = 2**M # this is how many unique M-bit patterns can exist
    T = [0] * nsymbols
    for i in range( Q ):
        pattern = input[i * M:( i + 1 ) * M]
        j = int( pattern, 2 )
        T[j] = i + 1
    return T

def calculate_fn( input, Q, K, M, T ):
    sum_distances = 0.0
    for i in range( Q, K + Q ):
        pattern = input[i * M:( i + 1 ) * M] 
        j = int( pattern, 2 )  
        dist = ( i + 1 ) - T[j]  
        T[j] = i + 1 
        sum_distances += math.log( dist, 2 )    
    fn = sum_distances / K
    return fn

def calculate_p_value( M, K, fn ):
    expected = [0, 0, 0, 0, 0, 0, 5.2177052, 
                6.1962507, 7.1836656, 8.1764248, 9.1723243, 10.170032, 
                11.168765, 12.168070, 13.167693, 14.167488, 15.167379]
    variance = [0, 0, 0, 0, 0, 0, 2.954, 
                3.125, 3.238, 3.311, 3.356, 3.384,
				3.401, 3.410, 3.416, 3.419, 3.421]
    
    c = 0.7 - ( 0.8 / M ) + ( ( 4 + (  32. / M ) ) * ( K**( ( -3. / M ) ) / 15. ) )
    deviation = c * math.sqrt( variance[M] / K ) 
    return math.erfc( abs( ( fn - expected[M] ) / ( math.sqrt( 2 ) * deviation ) ) )
    

def universal_test( input ):
    n = len( input )
    M = get_block_length( n )
    if M is None:
        return [0.]
    
    p_values = []
    Q = 10 * 2**M
    K = math.floor( n / M ) - Q # remaining blocks 
    T = initialize_patterns( input, M, Q )
    fn = calculate_fn( input, Q, K, M, T )
    p_value = calculate_p_value( M, K, fn )
    p_values.append( p_value )
    return p_values