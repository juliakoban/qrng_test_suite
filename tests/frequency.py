import math
import numpy as np
from utilities.statistics import *

TEST_NAME = "FREQUENCY"
bins = np.arange(0., 1.1, 0.1)

def frequency_test( input ):
    s_n     = sum( 2 * int(bit) - 1 for bit in input )
    s_obs   = abs( s_n ) / math.sqrt( len( input ) ) 
    p_value = math.erfc( float( s_obs / math.sqrt( 2 ) ) )
    return p_value
    
def frequency( input ):
    p_values = [frequency_test( input[i] ) for i in range( 0, len( input ) )]
    hist, _ = np.histogram(p_values, bins = bins)
    p_value_chi = chi_squared( p_values, bins, hist )
    p_value_ks  = Kolmogorov_Smirnov( p_values )
    return [hist, p_value_chi, p_value_ks, TEST_NAME]
