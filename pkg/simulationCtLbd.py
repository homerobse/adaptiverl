'''
Run the simulation using the environment and the learning agent
'''
from numpy import array
from numpy.random import seed
from pkg.environment import PRL
from pkg.predictionAgent import PredictionAgent
import time
import datetime
from pkg.utils import showProgress
from pkg.fileHandler import saveArrangeVar, saveCtLbdEpisodeVar

def simulateCtLbd (vol,prob,x0,lRates,nTrials,nEpisodes,pPolicy,fixSeed=True,saveOutput=False,path=None):
   '''
   DEFINITION: runs the simulation for the agent with constant learning rate
   INPUTS:
   vol: list of volatilities to run
   prob: list of probabilities to run
   x0: initial value for the first agent
   lRates: learning rates simulated
   nTrials: number of trials
   nEpisodes: number of episodes
   pPolicy: string with the name of the policy for the prediction agent (first agent)
   lrLearner: string with the kind of algorithm is to be used to learn the Q-values
   lrPolicy: string with the name of the policy for the learning rate agent (second agent)
   fixSeed: (boolean) if true, the seed of the random number generation is fixed and the results can be repeated
   saveOutput: (boolean) if true the output will be saved at the path
   path: path for saving simulation data
   '''

   now = datetime.datetime.now()
   n=1 #iterations counter
   begin = time.time()
   
   print 'Simulation started. Date:', now.strftime("%Y-%m-%d %H:%M")
   if saveOutput:
      name = path + 'output' + now.strftime("%Y-%m-%d_%H-%M") + '.txt'
      f=open(name, 'w')
      print >>f,'Simulation started. Date:', now.strftime("%Y-%m-%d %H:%M")
      print >>f, 'Constant lambda'
      print >>f, 'Run parameters:'
      print >>f, 'x0 =',x0
      print >>f, 'lRates =',lRates
      print >>f, 'vol =', vol
      print >>f, 'prob = ', prob
      print >>f, 'nTrials = ', nTrials
      print >>f, 'nEpisodes = ', nEpisodes
   
   totalIter = nTrials*nEpisodes*len(prob)*len(vol)*len(lRates)
   
   for v in vol:
      for p in prob:
         for lr in lRates:
            for e in xrange(nEpisodes):
               seed(e)  # this makes episode e have the same pseudo-random numbers for different p and v
               
               #set up
               environment = PRL(p,v)
               agent = PredictionAgent(pPolicy,environment,lrLearner=None,lr=array([lr]),x0=x0)
               
               #execution
               for t in xrange(nTrials):
                  agent.play() #use this if you want to run with constant learning rate
                  showProgress(totalIter, n, time.time(), begin)
                  n+=1
               
               #saving information for this episode
               if saveOutput: saveCtLbdEpisodeVar(p,v,lr,e,agent,path,'agent')
            if saveOutput: saveArrangeVar(p, v, environment, path, 'environment')
               
            print 'Finished',nEpisodes,'episodes of',nTrials,'trials for vol =',v,'prob =', p, 'lr=',lr, 'at time %.1f'%(time.time()-begin)
            if saveOutput: print >>f,'Finished',nEpisodes,'episodes of',nTrials,'trials for vol =',v,'prob =', p, 'at time %.1f'%(time.time()-begin)
   print 'Calculation finished in %.1f' %(time.time()-begin), 'seconds.'
   if saveOutput: print >>f,'Calculation finished in %.1f' %(time.time()-begin),'seconds.'
   
   if saveOutput: f.close()
   
   return (agent, environment)