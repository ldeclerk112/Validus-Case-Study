import numpy as np

def factor_optimisation(K, S_0, nu, periods, interest_rate, learning_rate, N, min_error, asset_no):

    S_j = np.zeros((N, asset_no))

    S_j[0,:] = S_0[:]

    error = np.zeros((N,asset_no))
    asset_no = np.zeros((N, asset_no))

    for m in range(0, asset_no):
        for i in range(0, N):

            value[i,m] = value_europe_call_option(K[m], S_j[i,m], nu[m], periods[m], interest_rate)

            error[i,m] = (S_j[i,m] - value[i,m])/(abs(value[i,m]))

            if (i > 0) and ((error[i] - error[i-1])/error[i-1]) > min_error:

                nu[m] = nu[m] + learning_rate * error[i,m]

            elif (i > 0):

                break

        if i == N-1:

            print("Minimum Error not reached for asset: ", m)

        else:

            print("Minimum Error reached for asset: ", m)

    return nu


