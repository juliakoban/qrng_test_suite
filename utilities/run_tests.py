import numpy as np
from .results_printer import write_to_file, write_header_to_file
from scipy.stats import chisquare, kstest

def calculate_stats( hist, p_values, bins ):
    expected_freq = len( p_values ) / ( len( bins ) - 1 )
    expected = [expected_freq] * ( len( bins ) - 1 )
    p_value_chi = round( chisquare( hist, expected ).pvalue, 6 )
    p_value_ks  = round( kstest( p_values, "uniform" ).pvalue, 6 )
    passed_tests = np.sum( np.array( p_values ) > 0.01 )
    proportion = passed_tests / len( p_values)  if p_values else 0
    return p_value_chi, p_value_ks, proportion

def run_nist_test( input, test_function ):
    bins = np.arange(0., 1.1, 0.1)
    results = []
    
    p_values_all = list( map( test_function, input ) )
    p_values_list = [list( filter( lambda x: x != 0, p_values ) ) for p_values in zip( *p_values_all )]
    
    for p_values in p_values_list:
        
        if not p_values: 
            hist = np.zeros( len( bins ) - 1, dtype = int )
            results.append( [hist, "----    ", "----    ", "----  "] )
            continue
    
        hist = np.histogram( p_values, bins = bins )[0]
        p_value_chi, p_value_ks, proportion = calculate_stats( hist, p_values, bins )
        
        if len( p_values ) < len( p_values_all ): results.append( [hist, "----    ", "----    ", proportion] )
        else: results.append( [hist, p_value_chi, p_value_ks, proportion] )
    return results
    
def run_nist_tests( tests, input ):
    write_header_to_file( )
    
    for test in tests:
        test_name = str( test ).split()[1].replace( "_test" , "" )
        results = run_nist_test( input, test )
        
        for result in results:
            hist, p_value_chi, p_value_ks, proportion = result
            write_to_file( hist, p_value_chi, p_value_ks, proportion, test_name )
   