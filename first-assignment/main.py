import numpy;
import matplotlib.pyplot as plt;
import pandas as pd;

initial_price = 100;
mu = 0.1;  # daily return (0.1%)
sigma = 0.02;  # daily volatility (2%)
Z = numpy.random.normal(0, 1, 1000);  # Gaussian noise
days = 252;  # 1 year
data = [];

s0 = 