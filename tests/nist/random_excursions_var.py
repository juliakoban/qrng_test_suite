import math

# The focus of this test is the total number of times that a particular state is visited (i.e., occurs) in a
# cumulative sum random walk. The purpose of this test is to detect deviations from the expected number
# of visits to various states in the random walk. This test is actually a series of eighteen tests (and
# conclusions), one test and conclusion for each of the states: -9, -8, …, -1 and +1, +2, …, +9. 

def random_excursions_var_test( input ):
    n = len( input )
    if n < 1000000: 
        return [0.]
    
    state_range = list( range( -9, 0 ) ) + list( range( 1, 10 ) )
    values = list( )
    for i in range( n ):
        values.append( 2 * int( input[i] ) - 1 )

    s_i = list( )   
    s_i_sum = 0.
    for value in values:
        s_i_sum += value
        s_i.append( s_i_sum )
    s_i_prim = [0.] + s_i + [0.]  # add zeros before and after set S
    
    J = 0
    for value in s_i_prim[1:]:
        if value == 0:
            J += 1
    
    if J < 500: return [0.] * len( state_range )
    
    freq_dict = {state: 0 for state in state_range}
    for value in s_i_prim:
        if value in freq_dict:
            freq_dict[value] += 1
            
    p_values = []    
    for state, count in freq_dict.items( ):
        p_values.append( math.erfc( abs( count - J ) / math.sqrt( ( 2 * J * ( 4 * abs( state ) - 2 ) ) ) ) )
    return p_values