
# The focus of this test is the maximal excursion (from zero) of the random walk defined by the cumulative
# sum of adjusted (-1, +1) digits in the sequence. The purpose of the test is to determine whether the
# cumulative sum of the partial sequences occurring in the tested sequence is too large or too small relative
# to the expected behavior of that cumulative sum for random sequences. This cumulative sum may be
# considered as a random walk. For a random sequence, the excursions of the random walk should be near
# zero. For certain types of non-random sequences, the excursions of this random walk from zero will be
# large. 

def cumulative_sums_test( input ):
    return 0