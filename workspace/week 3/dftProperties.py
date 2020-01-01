#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 29 13:08:23 2019

@author: curlymorphic
"""

import matplotlib.pyplot as plt
import numpy as np
from scipy.signal import triang
from scipy.fftpack import fft

x = triang(15)
fftbuffer = np.zeros(15)
fftbuffer[:8] = x[7:]
fftbuffer[8:] = x[:7]
X = fft(fftbuffer)
mX = abs(X)
pX = np.angle(X)
