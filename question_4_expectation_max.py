import numpy as np
from numpy import random as rd

def max_expectation_asset_price(realisations, periods, S_0, nu):

    S_j = np.zeros((realisations,periods))

    S_j[:,0] = S_0

    for i in range(0, realisations):
        for k in range(0, periods):

            u = rd.randint(2)

            if u == 0:

                S_j[i,k+1] = (1 + nu) * S_j[i,k]

            if u == 1:

                S_j[i,k+1] = (1 - nu) * S_j[i,k]

    max_S_j = np.amax(S_j, axis=1)

    return np.mean(max_S_j)
