from numpy.core.numeric import zeros, arange
from numpy.ma.core import exp, sqrt
from scipy.constants.constants import pi
from matplotlib.pyplot import plot, show

center = 5.
sgm = 1.2
n = 10
update = zeros(n)
a = 1#/(sgm*sqrt(2*pi))
for i in xrange(n):
   update[i]= a*exp(-1/2*((i-center)/sgm)**2)
plot(arange(0,n),update,'o')

x= arange(0,n,.01)
update2 = zeros(len(x))
for i in xrange(len(x)):
   update2[i]= a*exp(-1/2*((x[i]-center)/sgm)**2)
plot(x,update2)
show()