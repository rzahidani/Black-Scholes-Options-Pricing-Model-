# Black-Scholes Formula implementation 
import numpy as np 
'''
makes it easier to reference NumPy library in my code 
offers a multidemonsional array object that allows for fast computations on arrays 
also makes numerical operations on large data sets more useful 
'''
import scipy.stats as si 
''' 
collection of statistical functions that are useful for analyzing data, 
performing hypothesis tests, and implementing statistical models. Also provides a wide range 
of statistical tools and techniques 
'''
'''
Defined Variables: 
S = Underlying Stock Price 
K = Strike Price (the price at which the option must be bold or sold at until expirationd date)
T = Time to expiration 
r = Risk-Free Rate (the theoretical rate of return on an investment with zero risk). 
vol = Volatility (statistical measure to measure how much a stock price is expected to change over time)
'''
def black_scholes(S,K,T,r, vol, option_type="call"): 
    d1 = (np.log(S/K) + (r + 0.5 * vol ** 2) * T) / (vol * np.sqrt(T))
    d2 = d1 - vol * np.sqrt(T) 

    if option_type == "call": 
        option_price = S * si.norm.cdf(d1) - K * np.exp(-r * T) * si.norm.cdf(d2) 
    elif option_type == "put": 
        option_price = K * np.exp(-r * T) * si.norm.cdf(-d2) - S * si.norm.cdf(-d1) 
    else:
        raise ValueError("Invalid option type. Choose either 'call' or 'put'.")
        # used to explicitly trigger an exception if neither "put" or "call" is selected 

    return option_price

