from matplotlib.pyplot import boxplot, show,figure, xlabel, ylabel, title, xlim,\
   plot
from pkg.fileHandler import loadVar
from numpy.core.numeric import array, arange
import pylab

def boxplotProbabilities(prob,nv, lbdMean):
   '''
   DEFINITION: makes a boxplot of the mean (within an episode) learning rates for different probabilities and a given volatility  
   INPUTS:
   prob: probabilities array
   nv: given volatility (you have to know what the indexes in lbdMean mean in terms of volatility e.g. 1 would mean volatility .005 if the simulation was done with vol=[.001 .005])
   TODO - think of a way of how not to depend on knowing beforehand of how the simulation was done 
   lbdMean: array with the mean chosen learning rate in an episode. lbdMean is indexed [p,v,e]
   '''
   l=[]
   for p in xrange(len(prob)):
      l.append(lbdMean[p,nv,:])
   figure()
   boxplot(l)
   pylab.xticks(range(1,len(prob)+1), prob)
   xlabel('Reward probability')
   ylabel('Average learning rate lambda')
   title('Average learning rates distributions for v='+str(vol[nv]))
   plot(arange(0,5),'x')

def boxplotVolatilities(np,vol, lbdMean):
   '''
   DEFINITION: makes a boxplot of the mean (within an episode) learning rates for different probabilities and a given volatility  
   INPUTS:
   prob: probabilities array
   nv: given volatility (you have to know what the indexes in lbdMean mean in terms of volatility e.g. 1 would mean volatility .005 if the simulation was done with vol=[.001 .005])
   TODO - think of a way of how not to depend on knowing beforehand of how the simulation was done 
   lbdMean: array with the mean chosen learning rate in an episode. lbdMean is indexed [p,v,e]
   '''
   l=[]
   for v in xrange(len(vol)):
      l.append(lbdMean[np,v,:])
   figure()
   boxplot(l)
   pylab.xticks(range(1,len(vol)+1), vol)
   xlabel('Volatility')
   ylabel('Average learning rate lambda')
   title('Average learning rates distributions for p='+str(prob[np]))
   
prob = array([.55, .65, .75, .85, .95])
vol = array([0,.001,.005,.01,.05])
path = 'data/tabuHigh/statistics/'
lbdMean = loadVar(path,'lbdMean')

#for i in xrange(len(prob)):
#   boxplotVolatilities(i, vol, lbdMean)
#for i in xrange(len(vol)):
#   boxplotProbabilities(prob, 3, lbdMean)

boxplotVolatilities(3, vol, lbdMean)
show()