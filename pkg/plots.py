from matplotlib.pyplot import title, xlabel, ylim, plot, legend,\
   colorbar, figure, subplot, ylabel, pcolor, axis, errorbar
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from pkg.fileHandler import loadEpisodeVar, loadArrangeVar
from numpy.ma.core import shape, mean, std
from numpy.core.numeric import arange, zeros, array
import numpy as np
from matplotlib.ticker import FormatStrFormatter
from pkg.agent import Agent
from numpy.lib.index_tricks import r_
from pkg.utils import genStat
import pdb
   
def showPredictions(prob, vol, epis,path):
   '''Temporal evolution of agent's prediction in comparison with the real value'''
   environment = loadArrangeVar(prob, vol, path,'environment')
   agent = loadEpisodeVar(prob, vol, epis, path,'agent')
   
   title('Environment and Predictions - p='+str(prob)+' v='+str(vol)+' episode '+str(epis))
   xlabel('Trials')
   ylim(-.05,1.05)
   plot(environment.history,label="probability")
   plot(agent.x, label="value")
   legend()
   
def showAgentDynamics(prob, vol, epis, path):
   '''Plot agent's errors, rewards and learning rates from saved data'''
   agent = loadEpisodeVar(prob, vol, epis, path,'agent')
   xlabel('Trials')
   plot(agent.err,'.',label="error")
   plot(agent.r, 'o',label="reward")
   plot(agent.lr,'x',label="LR", markersize=5)
   ylim(ymax=1.1)
   legend()
   
def figureAgent(prob, vol, epis,path):
   '''Shows agent-environment main dynamics: Actual probability and agent predictions,errors and rewards'''
   figure()
   subplot(2,1,1)
   showPredictions(prob, vol, epis,path)
   subplot(2,1,2)
   showAgentDynamics(prob, vol, epis,path)
def showPredictions2(environment,agent):
   '''Temporal evolution of agent's prediction in comparison with the real value'''   
   prob = environment.prob
   vol = environment.vol
   title('Environment and Predictions - p='+str(prob)+' v='+str(vol))
   xlabel('Trials')
   ylim(-.05,1.05)
   plot(environment.history,label="probability")
   plot(agent.x, label="value")
   legend()
def showAgentDynamics2(agent):
   '''Plot agent's errors, rewards and learning rates from data in memory (agent variable)'''
   xlabel('Trials')
   plot(agent.err,'.',label="error")
   plot(agent.r, 'o',label="reward")
   plot(agent.lr,'x',label="LR", markersize=5)
   ylim(ymax=1.1)
   legend()
def figureAgent2(environment,agent):
   '''Shows agent-environment main dynamics: Actual probability and agent predictions,errors and rewards'''
   figure()
   subplot(2,1,1)
   showPredictions2(environment,agent)
   subplot(2,1,2)
   showAgentDynamics2(agent)
def showQValues2(lrAgent,spFactor=1):
   '''Colorplot for the QValues'''
   figure()
   title('Q-values over the trials')
   dlbd=lrAgent.lbd[1]-lrAgent.lbd[0]
   ny,nx = shape(lrAgent.x)
   last = lrAgent.lbd[-1]+dlbd
   X = r_[lrAgent.lbd,last] #watch out with this limit here "last" (pcolor doesn't show the last column)
   Y = arange(ny/spFactor+1)
   
   sample= array([i%spFactor==0 for i in xrange(ny)])
   Z = lrAgent.x[sample]
   pcolor(X,Y,Z)
   colorbar()
   axis([lrAgent.lbd[0],last,0,ny/spFactor+1])
   xlabel('Learning rates')
   ylabel('Trials') 
def show3dQValues2(lrAgent):
   '''3d Colorplot for the QValues'''
   fig = figure()
   ny,nx = shape(lrAgent.x)
   ax = fig.gca(projection='3d')
   X = Agent.lbd
   Y = np.arange(ny)[::-1]
   X, Y = np.meshgrid(X, Y)
   Z=lrAgent.x
   xlabel('x')
   ylabel('y')
   title('Q-values over the trials')
   surf = ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap=cm.jet,linewidth=0, antialiased=False)
   ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))
   fig.colorbar(surf, shrink=0.5, aspect=5)
