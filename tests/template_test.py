from itertools import product
import time
from utilities.file_loader import load_file

def generate_all_patterns(length):
    # Generate all binary strings of a given length using Cartesian product
    return [''.join(bits) for bits in product("01", repeat=length)]

def test_for_patterns_in_sequence(sequence, pattern_length):
    # Generate all possible patterns of the given length
    all_patterns = generate_all_patterns(pattern_length)
    print(len(all_patterns))
    # Find the number of times each pattern appears in the sequence
    pattern_counts = {pattern: 0 for pattern in all_patterns}
    seq_len = len(sequence)
    
    # Check all subsequences of the given length
    for i in range(seq_len - pattern_length + 1):
        subsequence = sequence[i:i + pattern_length]
        if subsequence in pattern_counts:
            pattern_counts[subsequence] += 1
    
    # Output the frequencies of each pattern found
    return pattern_counts

def is_random(sequence, pattern_length):
    pattern_counts = test_for_patterns_in_sequence(sequence, pattern_length)
    # print(pattern_counts)
    # Check if the pattern frequencies deviate from what we'd expect in a truly random sequence
    expected_frequency = len(sequence) / (2 ** pattern_length)
    
    # Threshold for detecting non-randomness (e.g., pattern appears too often)
    threshold = expected_frequency * 1.5  # You can adjust the threshold
    
    for pattern, count in pattern_counts.items():
        if count > threshold or count < expected_frequency * 0.5:
            return False 
    
    return True 

file = "./data/QNGFile.dat"
bits = 10000000
bitstreams = 1 
file_content = load_file( file, bits, bitstreams ) 
sequence = file_content

pattern_length = 27

start_time = time.time()
result = is_random(sequence, pattern_length)
end_time = time.time()
elapsed_time = end_time - start_time
print(f"elapsed_time: {elapsed_time:.6f}")

