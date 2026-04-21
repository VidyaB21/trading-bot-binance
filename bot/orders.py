from bot.client import send_signed_request
from bot.logging_config import setup_logger

logger = setup_logger()


def place_order(symbol, side, order_type, quantity, price=None):
    try:
        params = {
            "symbol": symbol,
            "side": side,
            "type": order_type,
            "quantity": quantity
        }

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


def get_balance():
    try:
        response = send_signed_request("GET", "/fapi/v2/account")

        balances = response.get("assets", [])

        for asset in balances:
            if asset["asset"] == "USDT":
                return asset

        return None

    except Exception as e:
        logger.error(f"Error fetching balance: {e}")
        raise e