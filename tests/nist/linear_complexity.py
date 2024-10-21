
# The focus of this test is the length of a linear feedback shift register (LFSR). The purpose of this test is to
# determine whether or not the sequence is complex enough to be considered random. Random sequences
# are characterized by longer LFSRs. An LFSR that is too short implies non-randomness. 

def linear_complexity_test( input ):
    return 0