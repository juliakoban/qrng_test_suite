from scipy.stats import chisquare, kstest

def chi_squared( hist, expected):
    # assesses if the observed frequencies of a categorical variable (p_values) 
    # match expected frequencies derived from a specified distribution (uniform)
    # p-value < 0.01 indicates that observed distribution is different from expected
    p_value = chisquare(f_obs = hist, f_exp = expected).pvalue
    return p_value

def Kolmogorov_Smirnov( p_values ):
    # checks if data set (p_values) matches a specific distribution (uniform)
    # p-value < 0.01 indictes that data set does not match pecific distribution
    p_value = kstest( p_values, 'uniform' ).pvalue
    return p_value