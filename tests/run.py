from .frequency import frequency

def run_tests( input ):
    p_value = frequency( input )
    print( f"p_value: { p_value } " )
    if p_value < 0.01: print( f"Sequence is non random." )
    else: print( f"Sequence is accepted as random." )