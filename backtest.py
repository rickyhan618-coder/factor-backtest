import numpy as np
import pandas as pd

def long_short_backtest(close, factor, quantile=0.2):
    ret = close.pct_change().shift(-1)

    long_signal = factor.ge(factor.quantile(1 - quantile, axis=1), axis=0)
    short_signal = factor.le(factor.quantile(quantile, axis=1), axis=0)

    long_weight = long_signal.div(long_signal.sum(axis=1), axis=0).fillna(0)
    short_weight = short_signal.div(short_signal.sum(axis=1), axis=0).fillna(0)

    weight = long_weight - short_weight
    portfolio_ret = (weight * ret).sum(axis=1)

    return portfolio_ret.dropna(), weight