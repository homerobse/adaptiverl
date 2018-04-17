from pkg.environment import PRL
from numpy.core.numeric import array
from pkg.fileHandler import saveArrangeVar, loadArrangeVar
from matplotlib.pyplot import show, plot

#TODO: define a function and put this in the file utils

path = 'data/ctLbd/'
prob = array([.55, .65, .75, .85, .95])
vol = array([0, .001, .005, .01, .05])
nTrials = 5000


for v in vol:
   for p in prob:
      env = PRL(p, v)
      for i in xrange(nTrials):
         env.sufferAction(0)
      saveArrangeVar(p, v, env, path, 'environment')

#see history
#env = loadArrangeVar(.85, .001, path, 'environment')
#
#plot(env.history)
#
#show()
#      
