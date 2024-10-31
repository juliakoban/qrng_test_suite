import numpy as np
import scipy.special as ss
import math

# The focus of the test is the longest run of ones within M-bit blocks. The purpose of this test is to
# determine whether the length of the longest run of ones within the tested sequence is consistent with the
# length of the longest run of ones that would be expected in a random sequence. Note that an irregularity in
# the expected length of the longest run of ones implies that there is also an irregularity in the expected
# length of the longest run of zeroes. Therefore, only a test for ones is necessary. 

def get_parameters( n ):
    M, K, N = 0, 0, 0 # length of each block, length of ones run for frequencies , number of blocks 
    intervals, pi = [], []
    
    if n < 6272: 
        M, K, N = 8, 3, 16
        intervals = [1, 2, 3, 4]
        pi = [0.2148, 0.3672, 0.2305, 0.1875]
    elif n < 750000:
        M, K, N = 128, 5, 49
        intervals = [4, 5, 6, 7, 8, 9]
        pi = [0.1174035788, 0.242955959, 0.249363483, 0.17517706,  0.102701071, 0.112398847]
    else:
        M, K, N = 10**4, 6, 75
        intervals = [10, 11, 12, 13, 14, 15, 16]
        pi = [0.0882, 0.2092, 0.2483, 0.1933, 0.1208, 0.0675, 0.0727] 
    return M, K, N, intervals, pi

def longest_run_in_block( block ):
    run, longest_run = 0, 0
    for bit in block:
        if bit == '1':
            run += 1
            longest_run = max(longest_run, run)
        else:
            run = 0
    return longest_run

def calculate_chi_squared( vi, pi, N ):
    return sum( ( ( vi[i] - N * pi[i] )**2 ) / ( N * pi[i] ) for i in range( len( pi ) ) )

def longest_run_test( input ):
    n = len( input )
    if n < 128:
        return [0.]

    p_values = []
    M, K, N, intervals, pi = get_parameters( n )
    vi = np.zeros( K + 1 ) # frequencies νi of the longest runs of ones in each block; i - length of ones run
    N = math.floor( n / M ) # this is in NIST code but above N values are in the manual
    
    for i in range( N ):
        block = input[i * M:( i + 1 ) * M]
        longest_run = longest_run_in_block( block )

        for index, value in enumerate(intervals):
            if ( value == min( intervals ) and longest_run <= value ) or \
               ( value == max( intervals ) and longest_run >= value ) or \
               ( longest_run == value ):
                vi[index] += 1
                break
    chi_squared = calculate_chi_squared( vi, pi, N )
    p_value = ss.gammaincc( ( K / 2. ), ( chi_squared / 2. ) )
    p_values.append( p_value )
    return p_values