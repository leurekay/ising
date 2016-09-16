# -*- coding: utf-8 -*-
"""
Created on Fri Sep 16 19:51:27 2016
H=-j*∑ Si*Sj + ∑ h*Si
@author: aa
"""
from __future__ import division
import random,math,time
import numpy as np
import matplotlib.pyplot as plt
import pylab
start_time=time.time()
L=8

conf=[random.choice((-1,1)) for i in range(L)]
s=







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