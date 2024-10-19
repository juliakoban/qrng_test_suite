import math
import numpy as np

# The focus of the test is the longest run of ones within M-bit blocks. The purpose of this test is to
# determine whether the length of the longest run of ones within the tested sequence is consistent with the
# length of the longest run of ones that would be expected in a random sequence. Note that an irregularity in
# the expected length of the longest run of ones implies that there is also an irregularity in the expected
# length of the longest run of zeroes. Therefore, only a test for ones is necessary. 

def longest_run_test( input ):
    n = len( input )
    M, K, N = 0, 0, 0
    if n >= 128 and n < 6272: M, K, N = 8, 3, 16
    elif n >= 6272 and n < 750000: M, K, N = 128, 5, 49
    elif n >= 750000: M, K, N = 10**4, 6, 75
    
    vi = np.zeros( 7 ) # frequencies νi of the longest runs of ones in each block; i - length of ones run
    for i in range( N ):
        block = input[i * M:( i + 1 ) * M]
        run, longest_run = 0, 0
        for j in range( M ):
            if block[j] == "1": 
                run += 1
                if run > longest_run: longest_run = run 
            else: run = 0
    return 0