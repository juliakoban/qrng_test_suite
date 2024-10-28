import numpy as np
from .results_printer import write_to_file, write_header_to_file
from scipy.stats import chisquare, kstest

def run_nist_test( input, test_function ):
    bins = np.arange(0., 1.1, 0.1)
    results = []
    p_values_all = [test_function( input[i] ) for i in range( 0, len( input ) )]
    
    p_values_list = list( map( list, zip( *p_values_all) ) )
    
    for p_values in p_values_list:
    
        hist, _ = np.histogram( p_values, bins = bins )
    
        passed_tests = 0
        for p_value in p_values:
            if p_value > 0.01: passed_tests += 1
            
        expected_freq = len( p_values ) / ( len( bins ) - 1 )
        expected = [expected_freq] * ( len( bins ) - 1 )
    
        p_value_chi = chisquare( hist, expected ).pvalue
        p_value_ks  = kstest( p_values, "uniform" ).pvalue
        proportion  = passed_tests / len( input )
        results.append( [hist, p_value_chi, p_value_ks, proportion] )
    return results
    
def run_nist_tests( tests, input ):
    write_header_to_file( )
    for test in tests:
        results = run_nist_test( input, test )
        test_name = str( test ).split()[1].replace( "_test" , "" )
        for result in results:
            hist, p_value_chi, p_value_ks, proportion = result
            write_to_file( hist, p_value_chi, p_value_ks, proportion, test_name )
   