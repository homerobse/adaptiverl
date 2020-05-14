from pkg.plots import showAverageQTrace, showAverageQValues, showQValues,\
   showQTrace, figureAgent
from matplotlib.pyplot import show, title, xlabel, plot, legend, ylim, ylabel
from pkg.fileHandler import loadArrangeVar

path='data/varredura_0-4/'
p=.85
v=.01
nEpisodes = 10

showAverageQTrace(p, v, nEpisodes, path)
showAverageQValues(p, v, nEpisodes, path)
#showQValues(p, v, 0, path)
#showQTrace(p, v, 0, path)
figureAgent(p,v,0,path)
#showActions(p,v, e, path)

#environment = loadArrangeVar(p, v, path,'environment')
#title('Environment - p='+str(p)+', v='+str(v))
#xlabel('Trials ($t$)')
#ylabel('Probability ($x_t$)')
#ylim(-.05,1.05)
#plot(environment.history)
#legend()

show()