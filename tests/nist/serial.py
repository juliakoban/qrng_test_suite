
# The focus of this test is the frequency of all possible overlapping m-bit patterns across the entire
# sequence. The purpose of this test is to determine whether the number of occurrences of the 2m m-bit
# overlapping patterns is approximately the same as would be expected for a random sequence. Random
# sequences have uniformity; that is, every m-bit pattern has the same chance of appearing as every other
# m-bit pattern. Note that for m = 1, the Serial test is equivalent to the Frequency test. 

def serial_test( input ):
    return 0