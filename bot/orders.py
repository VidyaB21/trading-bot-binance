from bot.client import send_signed_request
from bot.logging_config import setup_logger

logger = setup_logger()


# 🔹 PLACE MARKET / LIMIT ORDER
def place_order(symbol, side, order_type, quantity, price=None):
    try:
        params = {
            "symbol": symbol,
            "side": side,
            "type": order_type,
            "quantity": quantity
        }

        # LIMIT needs price
        if order_type == "LIMIT":
            params["price"] = price
            params["timeInForce"] = "GTC"

        logger.info(f"Placing order: {params}")

        response = send_signed_request("POST", "/fapi/v1/order", params)

        logger.info(f"Response: {response}")

        return response

    except Exception as e:
        logger.error(f"Error placing order: {e}")
        raise e


# 🔥 STOP LOSS + TAKE PROFIT (SIMULATED - TESTNET LIMITATION)
def place_stop_loss_take_profit(symbol, side, quantity, stop_price, take_profit_price):
    try:
        logger.info(f"Simulating SL/TP for {symbol}")

        result = {
            "message": "SL/TP simulated (Binance Testnet limitation)",
            "details": {
                "symbol": symbol,
                "side": side,
                "quantity": quantity,
                "stop_loss": stop_price,
                "take_profit": take_profit_price
            }
        }

        logger.info(f"SL/TP Result: {result}")

        return result

    except Exception as e:
        logger.error(f"Error placing SL/TP: {e}")
        raise e


# 🔹 GET ACCOUNT BALANCE
def get_balance():
    try:
        response = send_signed_request("GET", "/fapi/v2/account")

        logger.info("Fetched account balance")

        return response

    except Exception as e:
        logger.error(f"Error fetching balance: {e}")
        raise e