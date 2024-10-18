import numpy as np
from .results_printer import write_to_file, write_header_to_file
from utilities.statistics import *

def run_nist_test( input, test_function ):
    bins = np.arange(0., 1.1, 0.1)
    
    p_values = [test_function( input[i] ) for i in range( 0, len( input ) )]
    hist, _ = np.histogram(p_values, bins = bins)
    
    passed_tests = 0
    for p_value in p_values:
        if p_value > 0.01: passed_tests += 1
            
    expected_freq = len( p_values ) / ( len( bins ) - 1 )
    expected = [expected_freq] * ( len( bins ) - 1 )
    
    p_value_chi = chi_squared( hist, expected )
    p_value_ks  = Kolmogorov_Smirnov( p_values )
    proportion  = passed_tests / len( input )
    return [hist, p_value_chi, p_value_ks, proportion]
    
def run_nist_tests( tests, input ):
    write_header_to_file( )
    for test in tests:
        hist, p_value_chi, p_value_ks, proportion = run_nist_test( input, test )
        test_name = str( test ).split()[1].replace( "_test" , "")
        write_to_file( hist, p_value_chi, p_value_ks, proportion, test_name )
   