def showActions(p, v, epis, path):
   '''Plot agent actions'''
   figure()
   agent = loadEpisodeVar(p, v, epis, path,'agent')
   plot(agent.actions,'.', label="action")
   title('Actions')
   ylim(-.05,1.05)
   xlabel('Trials')   
def showQValues(p, v, epis, path):
   '''Colorplot for the QValues'''
   lrAgent = loadEpisodeVar(p, v, epis, path, 'lrAgent')
   figure()
   title('Q-values over the trials')
   
   dlbd=lrAgent.lbd[1]-lrAgent.lbd[0]
   ny,nx = shape(lrAgent.x)
   last = lrAgent.lbd[-1]+dlbd
   X = r_[lrAgent.lbd,last] #watch out with this limit here "last" (pcolor doesn't show the last column)
   Y = arange(ny+1)
   
   Z = lrAgent.x
   pcolor(X,Y,Z)
   colorbar()
   axis([lrAgent.lbd[0],last,0,ny+1])
   xlabel('Learning rates')
   ylabel('Trials')  
   #you can also use imshow: #cax = imshow(lrAgent.x, aspect='auto', interpolation='none')

def showAverageQValues(p, v, nEpisodes, path):
   '''Colorplot for the average QValues'''
   lrAgent = loadEpisodeVar(p, v, 0, path, 'lrAgent')
   ny,nx = shape(lrAgent.x)
   avgValues=zeros((ny,nx))
   for  e in xrange(nEpisodes):
      if e!=0: lrAgent = loadEpisodeVar(p, v, e, path, 'lrAgent')
      avgValues += lrAgent.x
#      pdb.set_trace()
   avgValues = avgValues/nEpisodes
   figure()
   title('Average Q-values over the trials- p='+str(p)+' v='+str(v))
   
   dlbd=lrAgent.lbd[1]-lrAgent.lbd[0]
   last = lrAgent.lbd[-1]+dlbd
   X = r_[lrAgent.lbd,last] #watch out with this limit here "last" (pcolor doesn't show the last column)
   Y = arange(ny+1)
   Z = avgValues
   pcolor(X,Y,Z)
   colorbar()
   axis([lrAgent.lbd[0],last,0,ny+1])
   xlabel('Learning rates')
   ylabel('Trials')  

def showAverageQTrace(p, v, nEpisodes,path):
   '''
   DEFINITION: plot the Q-values in the last trial averaged over all episodes
   INPUTS:
   p: probability
   v: volatility
   nEpisodes: number of episodes
   path: location of the file
   '''
   figure()
   for e in xrange(nEpisodes):
      lrAgent = loadEpisodeVar(p, v, e, path, 'lrAgent')
      if e==0: allQs=array([lrAgent.x[-1]])
      else: allQs=r_[allQs,[lrAgent.x[-1]]]
   meanQ=genStat(allQs, mean)
   stdQ=genStat(allQs,std)
   errorbar(lrAgent.lbd,meanQ,yerr=stdQ,fmt='o')
   title('Averaged Q-values - p='+str(p)+' v='+str(v))
   xlabel('Learning rates')
def showQTrace2(lrAgent):
   '''
   DEFINITION: plot Q-values in the last trial of the episode
   '''
   figure()
   plot(lrAgent.lbd,lrAgent.x[-1],'o')
   title('Q-values')
   xlabel('Learning rates')
def showQTrace(p,v,e,path):
   '''
   DEFINITION: plot Q-values in the last trial of the episode
   INPUTS:
   p: probability
   v: volatility
   e: episode
   path: location of the file
   '''
   lrAgent = loadEpisodeVar(p, v, e, path, 'lrAgent')
   figure()
   plot(lrAgent.x[-1],'o')
   title('Q-values - p='+str(p)+' v='+str(v))
   xlabel('Learning rates')