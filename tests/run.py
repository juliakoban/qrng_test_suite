from .frequency import frequency

header_labels = ["0.1", "0.2", "0.3", "0.4", "0.5", "0.6", "0.7", "0.8", "0.9", "1.0", "P-VALUE(CHI^2)", "P-VALUE(KS)", "STATISTICAL TEST"]

def print_header( ):
    print("-" * 109) 
    print(" ".join(f"{label:>2} |" for label in header_labels))
    print("-" * 109) 

def run_tests( input ):
    print_header( )
    frequency( input )
    print("-" * 109) 
   