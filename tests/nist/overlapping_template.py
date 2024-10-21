import math

# The focus of the Overlapping Template Matching test is the number of occurrences of pre-specified target
# strings. Both this test and the Non-overlapping Template Matching test use an m-bit
# window to search for a specific m-bit pattern. As with the previous test, if the pattern is not found,
# the window slides one bit position. The difference between this test and the other test is that
# when the pattern is found, the window slides only one bit before resuming the search. 

def overlapping_template_test( input ):
    return 0