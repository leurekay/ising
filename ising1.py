# -*- coding: utf-8 -*-
"""
Created on Thu Sep 15 11:58:05 2016

@author: aa
"""
from __future__ import division
import random,math,time
import numpy as np
import matplotlib.pyplot as plt
import pylab
start_time=time.time()
L=16

Low=0.3
High=5.7
Interval=0.1
mc_steps=8000
T_list=np.arange(Low,High,Interval)
T_list=np.append(T_list,np.arange(1.85,2.65,0.04))
T_list.sort()
steps=mc_steps*L**2

        
m_list=[]
Cv_list=[]
for T in T_list:
    conf=np.random.choice((-1,1),(L,L))
    M_total=0    
    E2_total=0
    E_total=0
    M=0
    E=0
    for i in range(L):
        for j in range(L):
            M=M+conf[i][j]
            E=E-0.5*conf[i][j]*sum([conf[(i-1)%L][j],conf[(i+1)%L][j],conf[i][(j-1)%L],conf[i][(j+1)%L]])

    sample=0
    for step in range(steps):    
        s=[random.randrange(L),random.randrange(L)]
        x,y=s
        neighbour=[conf[(x-1)%L][y],conf[(x+1)%L][y],conf[x][(y-1)%L],conf[x][(y+1)%L]]
        delta_E=2*conf[x][y]*sum(neighbour)
        rho=min(1,math.exp(-delta_E/T))
        if random.random()<rho:
            conf[x][y]=-1*conf[x][y]
            M=M+2*conf[x][y]
            E=E+delta_E
        if step>steps/2 and step%(L)==0:
        #if step>steps/2 :
            sample=sample+1
            M_total=M_total+M
            E_total=E_total+E
            E2_total=E2_total+E**2
    m=M_total/sample/L**2
    E_mean=E_total/sample
    E2_mean=E2_total/sample
    Cv=(E2_mean-E_mean**2)/T**2/L**4
    m_list.append(abs(m))  
    Cv_list.append(Cv)
maxCv=max(Cv_list)
Cv_list=[i*1.2/maxCv for i in Cv_list]
run_time=time.time()-start_time    
#plt.figure(figsize=(20,10))
#plt.plot(T_list,m_list,color="blue",linewidth=1.5,label="mc")    
#plt.savefig('L=%d'%L)
pylab.title('$%i\\times%i$ lattice' % (L, L))
pylab.xlabel('$T$', fontsize=16)
pylab.ylabel('$<|M|>/N$', fontsize=16)
pylab.plot(T_list, m_list, 'bo-', clip_on=False)
pylab.plot(T_list, Cv_list, 'ro-', clip_on=False)
pylab.ylim(0.0, 1.2)
pylab.savefig('L=%i,mc_steps=%d,Low=%.1f,High=%.1f,Interval=%.1f,time=%.2f.png' % (L,mc_steps,Low,High,Interval,run_time))
print run_time
