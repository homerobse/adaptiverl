'''
Run the simulation using the environment and the learning agent
'''
from numpy import ones, array
from pkg.plots import figureAgent2, showQValues2, show3dQValues2
from matplotlib.pyplot import show, figure, plot
from pkg.agent import Agent
from pkg.simulation import simulate

#Initial conditions
x0=array([.5])
Q0=array([40*ones(len(Agent.lbd))])
gamma = .995
prob = array([.55,.65,.75,.85,.95])
vol = array([0,.005,.01,.05])
#prob = array([.85])
#vol = array([.005])
pPolicy = 'greedy'
lrPolicy = 'dynTabu'
lrLearner = 'gaussian'
nTrials = 1000 # number of trials of an episode
nEpisodes = 10   # number of episodes
saveOutput = True
fixSeed=True

path='data/varredura_0-2/'
lr=array([.2])
(agent,lrAgent, environment) = simulate(vol, prob, x0, Q0, lr, gamma, nTrials, nEpisodes, pPolicy, lrLearner, lrPolicy, fixSeed, saveOutput, path)
path='data/varredura_0-3/'
lr=array([.3])
(agent,lrAgent, environment) = simulate(vol, prob, x0, Q0, lr, gamma, nTrials, nEpisodes, pPolicy, lrLearner, lrPolicy, fixSeed, saveOutput, path)
path='data/varredura_0-4/'
lr=array([.4])
(agent,lrAgent, environment) = simulate(vol, prob, x0, Q0, lr, gamma, nTrials, nEpisodes, pPolicy, lrLearner, lrPolicy, fixSeed, saveOutput, path)

#figureAgent2(environment, agent)
   
#showQValues2(lrAgent)
#show3dQValues2(lrAgent)
#show()