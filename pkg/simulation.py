'''
Runs the simulation using the environment and the learning agent
'''
from numpy.random import seed
from pkg.environment import PRL
from pkg.predictionAgent import PredictionAgent
from pkg.rateAgent import RateAgent
from pkg.fileHandler import saveAllEpisodeVariables, saveArrangeVar
import time
from datetime import datetime
from pkg.utils import showProgress

def simulate (vol,prob,x0,Q0,lr,gamma,nTrials,nEpisodes,pPolicy,lrLearner,lrPolicy,fixSeed=True,saveOutput=False,path=None):
   '''
   DEFINITION: runs the simulation for the agent with changing learning rates
   INPUTS:
   prob: list of probabilities to run
   vol: list of volatilities to run
   x0: initial value for the first agent
   Q0: initial value for the second agent
   lr: learning rate for the second agent
   gamma: gamma value (second agent)
   nTrials: number of trials
   nEpisodes: number of episodes
   pPolicy: string with the name of the policy for the prediction agent (first agent)
   lrLearner: string with the kind of algorithm is to be used to learn the Q-values
   lrPolicy: string with the name of the policy for the learning rate agent (second agent)
   fixSeed: (boolean) if true, the seed of the random number generation is fixed and the results can be repeated
   saveOutput: (boolean) if true the output will be saved at the path
   path: path for saving simulation data
   '''
   now = datetime.now()
   n=1 #iterations counter
   begin = time.time()
   print 'Simulation started. Date:', now.strftime("%Y-%m-%d %H:%M:%S")
   if saveOutput:
      name = path + 'output' + now.strftime("%Y-%m-%d_%H-%M") + '.txt'
      f=open(name, 'w')
      print >>f,'Simulation started. Date:', now.strftime("%Y-%m-%d %H:%M")
      print >>f, 'Run parameters:'
      print >>f, 'x0 =',x0
      print >>f, 'Q0 =',Q0
      print >>f, 'lr =',lr
      print >>f, 'gamma =',gamma
      print >>f, 'vol =', vol
      print >>f, 'prob = ', prob
      print >>f, 'nTrials = ', nTrials
      print >>f, 'nEpisodes = ', nEpisodes
      print >>f, 'pPolicy=', pPolicy
      print >>f, 'lrPolicy = ', lrPolicy
      print >>f, 'lrLearner = ', lrLearner  
   
   totalIter = nTrials*nEpisodes*len(prob)*len(vol)
   
   for v in vol:
      for p in prob:
         for e in xrange(nEpisodes):
            if fixSeed: seed(e)  # this makes episode e have the same pseudo-random numbers for different prob and vol
            
            #set up
            environment = PRL(p,v)
            agent = PredictionAgent(pPolicy,environment,lrLearner=None,x0=x0)
            lrAgent = RateAgent(lrPolicy,lrLearner,agent,lr=lr, x0=Q0, gamma = gamma)
            agent.lrLearner = lrAgent
            
            #execution
            for t in xrange(nTrials):
               #agents[-1].play() #use this if you want to run with constant learning rate
               lrAgent.play()
               showProgress(totalIter, n, time.time(),begin)
               n+=1
            
            #saving information for this episode
            variables = {'agent':agent,'lrAgent':lrAgent}
            if saveOutput: saveAllEpisodeVariables(p,v,e,path,variables)
         if saveOutput: saveArrangeVar(p, v, environment, path, 'environment')
            
         print 'Finished',nEpisodes,'episodes of',nTrials,'trials for vol =',v,'prob =', p, 'at time %.1f' %(time.time()-begin)
         if saveOutput: print >>f,'Finished',nEpisodes,'episodes of',nTrials,'trials for vol =',v,'prob =', p, 'at time %.1f' %(time.time()-begin)
   print 'Calculation finished at',datetime.now().strftime("%Y-%m-%d %H:%M:%S"),'in %.1f' %(time.time()-begin), 'seconds.'
   if saveOutput: print >>f,'Calculation finished at',datetime.now().strftime("%Y-%m-%d %H:%M%S"),'in %.1f' %(time.time()-begin), 'seconds.'
   
   if saveOutput: f.close()
   return (agent,lrAgent, environment)

def simulateMore(agent,lrAgent,environment,nTrials):
   n=1 #iterations counter
   begin = time.time()
   #execution
   for t in xrange(nTrials):
      #agents[-1].play() #use this if you want to run with constant learning rate
      lrAgent.play()
      showProgress(nTrials, n, time.time(),begin)
      n+=1
   return (agent,lrAgent, environment)