import math
import numpy as np

# The focus of the test is the rank of disjoint sub-matrices of the entire sequence. The purpose of this test is
# to check for linear dependence among fixed length substrings of the original sequence. Note that this test
# also appears in the DIEHARD battery of tests

ROWS    = 32
COLUMNS = 32

def rank_probability( rank, M = ROWS, Q = COLUMNS ):
    product = 1.0
    for i in range( rank ):
        upper1 = ( 1.0 - ( 2.0**( i - Q ) ) )
        upper2 = ( 1.0 - ( 2.0**( i - M ) ) )
        lower = 1 - ( 2.0**( i - rank ) )
        product *= ( upper1 * upper2 ) / lower 
    probability = product * ( 2.0**( ( rank * ( Q + M - rank ) ) - ( Q * M ) ) )
    return probability

def compute_probabilities( M = ROWS ):
    FM_prob  = rank_probability( M )
    FMM_prob = rank_probability( M - 1 )
    R_prob   = 1. - ( FM_prob + FMM_prob ) 
    return FM_prob, FMM_prob, R_prob

def binary_rank( matrix, M = ROWS, Q = COLUMNS ): 
    rank = 0
    for col in range(Q):
        # Check for a leading 1 in the current column starting from the current rank row
        pivot_row = next( ( row for row in range( rank, M ) if matrix[row, col] == 1 ), None )
        
        if pivot_row is None:
            continue  # No pivot in this column, move to next column
        # Swap rows only if pivot is not in the current `rank` row
        if pivot_row != rank:
            matrix[[rank, pivot_row]] = matrix[[pivot_row, rank]]
        # Eliminate all rows with a 1 in this column (except the pivot row)
        for row in range( M ):
            if row != rank and matrix[row, col] == 1:
                matrix[row] ^= matrix[rank]  # XOR operation for binary addition
        rank += 1  # Increment the rank after processing the column
    return rank   

def binary_matrix_rank_test( input, M = ROWS, Q = COLUMNS ):
    p_values = []
    MATRIX_SIZE = M * Q
    n = len( input )
    N  = int( math.floor( n / MATRIX_SIZE ) ) # number of blocks
    if N < 38: 
        return [0.]
    
    # compute the reference probabilities for FM, FMM and remainder 
    FM_prob, FMM_prob, R_prob = compute_probabilities( )
    # initialize counts for full rank, rank M-1, and lower rank matrices
    FM, FMM, remainder = 0, 0, 0
    
    for i in range( N ):
        block  = input[i * MATRIX_SIZE:( i + 1 ) * MATRIX_SIZE]
        matrix = np.fromiter(block, dtype=int).reshape(M, Q)
        rank = binary_rank( matrix, M, Q )

        if rank == M: FM += 1
        elif rank == M - 1: FMM += 1
        else: remainder += 1
        
    expected_counts = [FM_prob * N, FMM_prob * N, R_prob * N]
    observed_counts = [FM, FMM, remainder]
    chi_squared = sum(((obs - exp) ** 2) / exp for obs, exp in zip(observed_counts, expected_counts))
    p_value = math.exp(-chi_squared / 2.0)
    p_values.append( p_value )
    return p_values