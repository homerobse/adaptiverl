from pkg.fileHandler import saveAllVars, loadArrangeVar,loadCtLbdEpisodeVar
from numpy.core.fromnumeric import mean, around
from numpy import array
import numpy as np
from pkg.utils import showProgress
import time
import pdb

path = 'data/ctLbd/'
outputPath = path + 'statistics/'
begin = time.time()

prob = array([.55, .65, .75, .85, .95])
vol = array([0.0,0.001,0.005,0.01,0.05,0.1])
lRates = [0.01,0.11,0.21,0.31,0.41,0.51, 0.61, 0.71, 0.81, 0.91]
nEpisodes = 50

meanSquareError = np.zeros((len(prob), len(vol),len(lRates), nEpisodes))
rightEstimate = np.zeros((len(prob), len(vol), len(lRates),nEpisodes))
rightPrediction = np.zeros((len(prob), len(vol), len(lRates),nEpisodes))
rewardedTrials = np.zeros((len(prob), len(vol), len(lRates),nEpisodes))
totalIter = len(prob)*len(vol)*nEpisodes*len(lRates)
n=1 #iterations counter
for v in xrange(len(vol)):
   for p in xrange(len(prob)):
      environment = loadArrangeVar(prob[p], vol[v], path,'environment')
      for r in xrange(len(lRates)):
         for e in xrange(nEpisodes):
            agent = loadCtLbdEpisodeVar(prob[p], vol[v], lRates[r],e, path,'agent')
            meanSquareError[p][v][r][e] = mean(agent.err**2)
            rightEstimate[p][v][r][e] = np.sum(around(agent.x[1:]) == around(environment.history)) / float(environment.history.size)*100 #x has a shape of nTrials+1 and history of nTrials. That is because after the last trial the agent learns the value of x for the next
            rightPrediction[p][v][r][e] = np.sum(around(agent.x[0:-1]) == around(environment.history)) / float(environment.history.size)*100
            rewardedTrials[p][v][r][e] = float(np.sum(agent.r))/agent.x.size*100 #Calculates how often the agent was rewarded within the episode

            showProgress(totalIter, n, time.time(), begin)
            n+=1

variables = {'meanSquareError':meanSquareError, 'rightEstimate':rightEstimate, 'rewardedTrials': rewardedTrials, 'rightPrediction':rightPrediction}
saveAllVars(outputPath,variables)
print 'Calculation finished in ', (time.time()-begin), 'seconds.'