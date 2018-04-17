from numpy.core.numeric import array
from numpy.lib.index_tricks import r_
from numpy import random

class Environment(object):
   def sufferAction(self, opt):
      """An environment must have the function suffer action and it returns a reward"""
      pass

class PRL(Environment):
   """Probabilistic Reversal Learning PRL"""
   prob = None
   vol = None
   history = array([])
   t=0
   def __init__(self, prob=.85,vol=0):
      self.vol=vol
      self.prob = prob
   
   def sufferAction(self, opt):
      if (opt==0 and int(self.t*self.vol)%2==0) or (opt==1 and int(self.t*self.vol)%2!=0):
         reward = random.random()<self.prob
      elif (opt==1 and int(self.t*self.vol)%2==0) or (opt==0 and int(self.t*self.vol)%2!=0):
         reward = random.random()<(1-self.prob)
      self.saveHistory()
         
      self.t += 1
      return int(reward)
   
   def saveHistory(self):
      '''Save the history of probability of choice 0 being correct'''
      if(int(self.t*self.vol)%2==0):
         self.history=r_[self.history,self.prob]
      elif(int(self.t*self.vol)%2!=0):
         self.history=r_[self.history,1-self.prob]