import numpy as np

"""
    Computes the sigmoid function of z
    input of z
    output of g
"""

def sigmoid_function (z):
    g = 1/(1+np.exp(-z))
    return g