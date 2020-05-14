from pkg.fileHandler import loadEpisodeVar, saveAllVars, loadVar, loadArrangeVar
from numpy.core.fromnumeric import mean, std, around
from numpy import array
import numpy as np
from pkg.utils import dualPrint, showProgress
import time
from datetime import datetime

path = 'data/varredura_0-4/'
outputPath = path + 'statistics/'
begin = time.time()

prob = array([.55, .65, .75, .85, .95])
vol = array([0, .005, .01, .05])
nEpisodes = 10

lbdMean = np.zeros((len(prob), len(vol), nEpisodes))
lbdStd = np.zeros((len(prob), len(vol), nEpisodes))
meanSquareError = np.zeros((len(prob), len(vol), nEpisodes))
rightEstimate = np.zeros((len(prob), len(vol), nEpisodes))
rightPrediction = np.zeros((len(prob), len(vol),nEpisodes))
rewardedTrials = np.zeros((len(prob), len(vol), nEpisodes))
totalIter = len(prob)*len(vol)*nEpisodes

n=1 #iterations counter
now = datetime.now()
print 'Simulation started. Date:', now.strftime("%Y-%m-%d %H:%M:%S")
for v in xrange(len(vol)):
   for p in xrange(len(prob)):
      environment = loadArrangeVar(prob[p], vol[v], path,'environment')
      for e in xrange(nEpisodes):
         lrAgent = loadEpisodeVar(prob[p], vol[v], e, path,'lrAgent')
         agent = loadEpisodeVar(prob[p], vol[v], e, path,'agent')
         chosenLRs = [lrAgent.lbd[a] for a in lrAgent.actions]
         lbdMean[p][v][e] = mean(chosenLRs)
         lbdStd[p][v][e] = std(chosenLRs) #low std indicates the algorithm chooses a optimum learning rate - convergence
         meanSquareError[p][v][e] = mean(lrAgent.r)
         rightEstimate[p][v][e] = np.sum(around(agent.x[1:]) == around(environment.history)) / environment.history.size*100 #x has a shape of nTrials+1 and history of nTrials. That is because after the last trial the agent learns the value of x for the next
         rightPrediction[p][v][e] = np.sum(around(agent.x[0:-1]) == around(environment.history)) / environment.history.size*100
         rewardedTrials[p][v][e] = float(np.sum(agent.r))/agent.x.size*100 #Calculates how often the agent was rewarded within the episode
         
         showProgress(totalIter, n, time.time(), begin)
         n+=1


variables = {'lbdStd':lbdStd,'lbdMean':lbdMean, 'meanSquareError':meanSquareError, 'rightEstimate':rightEstimate, 'rightPrediction':rightPrediction, 'rewardedTrials': rewardedTrials}
#variables = {'rewardedTrials': rewardedTrials, 'rightPrediction':rightPrediction}
saveAllVars(outputPath,variables)
print 'Calculation finished at',datetime.now().strftime("%Y-%m-%d %H:%M"),'in %.1f' %(time.time()-begin), 'seconds.'