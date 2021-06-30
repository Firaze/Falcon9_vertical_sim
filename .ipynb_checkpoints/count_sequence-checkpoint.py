#
#
#

from phidias.Types  import *
from phidias.Main import *
from phidias.Lib import *

class ball(Procedure): pass
class sequence_counter(SingletonBelief): pass
class expected_color(SingletonBelief): pass

class next_color(Procedure): pass

def_vars('Color','Count')

ball(Color) / expected_color(Color) >> \
	[ show_line('Ball in sequence, color = ', Color), next_color(Color) ]
ball(Color)  >> \
	[ show_line('Ball out of sequence, color = ', Color), +expected_color('red') ]

next_color('red') >> [ +expected_color('white') ]
next_color('white') >> [ +expected_color('green') ]
next_color('green') / sequence_counter(Count) >> \
	[ "Count = Count + 1", +sequence_counter(Count), +expected_color('red'), 
	   show_line('Sequence got') ]

PHIDIAS.assert_belief(sequence_counter(0))
PHIDIAS.assert_belief(expected_color('red'))

PHIDIAS.run()
PHIDIAS.shell(globals())

