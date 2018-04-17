from numpy.lib.index_tricks import r_
from environment import Environment
from agent import Agent
from numpy.core.numeric import array

class PredictionAgent(Agent, Environment):
   '''Class responsible for making predictions about the environment and acting over it'''

   def __init__(self,policy,environment,lrLearner,lr=array([.11]), x0=array([.5]),epsilon=None):
      super(PredictionAgent,self).__init__(policy,environment,lr=lr,x0=x0,epsilon=epsilon)
      self.lrLearner = lrLearner

   def learn(self):
      #calculate error
      if self.actions[-1] == 0: #depending on what choice was made, it computes the errors differently (the agent knows the constraint p, 1-p of the probabilities)
         self.err = r_[self.err,self.r[-1] - self.x[-1]]
      else:
         self.err = r_[self.err,complementaryRwd(self.r[-1]) - self.x[-1]]
      #update value
      self.x = r_[self.x,self.x[-1] + self.lr[-1]*self.err[-1]]
      
   def sufferAction(self,opt):
      self.lr= r_[self.lr,self.lbd[opt]]
      self.play()
      return self.err[-1]**2
   
def complementaryRwd(x):
   """if x is 1 it returns 0. if x is 0 it returns 1"""
   return int(x!=1)