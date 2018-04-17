from numpy.core.numeric import arange,zeros
from numpy.ma.core import argmin
from numpy import random

class Tabu(object):
   '''
   Tabu policy
   '''
   def __init__(self, agent):
      self.agent = agent
      self.lbdAllowed = zeros(self.agent.nLr,int)
      self.ngbhdSize = 2
      self.banThreshold=8
      self.banNumber=20
      self.sigma = 0.25 ** 2
      self.neighborhood = arange(2*self.ngbhdSize+1)
   
   @staticmethod
   def mapAllowedToAll(x,lbdAllowed):
      """map x index (of xAllowed) to index of the original x vector"""
      i=0
      while i<=x:
         if lbdAllowed[i]>1:
            x+=1
         i+=1
      return x
   def mapNeighborhood(self,ngbhdAllowed):
      ngbhd = zeros(len(ngbhdAllowed),int)
      for i in arange(len(ngbhdAllowed)):
         ngbhd[i] = self.mapAllowedToAll(ngbhdAllowed[i],self.lbdAllowed)
      return ngbhd
            
   def mapIndex(self, a_opt, a_pert, ngbhdSize):
      """Maps index of chosen lbd in neighborhood array to index of the array of all lbds"""
      a2 = max(0, a_opt - ngbhdSize) + a_pert #map a_pert index to index of x_allowed
      return self.mapAllowedToAll(a2,self.lbdAllowed)
   
   def decide(self):
      if len(self.agent.actions)==0: #first action
         action = random.randint(0,self.agent.nLr) #upper bound is exclusive
         self.neighborhood = arange(max(0, action-self.ngbhdSize),min(self.agent.nLr, action + self.ngbhdSize+1))
      else:
         self.lbdAllowed = self.lbdAllowed - 1
         self.lbdAllowed[self.lbdAllowed<0]=0
         if self.threshold()>self.banThreshold:
            self.lbdAllowed = zeros(self.agent.nLr,int) #only one region can be banned at a time
            self.lbdAllowed[self.neighborhood] = self.banNumber
         x_allowed = self.agent.x[-1][self.lbdAllowed<1]
         a_opt = argmin(x_allowed)
         ngbhdAllowed = arange(max(0, a_opt-self.ngbhdSize),min(len(x_allowed),a_opt+self.ngbhdSize+1)) #ngbhdAllowed has indexes related with the smaller vector x_allowed
         noise = random.randn(len(ngbhdAllowed))*self.sigma
         lrValues = x_allowed[ngbhdAllowed]
         a_pert = argmin(lrValues + noise)
         
         action = self.mapIndex(a_opt, a_pert,self.ngbhdSize)
         self.neighborhood = self.mapNeighborhood(ngbhdAllowed)#neighborhood has indexes related with the original self.x vector
      return action
   
   def threshold(self):
      return self.agent.r[-1]/abs(self.agent.gamma*min(self.agent.x[-1])-self.agent.x[-1][self.agent.actions[-1]])    