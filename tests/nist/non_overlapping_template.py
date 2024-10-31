import math
import scipy.special as ss
import numpy as np

# The focus of this test is the number of occurrences of pre-specified target strings. The purpose of this
# test is to detect generators that produce too many occurrences of a given non-periodic (aperiodic) pattern.
# For this test and for the Overlapping Template Matching test of Section 2.8, an m-bit window is used to
# search for a specific m-bit pattern. If the pattern is not found, the window slides one bit position. If the
# pattern is found, the window is reset to the bit after the found pattern, and the search resumes. 

NUM_OF_BLOCKS = 8 # < 100
TEMPLATES_FILE = "./templates/templates_m_9.txt"
SINGLE_TEMPLATE_FILE = "./templates/template_1"

def load_templates_from_file(file_path):
    templates = []
    with open(file_path, 'r') as file:
        for line in file:
            template = list(map(int, line.strip().split()))
            templates.append(template)  
    return templates

def generate_blocks( input, N, M ):
    input_array = np.frombuffer( input.encode( 'utf-8' ), dtype = np.uint8 ) - ord( "0" )  
    blocks = input_array.reshape( N, M )  
    return blocks.tolist()  

def count_template_occurrences( blocks, M,  template ):
    W = []
    m = len( template ) # m should be 9 or 10 for best results 
    for block in blocks:
        position = 0
        count = 0
        while position <= ( M - m ):
            if block[position:( position + m )] == template:
                position += m
                count += 1
            else:
                position += 1
        W.append( count )         
    return W

def calculate_statistics( W, M, N, template ):
    m = len( template )
    miu = ( M - m + 1 ) / ( 2**m )
    sigma = M * ( ( 1.0 / float( 2**m ) ) - ( float( ( 2 * m ) - 1 ) / float( 2**( 2 * m ) ) ) )
    chi_squared = sum( ( ( W[i] - miu )**2 ) / sigma for i in range( N ) )
    p_value = ss.gammaincc( N / 2.0, chi_squared / 2.0 ) 
    return p_value

def non_overlaping_template_test( input, N = NUM_OF_BLOCKS ):
    p_values = []
    n = len( input )
    if n < 1000:
        return [0.]
    
    templates = load_templates_from_file( SINGLE_TEMPLATE_FILE ) 
    M = math.floor( n / N ) # block length, M > 0.01 * N
    blocks = generate_blocks( input, N, M )
    
    for template in templates:
        W = count_template_occurrences( blocks, M, template )        
        p_value = calculate_statistics( W, M, N, template )
        p_values.append( p_value )
    return p_values