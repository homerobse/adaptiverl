from numpy.core.numeric import array
def dualPrint(string,file_name,log=True):
   if log:
      with open(file_name, 'w') as f:
         print >>f,string
   print string
   
def showProgress(totalIter, n, now, begin):
   if n % (totalIter / 20.) == 0:
      print 'Progress of Calculation: ', float(n) / totalIter * 100, '%'+' in %.1f' %(now-begin) ,'seconds'

def genStat(mtx,function):
   '''
   DEFINITION: generates a statistic of each column in a matrix
   INPUTS:
   mtx: array
   function: function like mean or average that we want to apply in the vector
   '''
   return array([function(mtx[:,i]) for i in xrange(len(mtx[0,:]))])