import math
from scipy.stats import norm

# The focus of this test is the maximal excursion (from zero) of the random walk defined by the cumulative
# sum of adjusted (-1, +1) digits in the sequence. The purpose of the test is to determine whether the
# cumulative sum of the partial sequences occurring in the tested sequence is too large or too small relative
# to the expected behavior of that cumulative sum for random sequences. This cumulative sum may be
# considered as a random walk. For a random sequence, the excursions of the random walk should be near
# zero. For certain types of non-random sequences, the excursions of this random walk from zero will be
# large. 

def compute_p_value( n, z ):
    sum_1 = 0.
    end = math.floor( ( ( n  / z ) - 1 ) / 4 )
    start = math.floor( ( ( -n  / z ) + 1 ) / 4. )
    for i in range( start, end + 1 ):
        x = ( ( ( ( 4 * i ) + 1 ) * z ) / math.sqrt( n ) )
        y = ( ( ( ( 4 * i ) - 1 ) * z ) / math.sqrt( n ) )
        sum_1 += norm.cdf( x ) - norm.cdf( y )
        
    sum_2 = 0.
    end = math.floor( ( ( n  / z ) - 1 ) / 4 )
    start = math.floor( ( ( -n  / z ) - 3 ) / 4. )
    for i in range( start, end + 1 ):
        x = ( ( ( ( 4 * i ) + 3 ) * z ) / math.sqrt( n ) )
        y = ( ( ( ( 4 * i ) + 1 ) * z ) / math.sqrt( n ) )
        sum_2 += norm.cdf( x ) - norm.cdf( y )

    p_value = 1 - sum_1 + sum_2
    return p_value

def cumulative_sums_test( input ):
    p_values = []
    n = len( input )
    if n < 100: return [0.] * 2
    
    values = list( )
    for i in range( n ):
        values.append( 2 * int( input[i] ) - 1 )

    s_i = 0.
    max_forward = 0.    
    for value in values:
        s_i += value
        if abs( s_i ) > max_forward: max_forward = abs( s_i )
    s_i = 0.
    max_backward = 0.    
    for value in reversed( values ):
        s_i += value
        if abs( s_i ) > max_backward: max_backward = abs( s_i )
        
    p_value_f = compute_p_value( n, max_forward )
    p_value_b = compute_p_value( n, max_backward )
    p_values.append( p_value_f )
    p_values.append( p_value_b )
    return p_values