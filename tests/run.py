from .frequency import frequency
from utilities.results import write_to_file

def run_tests( input ):
    hist, p_value_chi, p_value_ks, test_name = frequency( input )
    write_to_file( hist, p_value_chi, p_value_ks, test_name )
   