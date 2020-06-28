'''
radiate.py

Various functions related to wave radiation/propagation.  
'''
import numpy as np
from scipy import integrate, constants, pi

# Radiation patterns (in spherical coordinates) are passed to functions as lambdas

# [directivity, error]
def directivity_err(rad):

    return list(map(lambda u: (4 * pi)/u, integrate.dblquad(
    lambda x,y:((np.absolute(rad(x,y))**2)*np.sin(x)),0, 2*pi,
    lambda x:0, lambda x:pi)))

# Directivity without error
def directivity(rad):
    return directivity_err(rad)[0]


# [total radiated power (watts), error] 
def trp_err(rad):

    return integrate.dblquad(lambda x, y: rad(x,y)*np.sin(x), 
    0, 2*pi, lambda x:0,lambda x:pi) 

# Total radiated power (watts) without error
def trp(rad):
    return trp_err(rad)[0] 
