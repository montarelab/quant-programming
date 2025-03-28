# **Week 1: Market Microstructure & Mean-Reversion Trading Strategy**

## **📌 Learning Objectives**

By the end of this assignment, you will:

- Understand order book mechanics, bid-ask spread, and market impact.
- Implement a mean-reversion trading strategy using a simulated order book.
- Backtest your strategy on historical stock data.

---

## **📖 Step 1: Understanding Market Microstructure**

### **Order Book Mechanics**

- An order book is a real-time list of buy (bid) and sell (ask) orders for a security.
- The best bid is the highest price a buyer is willing to pay.
- The best ask is the lowest price a seller is willing to accept.
- The bid-ask spread is the difference between the best ask and best bid.

### **Market Impact & Liquidity**

- **Liquidity:** How easily an asset can be traded without affecting its price.
- **Market Impact:** Large orders may move prices unfavorably.
- **Market Makers:** Traders who provide liquidity by continuously quoting bid and ask prices.

---

## **🛠️ Step 2: Implementing a Mean-Reversion Strategy**

### **📝 Strategy Overview**

- Mean reversion assumes that asset prices fluctuate around a mean value.
- If the price deviates too much from the mean, we assume it will revert.
- Example: If a stock’s price is much higher than its moving average, we sell; if much lower, we buy.

### **🔧 Implementation Steps**

### **1️⃣ Simulating an Order Book**

- Create an order book that tracks bid and ask prices.
- Implement limit orders (specific price orders) and market orders (immediate execution at best price).
- Ensure that buy orders (bids) are sorted from highest to lowest, while sell orders (asks) are sorted from lowest to highest.

### **2️⃣ Mean-Reversion Trading Algorithm**

- Use a simple moving average (SMA) to determine the mean price.
- Define an upper and lower threshold (e.g., ±2 standard deviations).
- Trading logic:
  - If the price exceeds the upper bound, enter a short position (sell).
  - If the price drops below the lower bound, enter a long position (buy).
  - Otherwise, hold the position.

### **3️⃣ Backtesting the Strategy**

- Simulate buying and selling based on the strategy signals.
- Track portfolio performance over time.
- Compare the strategy’s returns against a buy-and-hold strategy.

---

## **📊 Deliverables**

1. A **simulated order book** implementation.
2. A **mean-reversion trading strategy** with entry and exit signals.
3. A **performance report** including returns, drawdowns, and Sharpe ratio.
4. **Visualizations** showing order book behavior and trade execution.

---

## **📚 Resources & Datasets**

### **Data Sources**

- [Yahoo Finance API](https://pypi.org/project/yfinance/)
- [Quandl](https://www.quandl.com/)
- [Polygon.io](https://polygon.io/)

### **Books**

- _Algorithmic Trading_ by Ernie Chan
- _Advances in Financial Machine Learning_ by Marcos López de Prado

### **Courses**

- [Financial Engineering & Risk Management (Coursera)](https://www.coursera.org/specializations/financial-engineering-risk-management)
- [AI for Trading (Udacity)](https://www.udacity.com/course/ai-for-trading--nd880)

---

## **🚀 Next Steps**

- Modify the strategy with **Bollinger Bands** or **Kalman Filters**.
- Introduce **transaction costs** to reflect real-world execution.
- Use a **more advanced backtesting framework**, such as `backtrader`.

Would you like guidance on debugging or extending this strategy? 🚀
