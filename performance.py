import numpy as np
import pandas as pd

def annual_return(ret):
    return (1 + ret).prod() ** (252 / len(ret)) - 1

def annual_volatility(ret):
    return ret.std() * np.sqrt(252)

def sharpe_ratio(ret):
    vol = annual_volatility(ret)
    if vol == 0:
        return np.nan
    return annual_return(ret) / vol

def max_drawdown(ret):
    nav = (1 + ret).cumprod()
    peak = nav.cummax()
    dd = nav / peak - 1
    return dd.min()

def calc_ic(factor, close):
    future_ret = close.pct_change().shift(-1)
    ic = factor.corrwith(future_ret, axis=1)
    return ic.mean()

def summarize_performance(ret, factor=None, close=None):
    result = {
        "Annual Return": annual_return(ret),
        "Annual Volatility": annual_volatility(ret),
        "Sharpe Ratio": sharpe_ratio(ret),
        "Max Drawdown": max_drawdown(ret),
    }

    if factor is not None and close is not None:
        result["IC"] = calc_ic(factor, close)

    return result