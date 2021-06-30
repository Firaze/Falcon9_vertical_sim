#
#
#

import math

from module import *
from controller import *


class Autopilot:

    def __init__(self):
        self.model = modulo(60*10**3,0,300*10**3)
        self.pos=PIDSat(2,0,64,1000)
        self.spd=PIDSat(5000,1000,1000,6906*10**3)
        self.z_target = 0
        self.power=0

    def run(self, delta_t):
            self.speed_target = self.pos.evaluate(-self.model.p, delta_t)
            self.v_error=self.speed_target-self.model.v
            self.power = self.spd.evaluate(self.v_error, delta_t)
            if self.power<0:
                self.power=0
            self.model.evaluate(self.power, delta_t)
