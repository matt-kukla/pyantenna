'''
wave.py

Provides some wave related functions. 
'''

import numpy as np

# Wavevector given cordinates of propagation direction and wavelength
def wavevector(th, ph, l):
    return list(map(lambda u: 2*pi/u,
    (np.sin(th)*np.cos(ph), np.sin(th)*np.sin(ph), np.cos(th))))
