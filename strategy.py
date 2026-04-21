import pandas as pd


def calculate_rsi(data, period=14):
    delta = data["close"].diff()

    gain = (delta.where(delta > 0, 0)).rolling(window=period).mean()
    loss = (-delta.where(delta < 0, 0)).rolling(window=period).mean()

    rs = gain / loss
    rsi = 100 - (100 / (1 + rs))

    return rsi


def generate_signal(df):
    df["rsi"] = calculate_rsi(df)

    latest_rsi = df["rsi"].iloc[-1]

    if latest_rsi < 30:
        return "BUY", latest_rsi
    elif latest_rsi > 70:
        return "SELL", latest_rsi
    else:
        return "HOLD", latest_rsi