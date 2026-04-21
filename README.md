# Binance Futures Trading Bot

## Overview
This is a Python-based trading bot that places MARKET and LIMIT orders using Binance Futures Testnet.

## Features
- Place MARKET and LIMIT orders
- CLI interface using Typer
- Logging using Loguru
- Error handling
- Balance checking

## Setup

1. Clone repo
2. Install dependencies:
pip install -r requirements.txt

3. Add .env file:
API_KEY=your_key
API_SECRET=your_secret

## Usage

Market Order:
python cli.py trade BTCUSDT BUY MARKET 0.01

Limit Order:
python cli.py trade BTCUSDT BUY LIMIT 0.01 --price 30000

Balance:
python cli.py balance