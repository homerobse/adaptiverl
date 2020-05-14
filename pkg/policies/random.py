from numpy import random

class Random(object):
   '''
   Random policy - maximum exploration
   '''
   t=0
   def __init__(self, agent):
      self.agent = agent
   
   def decide(self):
      action = random.randint(0,self.agent.nLr) #upper bound is exclusive
      self.t+=1
      return action