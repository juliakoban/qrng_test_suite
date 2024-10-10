import math

def frequency( input ):
    ones    = input.count( '1' )
    zeros   = input.count( '0' )
    s_n     = sum( 2 * int(bit) - 1 for bit in input )
    s_obs   = abs( s_n ) / math.sqrt( len( input ) ) 
    p_value = math.erfc( float( s_obs / math.sqrt( 2 ) ) )
    return [ ones, zeros, s_n, s_obs, p_value ]