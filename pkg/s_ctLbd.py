'''
Run the simulation using the environment and the learning agent
'''
from numpy import ones, array
from pkg.plots import figureAgent2, showQValues2, show3dQValues2
from pkg.agent import Agent
from pkg.simulationCtLbd import simulateCtLbd
from matplotlib.pyplot import show
from numpy.ma.core import mean

#Initial conditions
x0=array([.5])
#lRates = [0.01,0.11,0.21,0.31,0.41,0.51, 0.61, 0.71, 0.81, 0.91]
lRates = [0.11]
#prob = array([.55, .65, .75, .85, .95])
#vol = array([.001,.005])
prob = array([.85])
vol = array([.001])
pPolicy = 'greedy'
nTrials = 5000 # number of trials of an episode
nEpisodes = 1  # number of episodes
saveOutput = False
path='data/ctLbd/'
fixSeed=False

(agent, environment) = simulateCtLbd(vol, prob, x0, lRates, nTrials, nEpisodes, pPolicy, fixSeed, saveOutput, path)
#import pdb
figureAgent2(environment, agent)

print mean(agent.err**2)

show()
#pdb.set_trace()