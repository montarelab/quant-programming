## First assignment

📌 Simulating a Stock Price Using Geometric Brownian Motion (GBM)

Geometric Brownian Motion (GBM) is widely used in financial modeling to simulate stock price movements. This exercise will introduce you to the mathematical foundation of asset price modeling while giving you hands-on experience with Python.

### 🎯 Objectives:

1. Write a Python script to simulate a stock price using GBM.
2. Assume the initial price is **$100**, with a **daily return of 0.1%** and **volatility of 2%**.
3. Simulate the price for **252 trading days** (one year).
4. Plot the simulated stock path.

### 🧠 Formula:

GBM follows the stochastic differential equation:

$S_{t+1} = S_t \times e^{(\mu - \frac{1}{2} \sigma^2) \Delta t + \sigma \sqrt{\Delta t} \cdot Z}$

Where:

- $S_t$ = stock price at time $t$
- $\mu$ = expected return (0.001 per day)
- $\sigma$ = volatility (0.02 per day)
- $Z$ = random normal variable (Gaussian noise)

### 🛠️ Implementation Steps:

1. Import necessary libraries (`numpy`, `matplotlib`).
2. Set up parameters: `initial_price`, `mu`, `sigma`, `days`.
3. Generate random Gaussian noise for price movements.
4. Compute the GBM formula iteratively.
5. Plot the stock price over time.

### 🏆 Expected Outcome:

A graph showing a randomly simulated stock price path over **one year (252 days)**.

Good luck! 🚀
