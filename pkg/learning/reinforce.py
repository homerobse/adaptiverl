from numpy.core.numeric import array
class Reinforce(object):
   '''
   Reinforcement learning updates 
   '''
   def __init__(self, agent):
      self.agent = agent
      pass
      
   def learn(self):
      newValue = array([self.agent.x[-1]]) #new values are initiated equal to the most recent values (last in the array)
      newValue[-1][self.agent.actions[-1]] = newValue[-1][self.agent.actions[-1]] + self.agent.lr[-1] * self.agent.err[-1]
      return newValue