'''
Run the simulation using the environment and the learning agent
'''
from numpy import ones, array
from pkg.plots import figureAgent2, showQValues2, show3dQValues2
from pkg.agent import Agent
from pkg.simulation import simulate
from matplotlib.pyplot import show

#Initial conditions
x0=array([.5])
Q0=array([.3*ones(len(Agent.lbd))])
lr=array([.001])
gamma = .0
#prob = array([.55,.65,.75,.85,.95])
#vol = array([0,.005,.01,.05])
prob = array([.85])
vol = array([.01])
pPolicy = 'greedy'
lrPolicy = 'dynTabu'
lrLearner = 'gaussian'
nTrials = 20000 # number of trials of an episode
nEpisodes = 1   # number of episodes
saveOutput = False
path='data/dynTabu/'
fixSeed=False

(agent,lrAgent, environment) = simulate(vol, prob, x0, Q0, lr, gamma, nTrials, nEpisodes, pPolicy, lrLearner, lrPolicy, fixSeed, saveOutput, path)
import pdb
figureAgent2(environment, agent)
showQValues2(lrAgent,5)
#show3dQValues2(lrAgent)
show()
#pdb.set_trace()