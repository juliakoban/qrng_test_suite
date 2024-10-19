import math

# The focus of this test is the total number of runs in the sequence, where a run is an uninterrupted sequence
# of identical bits. A run of length k consists of exactly k identical bits and is bounded before and after with
# a bit of the opposite value. The purpose of the runs test is to determine whether the number of runs of
# ones and zeros of various lengths is as expected for a random sequence. In particular, this test determines
# whether the oscillation between such zeros and ones is too fast or too slow. 

def runs_test( input ):
    n = len( input )
    ones   = input.count( '1' ) 
    pi = float( ones ) / n # pre run proportion
    tao = 2.0 / math.sqrt( n )
    if abs( pi - 0.5 ) > tao: # determines passing of frequency test
        p_value = 0
    else:
        vobs = 1.0
        for i in range( n - 1 ):
            if input[i] != input[i + 1]:
                vobs += 1.0
        p_value = math.erfc( abs( vobs - ( 2 * n *  pi * ( 1 - pi ) ) ) / ( 2 * math.sqrt( 2 * n ) * pi * ( 1 - pi ) ) )
    return p_value