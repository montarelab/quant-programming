# 📅 Day 2: Risk & Portfolio Management

## 🛠️ Assignment: Implement Markowitz Portfolio Optimization

### **Task Overview**

You'll build an **optimal portfolio** using Markowitz's Modern Portfolio Theory (MPT), which balances risk and return by optimizing asset allocation.

### **Steps to Complete the Assignment:**

1. **Understand Portfolio Risk & Return**

   - Portfolio expected return:
     $$E(R_p) = \sum w_i E(R_i)$$. Where:
     - $$E(R_p)$$ = Expected return of the portfolio
     - $$E(R_i)$$ = Expected return of asset $$i$$
     - $$w_i$$ = Weight of asset $$i$$ in the portfolio. $$w_i = \frac{V_i}{V_{\text{total}}}$$. Where:
       - $$V_i$$ = Value of asset $$i$$ in the portfolio = amount of money invested in that particular asset
       - $$V_{\text{total}}$$ = Total value of the entire portfolio
   - Portfolio variance (risk):
     $$\sigma_p^2 = \sum \sum w_i w_j \sigma_{ij}$$
     where $$\sigma_{ij}$$ is the covariance between assets $$i$$ and $$j$$.

   **Candidate components:**

   1. **Asset Returns** - The individual expected returns of assets in the portfolio.
   2. **Asset Weights** - The proportion of each asset in the portfolio.
   3. **Portfolio Expected Return** - The weighted sum of individual asset returns.

2. **Load Asset Data**

   - Choose 3 stocks (e.g., AAPL, MSFT, TSLA)
   - Download historical price data using `yfinance`
   - Calculate daily returns

3. **Construct the Portfolio**

   - Generate random portfolio weights
   - Compute expected return, risk (variance), and Sharpe Ratio
   - Plot the **efficient frontier** (risk-return tradeoff curve)

4. **Find the Optimal Portfolio**
   - Use **scipy.optimize** to find weights maximizing the **Sharpe Ratio**
   - Compare optimized vs. random portfolios

---

### **Deliverables:**

✅ Python script implementing portfolio optimization.  
✅ Efficient frontier plot.  
✅ Optimal portfolio weights (printed or visualized).

---
