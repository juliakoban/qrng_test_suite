import math
import numpy as np
import matplotlib.pyplot as plt
from utilities.statistics import *

TEST_NAME = "FREQUENCY"
bins = np.arange(0., 1.1, 0.1)

def frequency_test( input ):
    s_n     = sum( 2 * int(bit) - 1 for bit in input )
    s_obs   = abs( s_n ) / math.sqrt( len( input ) ) 
    p_value = math.erfc( float( s_obs / math.sqrt( 2 ) ) )
    return p_value

def plot_results(p_values):
    plt.figure(figsize = (6, 4))
    plt.hist(p_values, bins, edgecolor = 'black', alpha = 0.7)
    plt.title('Histogram of p-values for Frequency Test')
    plt.xlabel('p-value intervals')
    plt.ylabel('frequency of p-values')
    plt.xticks(np.arange(0, 1.1, 0.1))
    plt.grid(axis='y', alpha = 0.75)
    plt.show()
    
def print_results( hist, p_value_chi, p_value_ks ):
    text_hist = [f"{num:<3} |" for num in hist]
    output_hist= " ".join( text_hist )
    final_output = f"{output_hist} {p_value_chi:.6f}       | {p_value_ks:.6f}    | {TEST_NAME}        |"
    print( final_output )
    #plot_results( p_values )
    
def frequency( input ):
    p_values = [frequency_test( input[i] ) for i in range( 0, len( input ) )]
    hist, _ = np.histogram(p_values, bins = bins)
    p_value_chi = chi_squared( p_values, bins, hist )
    p_value_ks  = Kolmogorov_Smirnov( p_values )
    print_results( hist, p_value_chi, p_value_ks )
