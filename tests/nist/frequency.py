import math

# The focus of the test is the proportion of zeroes and ones for the entire sequence. The purpose of this test
# is to determine whether the number of ones and zeros in a sequence are approximately the same as would
# be expected for a truly random sequence. The test assesses the closeness of the fraction of ones to ½, that
# is, the number of ones and zeroes in a sequence should be about the same. All subsequent tests depend on
# the passing of this test. 

def frequency_test( input ):
    p_values = []
    n = len( input )
    if n < 100: return [0.]
    s_n     = sum( 2 * int(bit) - 1 for bit in input )
    s_obs   = abs( s_n ) / math.sqrt( n ) 
    p_value = math.erfc( float( s_obs / math.sqrt( 2 ) ) )
    p_values.append( p_value )
    return p_values

