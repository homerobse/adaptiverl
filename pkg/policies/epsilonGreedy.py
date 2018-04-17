from numpy import random

class EpsilonGreedy(object):
   '''
   Epsilon Greedy policy
   Specific for 1st learner
   '''
   
   def __init__(self, agent, epsilon):
      '''
      Constructor
      '''
      self.epsilon = epsilon
      self.agent = agent
      pass
   
   def decide(self):
      if random.random()<= self.epsilon:
         return random.randint(0,2)
      else:
         if self.agent.x[-1]>.5:
            return 0
         else:
            return 1