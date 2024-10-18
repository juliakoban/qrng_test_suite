import numpy as np
from utilities.statistics import *
import struct
from scipy.stats import poisson

TEST_NAME = "BIRTHDAY"
DAYS      = 2**24
BIRTHDAYS = 2**9
NBITS     = 24
MAX_K     = 10
LAMBDA    = BIRTHDAYS**3 / ( 4*DAYS ) # mean of the Poisson distribution; the expected number of repeated spacings in the list of birthdays
bins = np.arange(0., 1.1, 0.1)

def extract_birthdays( file_path, bit_shift, num_samples ):
    birthdays = []
    with open( file_path, "rb" ) as f:
        while len( birthdays ) < num_samples:
            data = f.read( 4 ) # read 4 bytes (32 bits)
            if len( data ) < 4:
                break # end of file
            ( value, ) = struct.unpack( '>I', data ) # convert to 32-bit unsigned integer
            masked_value = ( value >> bit_shift ) & ( ( 1 << NBITS ) - 1 ) # keep only the 24 bits
            birthdays.append( masked_value )
    return birthdays

def calculate_repeated_spacings( birthdays ):
    sorted_birthdays = np.sort( birthdays )
    intervals = np.diff(sorted_birthdays, prepend = sorted_birthdays[0] ) # create intervals between sorted birthdays
    _, counts = np.unique( intervals, return_counts = True ) # count unique repeated intervals
    k = np.sum( counts > 1 ) # count intervals that occur more than once
    return k

def birthday_test( file_path ):
    p_values = []
    for bit_shift in range( 9 ):
        js = np.zeros( MAX_K, dtype = int )
        for _ in range( 100 ):
            birthdays = extract_birthdays( file_path, bit_shift, BIRTHDAYS )
            k = calculate_repeated_spacings( birthdays )
            if k < MAX_K:
                js[k] += 1 # increment histogram if k is less than MAX_K
        # calculate p-value using Chi-square goodness-of-fit test
        expected = [100 * poisson.pmf( i, LAMBDA ) for i in range( MAX_K )]
        chi_squared_stat, p_value = chisquare(f_obs=js, f_exp=expected)
        p_values.append(p_value)
        return p_values
        # p_value_chi = chi_squared( js, expected )
    
def birthday( input ):
    p_values    = [birthday_test( input[i] ) for i in range( 0, len( input ) )]
    p_value_ks  = Kolmogorov_Smirnov( p_values )
    # return [hist, p_value_chi, p_value_ks, TEST_NAME]