#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Dec  7 14:01:59 2019

@author: curlymorphic
"""

import numpy as np
import matplotlib.pyplot as plt
omega = np.arange(-np.pi,np.pi,0.01)
phi = 0
A = 1
y = np.array([0])
y = np.resize(1,0)

for w in omega:
    id = np.exp(complex(0,w))
    y = np.append(y,id)
    
plt.plot(omega,y.real,label = "omega , y.real")
plt.plot(omega,y.imag, label = "omega, y.imag")
plt.plot(y.real,y.imag, label = "y.real,y.imag")
plt.title("-pi <= omega ,<= pi, exp(complex(0, omega))")
plt.legend()
plt.show()
    


