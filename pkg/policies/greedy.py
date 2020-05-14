class Greedy(object):
   '''
   Greedy policy
   '''
   
   
   def __init__(self, agent):
      '''
      Constructor
      '''
      self.agent = agent
      pass
   
   def decide(self):
      if self.agent.x[-1]>.5:
         return 0
      else:
         return 1