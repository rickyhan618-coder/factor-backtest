import pandas as pd
import numpy as np

def calc_momentum(close, window=60):
    return close.pct_change(window)

def calc_reversal(close, window=5):
    return -close.pct_change(window)

def calc_volatility(close, window=20):
    ret = close.pct_change()
    return -ret.rolling(window).std()

def cross_sectional_rank(factor):
    factor = factor.rank(axis=1, pct=True)
    factor = factor.sub(factor.mean(axis=1), axis=0)
    return factor