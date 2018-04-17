from pkg.plots import showAverageQTrace, showAverageQValues, showQValues,\
   showQTrace, figureAgent
from matplotlib.pyplot import show

path='data/tabuHigh/'
p=.65
v=.005
nEpisodes = 30

showAverageQTrace(p,v,nEpisodes,path)
showAverageQValues(p, v, nEpisodes, path)
#showQValues(p, v, 0, path)
#showQTrace(p, v, 0, path)
#figureAgent(p,v,0,path)
#showActions(p,v, e, path)

show()