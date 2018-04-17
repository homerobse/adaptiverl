import pickle

def saveCtLbdEpisodeVar(p,v,r,e,variable, path, var_name):
   '''
   DEFINITION: saves a variable
   INPUTS:
   p: probability
   v: volatility
   r: learning rate
   e: episode
   variable: variable to be saved
   var_name: name of the variable as used when it was saved (check if the file was saved with the same name as the variable)
   '''
   f= open(path+var_name+'_p'+str(p)+'_v'+str(v)+'_r'+str(r)+'_e'+str(e)+'.dat','w')
   pickle.dump(variable,f)
   f.close()

def saveEpisodeVar(p,v,e,variable, path, var_name):
   '''
   DEFINITION: saves a variable
   INPUTS:
   p: probability
   v: volatility
   e: episode
   variable: variable to be saved
   var_name: name of the variable as used when it was saved (check if the file was saved with the same name as the variable)
   '''
   f= open(path+var_name+'_p'+str(p)+'_v'+str(v)+'_e'+str(e)+'.dat','w')
   pickle.dump(variable,f)
   f.close()
   
def saveArrangeVar(p,v,variable, path, var_name):
   '''
   DEFINITION: saves a variable
   INPUTS:
   p: probability
   v: volatility
#TODO: put number of trials as a parameter. It is possible to have different number of trials for same (p,v)   
   variable: variable to be saved
   var_name: name of the variable as used when it was saved (check if the file was saved with the same name as the variable)
   '''
   f= open(path+var_name+'_p'+str(p)+'_v'+str(v)+'.dat','w')
   pickle.dump(variable,f)
   f.close()

def saveVar(variable, path,var_name):
   '''
   DEFINITION: saves a variable
   INPUTS:
   variable: variable to be saved
   var_name: name of the variable as used when it was saved (check if the file was saved with the same name as the variable)
   '''
   f= open(path+var_name+'.dat','w')
   pickle.dump(variable,f)
   f.close()
   
def saveAllVars(path, variables):
   '''
   DEFINITION: saves all given variables
   INPUTS:
   variables: dictionary with variable names as keys and  variable to be saved
   '''
   for name,var in variables.items():
      saveVar(var, path, name)
   
def saveAllEpisodeVariables(p,v,e, path, variables):
   '''
   DEFINITION: saves all given variables
   INPUTS:
   p: probability
   v: volatility
   e: episode
   variables: dictionary with variable names as keys and  variable to be saved
   '''
   for name,var in variables.items():
      saveEpisodeVar(p,v,e,var,path,name)
      
def loadCtLbdEpisodeVar(p,v,lr,e,path,var_name):
   '''
   DEFINITION: loads a episode variable from a simulation of given constant learning rate
   INPUTS:
   p: probability
   v: volatility
   lr: learning rate
   e: episode
   var_name: name of the variable as used when it was saved (check if the file was saved with the same name as the variable)
   '''
   f= open(path+var_name+'_p'+str(p)+'_v'+str(v)+'_r'+str(lr)+'_e'+str(e)+'.dat','r')
   var=pickle.load(f)
   f.close()
   return var

def loadEpisodeVar(p,v,e,path,var_name):
   '''
   DEFINITION: loads a epsiode variable
   INPUTS:
   p: probability
   v: volatility
   e: episode
   var_name: name of the variable as used when it was saved (check if the file was saved with the same name as the variable)
   '''
   f= open(path+var_name+'_p'+str(p)+'_v'+str(v)+'_e'+str(e)+'.dat','r')
   var=pickle.load(f)
   f.close()
   return var
def loadArrangeVar(p,v,path,var_name):
   '''
   DEFINITION: loads a variable
   INPUTS:
   p: probability
   v: volatility
   var_name: name of the variable as used when it was saved (check if the file was saved with the same name as the variable)
   '''
   f= open(path+var_name+'_p'+str(p)+'_v'+str(v)+'.dat','r')
   var=pickle.load(f)
   f.close()
   return var
def loadVar(path,var_name):
   '''
   DEFINITION: loads a variable
   INPUTS:
   var_name: name of the variable as used when it was saved (check if the file was saved with the same name as the variable)
   '''
   f= open(path+var_name+'.dat','r')
   var=pickle.load(f)
   f.close()
   return var