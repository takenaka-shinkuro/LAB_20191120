# -*- coding: utf-8 -*-
"""
Created on Tue Nov 19 11:20:38 2019

@author: -
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint


def func_LN(N, t, r, N_max, N_min, m, n):
    dNdt = r*N*(1-(N/N_max)**m)*(1-(N_min/N)**n)
    return dNdt

r = 1
N0 = 2
t = np.arange(0, 8, 0.01)
N_max = 7
N_min = 1
m = 5
n = 0.3

N = odeint(func_LN, N0, t, args=(r,N_max,N_min,m,n,))

plt.plot(t, N, label= 'exp')
plt.legend()
plt.show()