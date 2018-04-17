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
Q0=array([30*ones(len(Agent.lbd))])
lr=array([.1])
gamma = .995
#prob = array([.55,.65,.75,.85,.95])
#vol = array([0,.001,.005,.01,.05])
prob = array([.85])
vol = array([.005])
pPolicy = 'greedy'
lrPolicy = 'tabu'
lrLearner = 'reinforce'
nTrials = 1000 # number of trials of an episode
nEpisodes = 1   # number of episodes
saveOutput = False
path='data/tabuHigh/'
fixSeed=True

(agent,lrAgent, environment) = simulate(vol, prob, x0, Q0, lr, gamma, nTrials, nEpisodes, pPolicy, lrLearner, lrPolicy, fixSeed, saveOutput, path)

figureAgent2(environment, agent)
   
#showQValues2(lrAgent)
#show3dQValues2(lrAgent)
show()