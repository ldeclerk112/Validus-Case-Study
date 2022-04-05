from math import log, factorial

def value_europe_call_option(K, S_0, nu, periods, interest_rate):

    up = (1+nu)
    down = (1-nu)

    n_hat = (log(K/(S_0 * down ** periods)))/(log(up/down)) + 1

    sum1 = 0
    sum2 = 0

    for n1 in range(0, periods):
        q_hat = ((up * down)/(1 + interest_rate) ** (periods)) ** (periods - n1)
        sum1 += (factorial(periods))/(factorial(periods - n1) * factorial(n1)) * \
                q_hat ** n1 *(1 - q_hat) ** (periods-n1)


    for n2 in range(0, periods):
        q = (1 + interest_rate - down)/(up * down)
        sum2 += (factorial(periods))/(factorial(periods - n1) * factorial(n1)) * \
                q_hat ** n2 * (1 - q) ** (periods - n2)

    pre_fact_1 = S_0
    pre_fact_2 = K/((1 + interest_rate) ** (periods))


    return pre_fact_1 * sum1 - pre_fact_2 * sum2
