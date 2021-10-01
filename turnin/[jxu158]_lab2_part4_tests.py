# Array of tests to run (in order)
# Each test contains
#   description - 
#   steps - A list of steps to perform, each step can have
#       inputs - A list of tuples for the inputs to apply at that step
#       *time - The time (in ms) to wait before continuing to the next step 
#           and before checking expected values for this step. The time should be a multiple of
#           the period of the system
#       *iterations - The number of clock ticks to wait (periods)
#       expected - The expected value at the end of this step (after the "time" has elapsed.) 
#           If this value is incorrect the test will fail early before completing.
#       * only one of these should be used
#   expected - The expected output (as a list of tuples) at the end of this test
# An example set of tests is shown below. It is important to note that these tests are not "unit tests" in 
# that they are not ran in isolation but in the order shown and the state of the device is not reset or 
# altered in between executions (unless preconditions are used).
tests = [ {'description': 'All 0 => PORTD: 0x00',
    'steps': [ {'inputs': [('PINA',0x00), ('PINB', 0x00), ('PINC', 0x00)], 'iterations': 5 } ],
    'expected': [('PORTD',0x00)],
    },
    {'description': 'all non-zero, even weigth dist => PORTD: 0x2C',
    'steps': [ {'inputs': [('PINA',0x1E), ('PINB', 0x1E), ('PINC', 0x1E)], 'iterations': 5 } ],
    'expected': [('PORTD',0x2C)],
    },
    {'description': 'all non-zero, un-even weigth dist => PORTD: 0x30',
    'steps': [ {'inputs': [('PINA',0x64), ('PINB', 0x00), ('PINC', 0x00)], 'iterations': 5 } ],
    'expected': [('PORTD',0x30)],
    },
    {'description': 'all non-zero, over weight limit => PORTD: 0x25',
    'steps': [ {'inputs': [('PINA',0x32), ('PINB', 0x32), ('PINC', 0x32)], 'iterations': 5 } ],
    'expected': [('PORTD',0x25)],
    },
    {'description': 'over weight limit and unblanced => PORTD: 0x27',
    'steps': [ {'inputs': [('PINA',0x64), ('PINB', 0x32), ('PINC', 0x00)], 'iterations': 5 } ],
    'expected': [('PORTD',0x27)],
    },
    {'description': 'gradescope test 1',
    'steps': [ {'inputs': [('PINA',64), ('PINB', 64), ('PINC', 64)], 'iterations': 5 } ],
    'expected': [('PORTD',0x31)],
    },
    {'description': 'gradescope test 2',
    'steps': [ {'inputs': [('PINA',0), ('PINB', 35), ('PINC', 85)], 'iterations': 5 } ],
    'expected': [('PORTD',0x1E)],
    },
    {'description': 'gradescope test 3',
    'steps': [ {'inputs': [('PINA',0), ('PINB', 56), ('PINC', 85)], 'iterations': 5 } ],
    'expected': [('PORTD',0x23)],
    },
    ]

# Optionally you can add a set of "watch" variables these need to be global or static and may need
# to be scoped at the function level (for static variables) if there are naming conflicts. The 
# variables listed here will display everytime you hit (and stop at) a breakpoint
watch = ['PORTD']
