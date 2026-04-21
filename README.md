# 🚀 Binance Futures Trading Bot

## 📌 Overview
A Python-based trading bot that interacts with Binance Futures Testnet to place MARKET and LIMIT orders via a clean CLI interface.

This project demonstrates API integration, secure request signing, error handling, and modular backend design.

---

## ⚙️ Features

- ✅ Place MARKET orders
- ✅ Place LIMIT orders
- ✅ Supports BUY and SELL
- ✅ CLI interface using Typer
- ✅ Logging with Loguru
- ✅ Input validation
- ✅ Error handling (API + user input)
- ✅ Account balance checking

---

## 🧱 Project Structure
trading_bot/
│
├── bot/
│ ├── client.py # API communication & signing
│ ├── orders.py # Order logic
│ ├── validators.py # Input validation
│ ├── logging_config.py # Logging setup
│
├── cli.py # CLI entry point
├── .env # API keys (not included in repo)
├── requirements.txt
├── README.md

---

## 🛠️ Setup Instructions

### 1. Clone the repository
git clone https://github.com/VidyaB21/trading-bot-binance.git

cd trading-bot-binance/trading_bot


### 2. Install dependencies

pip install -r requirements.txt


### 3. Create `.env` file

API_KEY=your_testnet_api_key
API_SECRET=your_testnet_secret_key


⚠️ Never commit your `.env` file

---

## ▶️ Usage

### 🔹 Place Market Order

python cli.py trade BTCUSDT BUY MARKET 0.01


### 🔹 Place Limit Order

python cli.py trade BTCUSDT BUY LIMIT 0.01 --price 30000


### 🔹 Check Balance

python cli.py balance


---

## 📊 Example Output


===== ORDER SUMMARY =====
Symbol : BTCUSDT
Side : BUY
Type : MARKET
Quantity : 0.01

===== ORDER RESPONSE =====
Order ID : 123456789
Status : FILLED
ExecutedQty : 0.01


---

## 🔐 Security

- API keys are stored securely using `.env`
- `.env` is excluded via `.gitignore`
- No sensitive data is exposed in the repository

---

## 🧠 Key Concepts Used

- REST API integration
- HMAC SHA256 request signing
- CLI application design
- Logging and debugging
- Error handling
- Modular architecture

---

## 🎯 Assignment Objective

This project was built as part of a Python Developer Internship assignment to demonstrate:

- Ability to interact with external APIs
- Clean and reusable code structure
- Proper logging and error handling

---

## 👨‍💻 Author

**Vidya Bag**  
---

## ⭐ Future Improvements

- Add Stop-Loss / Take-Profit orders
- Add Web UI (Streamlit / React)
- Add strategy-based trading logic
