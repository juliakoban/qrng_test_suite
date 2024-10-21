
# The focus of this test is the number of cycles having exactly K visits in a cumulative sum random walk.
# The cumulative sum random walk is derived from partial sums after the (0,1) sequence is transferred to
# the appropriate (-1, +1) sequence. A cycle of a random walk consists of a sequence of steps of unit length
# taken at random that begin at and return to the origin. The purpose of this test is to determine if the
# number of visits to a particular state within a cycle deviates from what one would expect for a random
# sequence. This test is actually a series of eight tests (and conclusions), one test and conclusion for each of
# the states: -4, -3, -2, -1 and +1, +2, +3, +4. 

def random_excursions_test( input ):
    return 0