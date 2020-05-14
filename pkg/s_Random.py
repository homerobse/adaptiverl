'''
Run the simulation using the environment and the learning agent
'''
from numpy import ones, array
from pkg.simulation import simulate, simulateMore
from pkg.agent import Agent
from pkg.plots import figureAgent2, showQValues2, showQTrace2
from matplotlib.pyplot import show

#Initial conditions
x0=array([.5])
Q0=array([10*ones(len(Agent.lbd))])
lr=array([.1])
gamma = .995
#prob = array([.55,.65,.75,.85,.95])
#vol = array([0,.005,.01,.05])
prob = array([.85])
vol = array([.05])
pPolicy = 'greedy'
lrPolicy = 'random20'
lrLearner = 'reinforce'
nTrials = 30000 # number of trials of an episode
nEpisodes = 1   # number of episodes
saveOutput =False
path='data/random/'
fixSeed=False

(agent,lrAgent,environment) = simulate(vol, prob, x0, Q0, lr, gamma, nTrials, nEpisodes, pPolicy, lrLearner, lrPolicy, fixSeed,saveOutput, path)
#(agent,lrAgent,environment) = simulateMore(agent, lrAgent, environment, nTrials)
figureAgent2(environment, agent)
showQValues2(lrAgent,5)
showQTrace2(lrAgent)
#show3dQValues2(lrAgent)
show()