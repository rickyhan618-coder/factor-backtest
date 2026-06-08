from data import get_price_data
from factors import calc_momentum, calc_reversal, calc_volatility, cross_sectional_rank
from backtest import long_short_backtest
from performance import summarize_performance

tickers = [
    "AAPL", "MSFT", "NVDA", "AMZN", "GOOGL", "META", "TSLA",
    "JPM", "BAC", "GS", "V", "MA",
    "XOM", "CVX", "JNJ", "PFE", "UNH",
    "PG", "KO", "PEP", "WMT", "COST", "HD",
    "NFLX", "ADBE", "CRM", "INTC", "AMD", "QCOM"
]

close, volume = get_price_data(tickers)

factors = {
    "Momentum_60D": calc_momentum(close, 60),
    "Reversal_5D": calc_reversal(close, 5),
    "Volatility_20D": calc_volatility(close, 20),
}

for name, raw_factor in factors.items():
    factor = cross_sectional_rank(raw_factor)
    ret, weight = long_short_backtest(close, factor)
    perf = summarize_performance(ret, factor, close)

    print("\n", name)
    for k, v in perf.items():
        print(f"{k}: {v:.4f}")