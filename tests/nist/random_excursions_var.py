
# The focus of this test is the total number of times that a particular state is visited (i.e., occurs) in a
# cumulative sum random walk. The purpose of this test is to detect deviations from the expected number
# of visits to various states in the random walk. This test is actually a series of eighteen tests (and
# conclusions), one test and conclusion for each of the states: -9, -8, …, -1 and +1, +2, …, +9. 

def random_excursions_var_test( input ):
    return 0