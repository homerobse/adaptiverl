from numpy.ma.core import exp, mean
from numpy.random import random

class Softmin(object):
   '''
   Softmin policy
   Specific for the 2nd learner
   '''
   def __init__(self, agent):
         '''
         Constructor
         '''
         self.agent = agent
         pass
      
   def decide(self): # not tested
      Qtmp = self.agent.x[-1] - self.agent.gamma*min(self.agent.x[-1])
      Qtmp = Qtmp/mean(Qtmp)
      
      tau=.2
      total=sum(exp(-Qtmp/tau))
      rn = random()*total
      i=0
      total=exp(-Qtmp[i]/tau)
      while rn>total:
         i+=1
         total+=exp(-Qtmp[i]/tau)
      action=i
      return action