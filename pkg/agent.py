from numpy.core.numeric import array
from pkg.policies.greedy import Greedy
from pkg.policies.tabu import Tabu
from pkg.policies.softmin import Softmin
from pkg.policies.epsilonGreedy import EpsilonGreedy
from pkg.policies.dynTabu import DynTabu
from pkg.policies.random import Random
from pkg.policies.random20 import Random20

class Agent(object):
   """Class for any learner agent"""
#   lbd = [0.01,0.06, 0.11,0.16, 0.21,0.26, 0.31,0.36, 0.41,0.46, 0.51,0.56, 0.61,0.66, 0.71,0.76, 0.81,0.86, 0.91,0.96]
   lbd = [0.01,0.11,0.21,0.31,0.41,0.51, 0.61, 0.71, 0.81, 0.91]
   

   def inicPolicy(self, policy, epsilon=None):
      if (policy == 'greedy'):
         policy = Greedy(self)
      elif (policy == 'tabu'):
         policy = Tabu(self)
      elif (policy == 'softmin'):
         policy = Softmin(self)
      elif (policy == 'epsilonGreedy'):
         policy = EpsilonGreedy(self,epsilon)
      elif (policy == 'dynTabu'):
         policy = DynTabu(self)
      elif (policy == 'random'):
         policy = Random(self)
      elif (policy == 'random20'):
         policy = Random20(self)
      return policy

   def __init__(self,policy,actionTarget,lr,x0,epsilon=None):
      self.lr = lr
      self.err = array([])
      self.r = []
      self.x = x0
      self.actions=[]
      self.actionTarget = actionTarget
      self.nLr=len(self.lbd)
      self.policy = self.inicPolicy(policy,epsilon)
      
   def play(self):
      self.decide()
      self.learn()
      
   def decide(self):
      """Function that makes a decision of which action to take over the agent's actionTarget. The reward is put in the lists of rewards""" 
      action = self.policy.decide()
      self.actions.append(action)
      
      rwd = self.act(action)
      self.r.append(rwd)
   
   def act(self,opt):
      rwd = self.actionTarget.sufferAction(opt)
      return rwd
   
   def learn(self):
      pass