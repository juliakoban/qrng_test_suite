#from tests.frequency import frequency
from .results import write_to_file, write_header_to_file
    
def run_all_tests( tests, input ):
    write_header_to_file( )
    for test in tests:
        hist, p_value_chi, p_value_ks, test_name = test( input )
        write_to_file( hist, p_value_chi, p_value_ks, test_name )
   