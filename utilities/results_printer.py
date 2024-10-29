HEADER_LABELS   = ["0.1", "0.2", "0.3", "0.4", "0.5", "0.6", "0.7", "0.8", "0.9", "1.0", "P-VALUE(CHI^2)", "P-VALUE(KS)", "PROPORTION", "STATISTICAL TEST       "]
TEST_LABEL_LENGTH = 24
HEADER_LENGTH   = 129
TITLE_CENTERING = 54

OUTPUT_FILE_NIST = "./output/nistResults.txt"
OUTPUT_FILE_DIEHARD = "./output/diehardResults.txt"

TEST_SUITE_NAME = "DIEHARDEST TEST SUITE"
HEADER_DESCRIPTION_NIST = "PART 1: NIST TESTS RESULTS FOR FILE "
HEADER_DESCRIPTION_DIEHARD = "PART 2: DIEHARD TESTS RESULTS FOR FILE "

def generate_header( ):
    header_output  = "-" * HEADER_LENGTH + "\n" 
    header_output += " " * TITLE_CENTERING + TEST_SUITE_NAME +  " " * TITLE_CENTERING + "\n" 
    header_output += "-" * HEADER_LENGTH + "\n" 
    return header_output

def generate_nist_header( file ):
    header_output  = HEADER_DESCRIPTION_NIST + file + "\n"  
    header_output += "-" * HEADER_LENGTH + "\n" 
    header_output += " ".join(f"{label:>2} |" for label in HEADER_LABELS) + "\n" 
    header_output += "-" * HEADER_LENGTH + "\n" 
    return header_output

def generate_diehard_header( file ):
    header_output  = HEADER_DESCRIPTION_DIEHARD + file + "\n"  
    header_output += "-" * HEADER_LENGTH + "\n" 
    return header_output

def nist_test_result( hist, p_value_chi, p_value_ks, proportion, test_name ):
    text_hist = [f"{num:<3} |" for num in hist]
    output_hist = " ".join(text_hist)
    if isinstance( proportion, float):
        final_output = f"{output_hist} {p_value_chi}       | {p_value_ks}    | {proportion:.4f}     | {test_name}"
    else: final_output = f"{output_hist} {p_value_chi}       | {p_value_ks}    | {proportion}     | {test_name}"
    final_output += " " * ( TEST_LABEL_LENGTH - len(test_name) ) + "|\n"
    final_output += "-" * HEADER_LENGTH + "\n" 
    return final_output

def diehard_test_result( p_value_ks, test_name ):
    final_output = f"{p_value_ks} | { test_name } |"
    return final_output

def write_nist_header( file ):
    with open( OUTPUT_FILE_NIST, 'w' ) as f:
        f.write( generate_header( ) )
        f.write( generate_nist_header( file ) )

def write_diehard_header( file ):
    with open( OUTPUT_FILE_DIEHARD, 'w' ) as f:
        f.write( generate_header( ) )
        f.write( generate_diehard_header( file ) )
    
def write_nist_result( hist, p_value_chi, p_value_ks, proportion, test_name ):
    with open( OUTPUT_FILE_NIST, 'a' ) as f:
        f.write( nist_test_result( hist, p_value_chi, p_value_ks, proportion, test_name ) )
        
def write_diehard_result( p_value_ks, test_name ):
    with open( OUTPUT_FILE_DIEHARD, 'a' ) as f:
        f.write( diehard_test_result( p_value_ks, test_name ) )