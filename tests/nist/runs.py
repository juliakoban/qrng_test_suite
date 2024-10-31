import math

# The focus of this test is the total number of runs in the sequence, where a run is an uninterrupted sequence
# of identical bits. A run of length k consists of exactly k identical bits and is bounded before and after with
# a bit of the opposite value. The purpose of the runs test is to determine whether the number of runs of
# ones and zeros of various lengths is as expected for a random sequence. In particular, this test determines
# whether the oscillation between such zeros and ones is too fast or too slow. 

def runs_test( input ):
    n = len( input )
    if n < 100: 
        return [0.]
    
    p_values = []
    ones = input.count( '1' ) 
    pi = float( ones ) / n # pre run proportion
    tao = 2.0 / math.sqrt( n )
    if abs( pi - 0.5 ) > tao: # determines passing of frequency test
        return [0.]
    
    vobs = sum( 1 for i in range( n - 1 ) if input[i] != input[i + 1]) + 1
    p_value = math.erfc( abs( vobs - ( 2 * n *  pi * ( 1 - pi ) ) ) / ( 2 * math.sqrt( 2 * n ) * pi * ( 1 - pi ) ) )
    p_values.append( p_value )
    return p_values