from pylab import *
import numpy as np
import  matplotlib.pyplot as plt

nTrials=100
eta = [0]*nTrials
r = [0]*nTrials
x = [0]*nTrials

def learn_cte(nTrials):
   lbd = [0.01, 0.11, 0.21, 0.31, 0.41, 0.51, 0.61, 0.71, 0.81, 0.91]
   x0 = 0.5
   eta[0] = r[0] - x0
   x[0] = x0 + lbd[1]*eta[0]
   for t in range(1,nTrials):
      eta[t] = r[t] - x[t-1]
      x[t] = x[t-1] + lbd[1]*eta[t]
   

prob = [.85]#prob = [.55, 0.65, 0.75, 0.85, 0.95] #(test all these values)
vol = [0]#vol = [.001, 0.005, 0.01, 0.05] #(test all these values)
nEpisodes=1
p = [0]*nTrials
for v in range(len(vol)):
   for j in range(len(prob)):
      for t in range(nTrials): #initialize p along trials
         if t*vol[v]%2 == 0:  #if it is even
            p[t] = prob[j]
         else:
            p[t] = 1 - prob[j]
      print p
      for n in range(nEpisodes):
         for t in range(1,nTrials):
            r[t] = int(np.random.random()<p[t])
         print r
         learn_cte(nTrials)
         #Mean of chosen lambda; mean(n2);
      #Distribution of mean of chosen lambda; Distribution mean(2);
      plot(eta,'.-')
      plot(r,'o-')
      plt.show()