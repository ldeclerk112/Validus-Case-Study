import numpy as np

def factor_optimisation(price, K, S_0, nu, periods, interest_rate, learning_rate, N, min_error):

    error = np.zeros(N)

    for i in range(0, N):

        value = value_europe_call_option(K, S_0, nu, periods, interest_rate)

        error[i] = (price - value)/(abs(value))

        if (i > 0) and ((error[i] - error[i-1])/error[i-1]) > min_error:

            nu = nu + learning_rate * error

        elif (i > 0):

            break

    if i == N-1:

        print("Minimum Error not reached")

    else:

        print("Minimum Error reached")

    return nu


