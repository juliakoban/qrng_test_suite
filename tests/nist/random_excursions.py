import scipy.special as ss

# The focus of this test is the number of cycles having exactly K visits in a cumulative sum random walk.
# The cumulative sum random walk is derived from partial sums after the (0,1) sequence is transferred to
# the appropriate (-1, +1) sequence. A cycle of a random walk consists of a sequence of steps of unit length
# taken at random that begin at and return to the origin. The purpose of this test is to determine if the
# number of visits to a particular state within a cycle deviates from what one would expect for a random
# sequence. This test is actually a series of eight tests (and conclusions), one test and conclusion for each of
# the states: -4, -3, -2, -1 and +1, +2, +3, +4. 

def construct_cycles( s_prim ):
    cycles = []
    curr_cycle = []
    for value in s_prim[1:]:
        if value == 0.: 
            if curr_cycle:
                curr_cycle.append( 0. )
                cycles.append( curr_cycle )
                curr_cycle = []
        else:
            if not curr_cycle:
                curr_cycle.append( 0. )
            curr_cycle.append( value )
    if len( cycles ) < 500: return 0
    return cycles

def compute_frequencies( cycles, state_range ):
    frequencies = []
    for cycle in cycles:
        freq_dict = {state: 0 for state in state_range}
        for value in cycle:
            if value in freq_dict:
                freq_dict[value] += 1
        frequencies.append( freq_dict )
    return frequencies

def compute_vk( frequencies, state_range ):
    v_k = {x: [0] * 6 for x in state_range}
    for frequency_dict in frequencies:
        for x in state_range:
            count = frequency_dict[x]
            k = min( count, 5 )
            v_k[x][k] += 1
    return v_k

def produce_p_values( v_k, J ):
    pi_k = [[0.5, 0.25, 0.125, 0.0625, 0.0312, 0.0312],
          [0.75, 0.0625, 0.0469, 0.0352, 0.0264, 0.0791],
          [0.8333, 0.0278, 0.0231, 0.0193, 0.0161, 0.0804],
          [0.875, 0.0156, 0.0137, 0.012, 0.0105, 0.0733]]
    
    state_range = [1, 2, 3, 4]
    
    pi_k_dict = {state: values for state, values in zip(state_range, pi_k)}
    chi_squared_dict = {}
    p_values = []
    for state, observed_freqs in v_k.items():
        chi_squared = 0.0
        for k, obs in enumerate(observed_freqs):
            exp = J * pi_k_dict[abs(state)][k]
            if exp != 0:
                chi_squared += ((obs - exp) ** 2) / exp
        chi_squared_dict[state] = chi_squared
        p_values.append( ss.gammaincc( 5. / 2., chi_squared_dict[state] / 2. ) )
    return p_values
    
def random_excursions_test( input ):
    n = len( input )
    state_range = list( range( -4, 0 ) ) + list( range( 1, 5 ) )
    if n < 1000000: return 0
    values = list( )
    for i in range( n ):
        values.append( 2 * int( input[i] ) - 1 )

    s_i = list( )   
    s_i_sum = 0.
    for value in values:
        s_i_sum += value
        s_i.append( s_i_sum )
    s_i_prim = [0.] + s_i + [0.]  # add zeros before and after set S
    
    cycles = construct_cycles( s_i_prim )
    if cycles == 0: 
        return [0.] * len( state_range )
    frequencies = compute_frequencies( cycles, state_range )
    v_k = compute_vk( frequencies, state_range )
    p_values = produce_p_values( v_k, len( cycles ) )
    return p_values
