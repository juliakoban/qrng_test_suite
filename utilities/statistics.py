from scipy.stats import chisquare, kstest

def chi_squared( p_values, bins, hist):
    expected_freq = len( p_values ) / ( len( bins ) - 1 )
    expected = [expected_freq] * (len(bins) - 1)
    p_value = chisquare(f_obs = hist, f_exp = expected).pvalue
    return p_value

def  Kolmogorov_Smirnov( p_values ):
    p_value = kstest( p_values, 'uniform').pvalue
    return p_value