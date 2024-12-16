import numpy as np
from .results_printer import write_nist_header, write_nist_result
from scipy.stats import chisquare, kstest
import math

def calculate_nist_stats( hist, p_values, bins ):
    expected_freq = len( p_values ) / ( len( bins ) - 1 )
    expected = [expected_freq] * ( len( bins ) - 1 ) 
    if not np.isclose( np.sum( hist ), np.sum( expected ), rtol = 1e-8 ):
        raise ValueError("Observed and expected frequencies do not match within the tolerance.")

    p_value_chi = chisquare( hist, expected ).pvalue
    p_value_ks  = kstest( p_values, "uniform" ).pvalue
    passed_tests = np.sum( np.array( p_values ) > 0.01 )
    proportion = passed_tests / len( p_values)  if p_values else 0
    
    m = len(p_values)
    alpha = 1 / m
    p_hat = 1 - alpha
    confidence_interval =  3 * math.sqrt( p_hat * ( 1 - p_hat ) / m )
    is_acceptable = proportion >= ( p_hat - confidence_interval )
    return p_value_chi, p_value_ks, proportion, is_acceptable

def run_nist_test( input, test_function ):
    bins = np.arange(0., 1.1, 0.1)
    results = []
    
    p_values_all = list( map( test_function, input ) )
    p_values_list = [list( filter( lambda x: x != 0, p_values ) ) for p_values in zip( *p_values_all )]
    
    for p_values in p_values_list:
        
        if not p_values: 
            hist = np.zeros( len( bins ) - 1, dtype = int )
            results.append( [hist, "----    ", "----    ", "----  ", ""] )
            continue
    
        hist = np.histogram( p_values, bins = bins )[0]
        try:
            p_value_chi, p_value_ks, proportion, is_acceptable = calculate_nist_stats( hist, p_values, bins )
        except ValueError:
                p_value_chi, p_value_ks, proportion, is_acceptable = "----    ", "----    ", "----  ", ""
                
        if len( p_values ) < len( p_values_all ): results.append( [hist, "----    ", "----    ", proportion, is_acceptable] )
        else: results.append( [hist, p_value_chi, p_value_ks, proportion, is_acceptable] )
    return results

def run_diehard_test( input, test_function ):
    p_value = test_function( input )
    return p_value
    
def run_nist_tests( tests, input, file ):
    write_nist_header( file )
    for test in tests:
        test_name = str( test ).split()[1].replace( "_test" , "" )
        results = run_nist_test( input, test )
        for result in results:
            hist, p_value_chi, p_value_ks, proportion, is_acceptable = result
            write_nist_result( hist, p_value_chi, p_value_ks, proportion, is_acceptable, test_name )
            
def run_diehard_tests( tests, input, file ):
    write_diehard_header( file )
    for test in tests:
        test_name = str( test ).split()[1].replace( "_test" , "" )
        p_value_ks = run_diehard_test( input, test )
        write_diehard_result( p_value_ks, test_name )
            
def run_all_tests( nist_tests, diehard_tests, input, file ):
    run_nist_tests( nist_tests, input, file )
   