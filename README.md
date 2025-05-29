# Black-Scholes-model-Implied-Volatility
Black–Scholes option pricing model &amp; Implied Volatility calculation for call options 
Web application link: #### https://black-scholes-model-and-implied-volatility.streamlit.app/
## Overview

This program calculates theoretical prices for Call and Put options using the Black-Scholes model. It also plots option prices against time to expiration, helping visualize time decay (theta) and other key pricing factors.

The tool is useful for:
Estimating fair option prices.
Analyzing how volatility and time decay affect premiums.
Developing trading strategies based on mispricings.


The program requires these inputs:

S – Current underlying asset price.\
K – Strike price.\
T – Time to expiration (in years).\
r – Risk-free interest rate.\
σ (sigma) – Underlying asset volatility.\

Compare the calculated price with the market price to identify:
Overpriced options (market price > theoretical price) → Potential short opportunity.
Underpriced options (market price < theoretical price) → Potential long opportunity.


The price vs. time graph helps understand how quickly an option loses value. This is critical for:
Option sellers → Faster decay = more profitable.
Option buyers → Must account for accelerating value loss near expiration.

## Recommended Resources
[Black-Scholes Model Explained (Investopedia)](https://www.investopedia.com/terms/b/blackscholes.asp)
