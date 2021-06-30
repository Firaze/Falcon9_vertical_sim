import pylab
import math
class modulo:
    def __init__(self,p,v,m):
        self.p=p
        self.v=v
        self.b= 17.1*10**(-6)
        self.g=9.81
        self.m=m
    def evaluate(self,f,delta_t):
        self.p=self.v*delta_t+self.p
        self.v=((f/self.m)-(self.b*self.v)/self.m-self.g)*delta_t+self.v
    def get_pos(self):
        return self.p
    def get_vel(self):
        return self.v