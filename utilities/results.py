import matplotlib.pyplot as plt
import numpy as np

TEST_SUITE_NAME = "DIEHARDEST TEST SUITE"
HEADER_LABELS   = ["0.1", "0.2", "0.3", "0.4", "0.5", "0.6", "0.7", "0.8", "0.9", "1.0", "P-VALUE(CHI^2)", "P-VALUE(KS)", "STATISTICAL TEST"]
HEADER_LENGTH   = 109
OUTPUT_FILE     = "./output/finalResults.txt"

def plot_results(p_values, bins):
    plt.figure(figsize = (6, 4))
    plt.hist(p_values, bins, edgecolor = 'black', alpha = 0.7)
    plt.title('Histogram of p-values for Frequency Test')
    plt.xlabel('p-value intervals')
    plt.ylabel('frequency of p-values')
    plt.xticks(np.arange(0, 1.1, 0.1))
    plt.grid(axis='y', alpha = 0.75)
    plt.show()

def header( ):
    header_output = TEST_SUITE_NAME + "\n" 
    header_output += "-" * HEADER_LENGTH + "\n" 
    header_output += " ".join(f"{label:>2} |" for label in HEADER_LABELS) + "\n" 
    header_output += "-" * HEADER_LENGTH + "\n"  
    return header_output

def test_result( hist, p_value_chi, p_value_ks, test_name ):
    text_hist    = [f"{num:<3} |" for num in hist]
    output_hist  = " ".join(text_hist)
    final_output = f"{output_hist} {p_value_chi:.6f}       | {p_value_ks:.6f}    | {test_name}        |\n"
    final_output += "-" * HEADER_LENGTH + "\n" 
    return final_output
    
def write_to_file( hist, p_value_chi, p_value_ks, test_name ):
    with open( OUTPUT_FILE, 'w' ) as f:
        f.write( header() )
        f.write( test_result( hist, p_value_chi, p_value_ks, test_name ) )