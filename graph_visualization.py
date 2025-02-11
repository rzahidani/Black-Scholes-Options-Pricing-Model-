# Generates graphs for visualization 
import numpy as np 
import matplotlib.pyplot as plt 
from black_scholes_formula import black_scholes 

def plot_option_prices(S, K, T, r, vol): 
    ''' 
    What this line of  code below is saying that assuming the underlying options contract 
    is being traded around 100 points, the option price range will be set at 80, 90, 100, 
    110, and 120. Basically what this means is that the price rule dictates a 10 point interval and 40 point 
    range around the given value / median. This range is necessary because it is able to capture a 
    reasonable spectrum of potential price movements for the underlying assets (provides a view of both upside 
    and downside scenarios)
    ''' 
    # Strike price is the predetermined price at which you buy (call) or sell (put) an underlying futures contract when option is exercised 
    strike_prices = np.linspace(K *0.8, K * 1.2, 100)
    # for loop used below in the format 'for item in sequence:'
    call_prices = [black_scholes(S, K, T, r, vol, "call") for K in strike_prices]
    put_prices = [black_scholes(S, K, T, r, vol, "put") for K in strike_prices]

    plt.figure(figsize=(10,6)) # 10 inches wide by 6 inches high 
    plt.plot(strike_prices, call_prices, label="Call Option Price", color = "blue") 
    plt.plot(strike_prices, put_prices, label = "Put Option price", color = "red")
    plt.xlabel("Strike Price") 
    plt.ylabel("Option Price")
    plt.title("Black Scholes Option Pricing")
    plt.legend() 
    plt.show() 

#Example Usage: 
#plot_option_prices(100,100,1,0.05,0.02)


