from numpy.core.fromnumeric import mean, shape
from pkg.fileHandler import loadVar
from numpy.ma.core import array
import numpy as np
import matplotlib.pyplot as plt
import pdb
from matplotlib.ticker import FormatStrFormatter
from numpy.core.numeric import zeros, arange
from mpl_toolkits.mplot3d import Axes3D
from numpy.lib.function_base import meshgrid
from matplotlib import cm
from matplotlib.pyplot import show

def generateMOQCtLbd(prob,vol,lbds,MOQ,function, path,name):
   '''
   DEFINITION: generates a table with the mean values of the lambdas in the episode
   INPUTS:
   prob: probabilities
   vol: volatilities
   lbds: learning rates
   MOQ: 4-d (p,v,r,e) array with the MOQ for each episode and learning rate used
   name: name of the resulting file with the table
   '''
   with open(path+name+'.txt', 'w') as f:
      print >>f,'v,p,',
      for lr in lbd:
         print >>f, '%.2f,' %lr,
      print >>f,'\n',
      for v in xrange(len(vol)):
         print >>f,'%.3f' %vol[v],
         for p in xrange(len(prob)):
            print >>f,',%.2f,' %prob[p],
            for r in  xrange(len(lbds)):
               print >>f,'%.3f,' %function(MOQ[p,v,r,:]),
            print >>f,'\n',
def plotTable(v,vol,prob,lbds,MOQ,name):
   """
   DEFINITION:
   v: index in volatility array
   vol: volatility array. Contains simulated volatilities.
   name: name of the plot. 
   """
   np,_,nr,_=shape(MOQ)
   MOQshape = zeros((np,nr))
   for p in xrange(len(prob)):
      for r in xrange(len(lbds)):
         MOQshape [p,r]= mean(MOQ[p,v,r,:])
   fig = plt.figure()
   ax = fig.gca(projection='3d')
   X = lbds
   Y = prob
   X, Y = meshgrid(X, Y)
   Z=MOQshape
   plt.xlabel('Lambdas')
   plt.ylabel('Probabilities')
   plt.title(name+' for fixed lambdas - v='+str(vol[v]))
   surf = ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap=cm.jet,linewidth=0, antialiased=False)
   ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))
   fig.colorbar(surf, shrink=0.5, aspect=5)

def generateTableofStatistics(prob,vol,statistic,function, path,name):
   '''
   DEFINITION: generates a table with the mean values of the lambdas in the episode
   INPUTS:
   prob: probabilities
   vol: volatilities
   statistic: 3-d (p,v,e) array with the mean lambda for each episode
   name: name of text file where the table will be written
   '''
   with open(path+name+'.txt', 'w') as f:
      print >>f,'v\p,',
      for p in prob:
         print >>f, '%.2f,' %p,
      print >>f,'\n',
      for v in xrange(len(vol)):
         print >>f,'%.3f,' %vol[v],
         for p in xrange(len(prob)):
            print >>f,'%.3f,' %function(statistic[p,v,:]),
         print >>f,'\n',

#POLICIES
path = 'data/varredura_0-4/statistics/'
lbdMean = loadVar(path,'lbdMean')
lbdStd = loadVar(path,'lbdStd')
meanSquareError = loadVar(path,'meanSquareError')
rightEstimate = loadVar (path,'rightEstimate')
rightPrediction = loadVar (path,'rightPrediction')
rewardedTrials = loadVar (path,'rewardedTrials')
prob = array([.55,.65,.75,.85,.95])
vol = array([0,.005,.01,.05])
lbd = [0.01,0.11,0.21,0.31,0.41,0.51, 0.61, 0.71, 0.81, 0.91]

generateTableofStatistics(prob, vol, lbdMean, mean, path, 'tableLbdMean')
generateTableofStatistics(prob, vol, lbdMean, std, path, 'tableLbdStdMean-consistence')
generateTableofStatistics(prob, vol, lbdStd, mean,path, 'tableLbdMeanStd-convergence') 
#generateTableofStatistics(prob, vol, meanSquareError,mean, path, 'tableMeanSquareError')
#generateTableofStatistics(prob, vol, rewardedTrials, mean,path,'tableRewardedTrials')
generateTableofStatistics(prob, vol, rightEstimate, mean,path,'tableRightEstimate')
#generateTableofStatistics(prob, vol, rightPrediction,mean, path,'tableRightPrediction')

##CONSTANT LAMBDA
#lbd = [0.01,0.11,0.21,0.31,0.41,0.51, 0.61, 0.71, 0.81, 0.91]
#prob = array([.55,.65,.75,.85,.95])
#vol = array([0, .001,.005,.01,.05,.1])
#path='data/ctLbd/statistics/'
#meanSquareError = loadVar(path,'meanSquareError')
#rightEstimate = loadVar (path,'rightEstimate')
##rightPrediction = loadVar (path,'rightPrediction')
##rewardedTrials = loadVar (path,'rewardedTrials')
#
#plotTable(4,vol, prob, lbd, rightEstimate,'Right Estimate')
#plotTable(4,vol, prob, lbd, meanSquareError, 'Mean Square Error')
#show()
##generateMOQCtLbd(prob, vol, lbd,meanSquareError,mean,path,'tableMeanSquareError')
##generateMOQCtLbd(prob, vol, lbd,rewardedTrials, mean,path,'tableRewardedTrials')
##generateMOQCtLbd(prob, vol, lbd,rightEstimate,mean,path,'tableRightEstimate')
##generateMOQCtLbd(prob, vol, lbd,rightPrediction, mean,path,'tableRightPrediction')