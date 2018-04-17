from numpy import array
from numpy.core.numeric import ones
from numpy.lib.index_tricks import r_
from agent import Agent
from pkg.learning.reinforce import Reinforce
from pkg.learning.gaussian import Gaussian

class RateAgent(Agent):
   """Class responsible for varying the learning rate of the predictionAgent"""
   
   def inicLearner(self, learner):
      if (learner == 'reinforce'):
         learner = Reinforce(self)
      elif (learner == 'gaussian'):
         learner = Gaussian(self)
      return learner
   
   def __init__(self,policy,learner,predictionAgent,lr=array([.11]),x0=array([25*ones(10)]),gamma=.995):
      super(RateAgent,self).__init__(policy,predictionAgent,lr=lr,x0=x0)
      self.gamma = gamma
      self.learner = self.inicLearner(learner)
      
   def learn(self):
      #calculate error
      self.err = r_[self.err,self.r[-1]+self.gamma*min(self.x[-1])-self.x[-1][self.actions[-1]]]

      #update value
#      self.x = r_[self.x,[self.x[-1]]] #create new line in the evolution of the function with the same values as the last
#      self.x[-1][self.actions[-1]] = self.x[-1][self.actions[-1]] + self.lr[-1]*self.err[-1]
      self.x = r_[self.x,self.learner.learn()]