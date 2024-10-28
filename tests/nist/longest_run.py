import numpy as np
import scipy.special as ss
import math

# The focus of the test is the longest run of ones within M-bit blocks. The purpose of this test is to
# determine whether the length of the longest run of ones within the tested sequence is consistent with the
# length of the longest run of ones that would be expected in a random sequence. Note that an irregularity in
# the expected length of the longest run of ones implies that there is also an irregularity in the expected
# length of the longest run of zeroes. Therefore, only a test for ones is necessary. 

def longest_run_test( input ):
    p_values = []
    n = len( input )
    M, K, N = 0, 0, 0 # length of each block, length of ones run for frequencies , number of blocks 
    intervals, pi = [], []
    if n >= 128 and n < 6272: 
        M, K, N = 8, 3, 16
        intervals = [1, 2, 3, 4]
        pi = [0.2148, 0.3672, 0.2305, 0.1875]
    elif n >= 6272 and n < 750000:
        M, K, N = 128, 5, 49
        intervals = [4, 5, 6, 7, 8, 9]
        pi = [0.1174035788, 0.242955959, 0.249363483, 0.17517706,  0.102701071, 0.112398847]
    elif n >= 750000: 
        M, K, N = 10**4, 6, 75
        intervals = [10, 11, 12, 13, 14, 15, 16]
        pi = [0.0882, 0.2092, 0.2483, 0.1933, 0.1208, 0.0675, 0.0727]
    
    vi = np.zeros( K + 1 ) # frequencies νi of the longest runs of ones in each block; i - length of ones run
    
    N = math.floor( n / M ) # this is in NIST code but above N values are in the manual
    
    for i in range( N ):
        block = input[i * M:( i + 1 ) * M]
        run, longest_run = 0, 0
        for j in range( M ):
            if block[j] == "1": 
                run += 1
            else: run = 0
            longest_run = max( longest_run, run )
   
        for index, value in enumerate( intervals ):
            if value == min( intervals ) and longest_run <= value:
                vi[index] += 1
            elif value == max( intervals ) and longest_run >= value:
                vi[index] += 1
            elif longest_run == value:
                vi[index] += 1
                      
    chi_squared = 0. # A measure of how well the observed longest run length within M-bit blocks matches the expected longest length within M-bit blocks.
    for i in range( K + 1 ):
        chi_squared += ( ( vi[i] - ( N * pi[i] ) )**2 ) / ( N * pi[i])
    p_value = ss.gammaincc( ( K / 2. ), ( chi_squared / 2. ) )
    p_values.append( p_value )
    return p_values