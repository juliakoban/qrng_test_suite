from .nist.frequency import frequency_test
from .nist.block_frequency import block_frequency_test
from .nist.runs import runs_test
from .nist.longest_run import longest_run_test
from .nist.matrix import binary_matrix_rank_test
from .nist.dft import DFT_test

nist_tests = [ frequency_test, block_frequency_test , runs_test, longest_run_test, binary_matrix_rank_test, DFT_test ]