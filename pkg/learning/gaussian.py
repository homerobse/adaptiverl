from numpy.core.numeric import zeros, array
from numpy.ma.core import exp, sqrt
from scipy.constants.constants import pi
import pdb

class Gaussian(object):
   '''
   Gaussian policy updates 
   '''
   def __init__(self, agent):
      self.agent = agent
      self.center = 0
      self.sgm = 1.2
      self.n = self.agent.nLr
      self.update = zeros(self.n)
      self.a = 1#/(self.sgm*sqrt(2*pi))
      
   def learn(self):
      self.center = float(self.agent.actions[-1])
      self.a = sum([exp(-1/2*((i-self.center)/self.sgm)**2) for i in xrange(self.n)])
      for i in xrange(self.n):
         self.update[i]= 1/self.a*exp(-1/2*((i-self.center)/self.sgm)**2)
      newValue = self.agent.x[-1] + self.update*self.agent.lr[-1] * self.agent.err[-1]
      return array([newValue])