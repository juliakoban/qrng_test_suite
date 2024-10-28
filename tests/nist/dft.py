import math
import numpy as np

# The focus of this test is the peak heights in the Discrete Fourier Transform of the sequence. The purpose
# of this test is to detect periodic features (i.e., repetitive patterns that are near each other) in the tested
# sequence that would indicate a deviation from the assumption of randomness. The intention is to detect
# whether the number of peaks exceeding the 95 % threshold is significantly different than 5 %. 

def DFT_test( input ):
    p_values = []
    n = len( input )
    T = math.sqrt( math.log( 1. / 0.05 ) * n ) # the 95 % peak height threshold value
    N0 = ( 0.95 * n ) / 2.  # expected theoretical (95 %) number of peaks (under the assumption of randomness) that are less than T
    
    X = [] # converted sequence 
    for i in range( n ):
        if   input[i] == "1": X.append( 1 )
        else: X.append( -1 )
        
    S = np.fft.fft( X ) # Discrete Fourier Transform
    M = abs( S )[:n//2]
    
    N1 = 0
    for peak in M:
        if peak < T: N1 += 1
            
    d = ( N1 - N0 ) / ( math.sqrt( ( n * 0.95 * 0.05 ) / 4 ) )
    p_value = math.erfc( float( abs( d ) / math.sqrt( 2 ) ) )
    p_values.append( p_value )
    return p_values