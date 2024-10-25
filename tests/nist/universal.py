import math

# The focus of this test is the number of bits between matching patterns (a measure that is related to the
# length of a compressed sequence). The purpose of the test is to detect whether or not the sequence can be
# significantly compressed without loss of information. A significantly compressible sequence is
# considered to be non-random. 

def universal_test( input ):
    n = len( input )
    
    if   ( n >= 387840 and n < 904960 ): M = 6
    elif ( n >= 904960 and n < 2068480 ): M = 7
    elif ( n >= 2068480 and n < 4654080 ): M = 8
    elif ( n >= 4654080 and n < 10342400 ): M = 9
    elif ( n >= 10342400 and n < 22753280 ): M = 10
    elif ( n >= 22753280 and n < 49643520 ): M = 11
    elif ( n >= 49643520 and n < 107560960 ): M = 12
    elif ( n >= 107560960 and n < 231669760 ): M = 13
    elif ( n >= 231669760 and n < 496435200 ): M = 14
    elif ( n >= 496435200 and n < 1059061760 ): M = 15
    elif ( n >= 1059061760 ): M = 16
    else: return 0
    
    Q = 10 * 2**M
    K = math.floor( n / M ) - Q # remaining blocks
    
    nsymbols = 2**M # this is how many unique M-bit patterns can exist
    T = [0] * nsymbols
    for i in range( Q ):
        pattern = input[i * M:( i + 1 ) * M]
        j = int( pattern, 2 )
        T[j] = i + 1
    
    sum_distances = 0.0
    for i in range( Q, K + Q ):
        pattern = input[i * M:( i + 1 ) * M] 
        j = int( pattern, 2 )  
        dist = ( i + 1 ) - T[j]  
        T[j] = i + 1 
        sum_distances += math.log( dist, 2 )  
        
    fn = sum_distances / K
    
    expected = [0, 0, 0, 0, 0, 0, 5.2177052, 
                6.1962507, 7.1836656, 8.1764248, 9.1723243, 10.170032, 
                11.168765, 12.168070, 13.167693, 14.167488, 15.167379]
    variance = [0, 0, 0, 0, 0, 0, 2.954, 
                3.125, 3.238, 3.311, 3.356, 3.384,
				3.401, 3.410, 3.416, 3.419, 3.421]
    
    c = 0.7 - ( 0.8 / M ) + ( ( 4 + (  32. / M ) ) * ( K**( ( -3. / M ) ) / 15. ) )
    deviation = c * math.sqrt( variance[M] / K )
        
    p_value = math.erfc( abs( ( fn - expected[M] ) / ( math.sqrt( 2 ) * deviation ) ) )
    return p_value