from numpy import random

class Random20(object):
   '''
   Random policy - maximum exploration
   '''
   t=0
   def __init__(self, agent):
      self.agent = agent
   
   def decide(self):
      if self.t%20==0:
         action = random.randint(0,self.agent.nLr) #upper bound is exclusive
      else:
         action = self.agent.actions[-1]
      self.t+=1
      return action