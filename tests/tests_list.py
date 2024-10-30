from .nist.frequency import frequency_test
from .nist.block_frequency import block_frequency_test
from .nist.runs import runs_test
from .nist.longest_run import longest_run_test
from .nist.matrix import binary_matrix_rank_test
from .nist.dft import DFT_test
from .nist.non_overlapping_template import non_overlaping_template_test
from .nist.overlapping_template import overlapping_template_test
from .nist.universal import universal_test
from .nist.linear_complexity import linear_complexity_test 
from .nist.serial import serial_test
from .nist.approximate_entropy import approximate_entropy_test
from .nist.cusum import cumulative_sums_test
from .nist.random_excursions import random_excursions_test
from .nist.random_excursions_var import random_excursions_var_test

nist_tests = [ 
#               frequency_test,
#               block_frequency_test,
#               runs_test,
#               longest_run_test,
#               binary_matrix_rank_test,
#               DFT_test,
               non_overlaping_template_test,
#               overlapping_template_test,
#               universal_test,
#               linear_complexity_test,
#               serial_test,
#               approximate_entropy_test,
#               cumulative_sums_test,
#               random_excursions_test,
#               random_excursions_var_test
            ]
diehard_tests = [ ]
