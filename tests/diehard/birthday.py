import numpy as np
from collections import Counter
from scipy.stats import poisson, chisquare, kstest
import matplotlib.pyplot as plt

TEST_NAME = "BIRTHDAY"
NBITS     = 24
DAYS      = 2**NBITS
BIRTHDAYS = 2**9
LAMBDA    = BIRTHDAYS**3 / ( 4*DAYS ) # mean of the Poisson distribution; the expected number of repeated spacings in the list of birthdays

def simulate_birthdays( sequence, bit_shift ):
    birthdays = []
    for i in range( 0, len( sequence ) - 32 + 1, 8 ):  # Move 8 bits at a time for 32 bits
        if i + 32 > len( sequence ) or len( birthdays ) >= BIRTHDAYS:  # Avoid going out of bounds
            break
        value = int( sequence[i:i + 32], 2 )  # Convert bits to an integer
        masked_value = ( value >> bit_shift ) & ( ( 1 << 24 ) - 1 )  # Extract 24 bits
        birthdays.append( masked_value )
    birthdays.sort( )
    return birthdays

def count_repeated_spacings( birthdays ):
    spacings = np.abs( np.diff( np.concatenate( ( [birthdays[-1] - DAYS], birthdays ) ) ) ) # circular spacings
    # count the frequency of each spacing
    spacing_counts = Counter( spacings )
    # count how many spacings occur more than once
    j = sum( count > 1 for count in spacing_counts.values( ) )
    return j

def run_simulation( sequences ):
    max_j_value = 7
    p_values = []
    expected = np.round( [100 * poisson.pmf( i, LAMBDA ) for i in range( max_j_value )] ).astype( int )
    for bit_shift in range( 9 ):
        j_values = []
        for sequence in sequences:
            birthdays = simulate_birthdays( sequence, bit_shift )
            j = count_repeated_spacings( birthdays )
            j_values.append( j )
            
        j_counts = Counter( j_values )  
          
        counts_array = np.zeros( max_j_value, dtype = int )
        for k in range( max_j_value ):
            counts_array[k] = j_counts.get( k, 0 )
            
        p_value_chi = chisquare( counts_array, expected ).pvalue
        p_values.append( p_value_chi )
        
    p_value_ks = kstest( p_values, "uniform" ).pvalue
    #print( f"{p_value_ks:.6f}" )