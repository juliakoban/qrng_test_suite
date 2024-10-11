from .frequency import frequency

def run_tests( input ):
    p_value = frequency( input )
    print( f"p_value: { p_value } " )