
# As with the Serial test, the focus of this test is the frequency of all possible overlapping
# m-bit patterns across the entire sequence. The purpose of the test is to compare the frequency of
# overlapping blocks of two consecutive/adjacent lengths (m and m+1) against the expected result for a
# random sequence

def approximate_entropy_test( input ):
    return 0