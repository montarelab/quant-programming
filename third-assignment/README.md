# 📅 Day 3: Derivatives Pricing (Options)

## 🎯 Goal:

- Implement pricing models for European call and put options.
- Compare the Black-Scholes analytical solution with Monte Carlo simulation.

---

## 📖 Topics Covered

### 1. Call & Put Options

- A **call option** gives the holder the right (but not the obligation) to buy an asset at a specified price (strike price) on or before expiration.
- A **put option** gives the holder the right to sell an asset at a specified price on or before expiration.

### Call Option

| **Role**               | **Rights / Obligations**                             | **Profit / Loss Condition**                | **Outcome if $S_T > K$**                       | **Outcome if $S_T \leq K$**             |
| ---------------------- | ---------------------------------------------------- | ------------------------------------------ | ---------------------------------------------- | --------------------------------------- |
| **Call Buyer (Bull)**  | **Right** to buy the asset at the strike price $K$   | Profits when $S_T > K$ (higher the better) | Exercises the option, buys at $K$ and gains    | Option expires worthless, loses premium |
| **Call Seller (Bear)** | **Obligation** to sell the asset at $K$ if exercised | Profits when $S_T \leq K$ (keeps premium)  | Suffers a loss, has to sell below market price | Keeps the premium, no obligation        |

---

### Put Option

| **Role**              | **Rights / Obligations**                            | **Profit / Loss Condition**               | **Outcome if $S_T < K$**                      | **Outcome if $S_T \geq K$**             |
| --------------------- | --------------------------------------------------- | ----------------------------------------- | --------------------------------------------- | --------------------------------------- |
| **Put Buyer (Bear)**  | **Right** to sell the asset at the strike price $K$ | Profits when $S_T < K$ (lower the better) | Exercises the option, sells at $K$ and gains  | Option expires worthless, loses premium |
| **Put Seller (Bull)** | **Obligation** to buy the asset at $K$ if exercised | Profits when $S_T \geq K$ (keeps premium) | Suffers a loss, has to buy above market price | Keeps the premium, no obligation        |

- **$S_T$** = Underlying asset price at expiration
- **$K$** = Strike price
- **Premium** = The cost the buyer pays to enter the contract

### 2. Greeks (Delta, Gamma, Vega)

- **Delta ($\Delta$)**: Sensitivity of the option price to the underlying asset price.
- **Gamma ($\Gamma$)**: Sensitivity of Delta to the underlying asset price.
- **Vega ($\nu$)**: Sensitivity of the option price to volatility changes.

### 3. Black-Scholes Pricing Formula

The **Black-Scholes Model** provides a closed-form solution to calculate price of European options.

**European options** - is a type of options contract where the buyer or seller is able to execute the option only at its expiration date, not before.

#### **European Call Option Price:**

$$
C = S_0 N(d_1) - Ke^{-rt} N(d_2)
$$

#### **European Put Option Price:**

$$
P = Ke^{-rt} N(-d_2) - S_0 N(-d_1)
$$

Where:

$$
d_1 = \frac{\ln(S_0/K) + (r + \sigma^2/2) t}{\sigma \sqrt{t}}
$$

$$
d_2 = d_1 - \sigma \sqrt{t}
$$

- $S_0$ = Current stock price
- $K$ = Strike price
- $r$ = Risk-free interest rate
- $\sigma$ = Volatility
- $t$ = Time to expiration
- $N(d)$ = Cumulative distribution function of the standard normal distribution

### 4. Monte Carlo Method for Option Pricing

- Simulates multiple future price paths of the underlying asset using random sampling.
- Each path follows a geometric Brownian motion:

$$
S_T = S_0 e^{(r - \frac{1}{2} \sigma^2)T + \sigma W_T}
$$

- Where $W_T$ is a Wiener process (random normal variable).
- The option price is computed as the **discounted average payoff**:

**Discounted average payoff** - refers to the average of discounted payoffs over a certain number of periods, T. (Game Theory)

$$
C = e^{-rt} \mathbb{E} [\max(S_T - K, 0)] \quad \text{(Call Option Price)}
$$

- $C$: The price of the European call option.
- $e^{-rt}$: The discount factor, accounting for the time value of money.
- $\mathbb{E} [\max(S_T - K, 0)]$: The expected payoff of the call option at expiration, discounted to the present.

$$
P = e^{-rt} \mathbb{E} [\max(K - S_T, 0)] \quad \text{(Put Option Price)}
$$

- $P$: The price of the European put option.
- $e^{-rt}$: The discount factor, accounting for the time value of money.
- $\mathbb{E} [\max(K - S_T, 0)]$: The expected payoff of the put option at expiration, discounted to the present.

Here:

- $S_T$: The underlying asset price at expiration.
- $K$: The strike price of the option.
- $r$: The risk-free interest rate.
- $t$: The time to expiration.
- $\max$: Ensures that the payoff is non-negative, as options cannot have negative payoffs.
- $\mathbb{E}$: Represents the expected value under the risk-neutral measure.

- The larger the number of simulations, the more accurate the estimate.

---

## 🛠️ Assignment Tasks

### 1. Implement Black-Scholes pricing for European call and put options.

- Write a function to compute the option price using the closed-form Black-Scholes formula.

### 2. Implement Monte Carlo simulation for European options.

- Generate multiple random price paths using the Geometric Brownian Motion model.
- Calculate the expected payoff and discount it to the present.

### 3. Compare Monte Carlo vs. Analytical Pricing.

- Run both models with the same inputs and compare the results.
- Measure the accuracy of Monte Carlo with different numbers of simulations.
- Discuss convergence and variance reduction techniques (e.g., Antithetic Variates, Control Variates).

---

## 💡 Bonus Challenges (Optional)

- Implement the **Greeks** (Delta, Gamma, Vega) for both methods.
- Use **Variance Reduction Techniques** to improve Monte Carlo efficiency.
- Try **Implied Volatility Calculation**: Given an option price, find $\sigma$.
