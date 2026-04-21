import streamlit as st
import requests
import pandas as pd
import plotly.graph_objects as go
import time

from bot.orders import place_order, place_stop_loss_take_profit, get_balance
from strategy import generate_signal

st.set_page_config(page_title="Trading Dashboard", layout="wide")

st.title("🚀 Binance Pro Trading Dashboard")

# 🔹 SIDEBAR
st.sidebar.title("⚙️ Trade Settings")
symbol = st.sidebar.text_input("Symbol", "BTCUSDT")
quantity = st.sidebar.number_input("Quantity", value=0.01)

# 🔹 FETCH MARKET DATA
def get_klines(symbol):
    try:
        url = f"https://api.binance.com/api/v3/klines?symbol={symbol}&interval=1m&limit=100"
        data = requests.get(url).json()

        df = pd.DataFrame(data, columns=[
            "time", "open", "high", "low", "close", "volume",
            "_", "_", "_", "_", "_", "_"
        ])

        df["time"] = pd.to_datetime(df["time"], unit="ms")
        df["open"] = df["open"].astype(float)
        df["high"] = df["high"].astype(float)
        df["low"] = df["low"].astype(float)
        df["close"] = df["close"].astype(float)

        return df

    except Exception:
        st.error("❌ Error fetching market data")
        return pd.DataFrame()

# 🔹 LOAD DATA WITH SPINNER
with st.spinner("Loading market data..."):
    df = get_klines(symbol)

# STOP IF DATA FAILS
if df.empty:
    st.stop()

# 🔹 CANDLESTICK CHART
st.subheader("📊 Candlestick Chart")

fig = go.Figure(data=[go.Candlestick(
    x=df["time"],
    open=df["open"],
    high=df["high"],
    low=df["low"],
    close=df["close"]
)])

st.plotly_chart(fig, width="stretch")

# 🔹 RSI SIGNAL
signal, rsi_value = generate_signal(df)

st.subheader("🤖 AI Trading Signal")

col1, col2 = st.columns(2)

with col1:
    st.metric("RSI Value", round(rsi_value, 2))

with col2:
    st.metric("Signal", signal)

# SIGNAL DISPLAY
if signal == "BUY":
    st.success("🟢 BUY Signal (RSI < 30)")
elif signal == "SELL":
    st.error("🔴 SELL Signal (RSI > 70)")
else:
    st.info("⚪ HOLD")

# 🔹 AUTO TRADE
st.subheader("⚡ Auto Trading")

if st.button("🚀 Auto Trade"):
    with st.spinner("Executing trade..."):
        try:
            if signal == "BUY":
                result = place_order(symbol, "BUY", "MARKET", quantity)
                st.success("✅ Auto BUY executed")
                st.json(result)

            elif signal == "SELL":
                result = place_order(symbol, "SELL", "MARKET", quantity)
                st.success("✅ Auto SELL executed")
                st.json(result)

            else:
                st.warning("⚪ No trade executed (HOLD)")

        except Exception as e:
            st.error(f"❌ Trade failed: {e}")

# 🔹 SL/TP (SIMULATED)
st.subheader("⚙️ Risk Management (SL/TP)")

stop_loss = st.number_input("Stop Loss", value=25000.0)
take_profit = st.number_input("Take Profit", value=35000.0)

if st.button("Set SL / TP"):
    result = place_stop_loss_take_profit(
        symbol, "BUY", quantity, stop_loss, take_profit
    )
    st.info("SL/TP configured")
    st.json(result)

# 🔹 BALANCE
st.subheader("💰 Account Balance")

if st.button("Check Balance"):
    try:
        balance = get_balance()
        st.json(balance)
    except Exception as e:
        st.error(f"❌ Error fetching balance: {e}")

# 🔄 AUTO REFRESH
time.sleep(5)
st.rerun()