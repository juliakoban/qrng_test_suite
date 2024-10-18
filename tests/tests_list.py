from .nist.frequency import frequency_test
from .nist.block_frequency import block_frequency_test
from .nist.runs import runs_test

from .diehard.birthday import birthday

nist_tests = [ frequency_test, block_frequency_test , runs_test ]
diehard_tests = [ birthday ]