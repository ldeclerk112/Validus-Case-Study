

def american_call_value(S_0, S_t, K, periods, interest_rate):

    value_next_period = value_europe_call_option(K, S_0, nu, periods, interest_rate)

    Z_t = S_t - K

    value_option = max(Z_t, value_next_period)