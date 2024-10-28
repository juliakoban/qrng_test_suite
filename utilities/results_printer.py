HEADER_LABELS   = ["0.1", "0.2", "0.3", "0.4", "0.5", "0.6", "0.7", "0.8", "0.9", "1.0", "P-VALUE(CHI^2)", "P-VALUE(KS)", "PROPORTION", "STATISTICAL TEST       "]
TEST_LABEL_LENGTH = 24
HEADER_LENGTH   = 129
OUTPUT_FILE     = "./output/finalResults.txt"
TEST_SUITE_NAME = "DIEHARDEST TEST SUITE"
TITLE_CENTERING = 54

def header( ):
    header_output = "\n" + "-" * TITLE_CENTERING + TEST_SUITE_NAME +  "-" * TITLE_CENTERING + 2 * "\n" 
    header_output += "-" * HEADER_LENGTH + "\n" 
    header_output += " ".join(f"{label:>2} |" for label in HEADER_LABELS) + "\n" 
    header_output += "-" * HEADER_LENGTH + "\n"  
    return header_output

def test_result( hist, p_value_chi, p_value_ks, proportion, test_name ):
    text_hist    = [f"{num:<3} |" for num in hist]
    output_hist  = " ".join(text_hist)
    if isinstance( proportion, float):
        final_output = f"{output_hist} {p_value_chi}       | {p_value_ks}    | {proportion:.4f}     | {test_name}"
    else: final_output = f"{output_hist} {p_value_chi}       | {p_value_ks}    | {proportion}     | {test_name}"
    final_output += " " * ( TEST_LABEL_LENGTH - len(test_name) ) + "|\n"
    final_output += "-" * HEADER_LENGTH + "\n" 
    return final_output

def write_header_to_file( ):
    with open( OUTPUT_FILE, 'w' ) as f:
        f.write( header() )
    
def write_to_file( hist, p_value_chi, p_value_ks, proportion, test_name ):
    with open( OUTPUT_FILE, 'a' ) as f:
        f.write( test_result( hist, p_value_chi, p_value_ks, proportion, test_name ) )