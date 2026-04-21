import typer
from bot.orders import place_order, get_balance, place_stop_loss_take_profit
from bot.validators import validate_order

app = typer.Typer()


# 🔹 TRADE COMMAND
@app.command()
def trade(
    symbol: str,
    side: str,
    order_type: str,
    quantity: float,
    price: float = typer.Option(None, "--price")
):
    try:
        validate_order(symbol, side, order_type, quantity, price)

        print("\n===== ORDER SUMMARY =====")
        print(f"Symbol      : {symbol}")
        print(f"Side        : {side}")
        print(f"Type        : {order_type}")
        print(f"Quantity    : {quantity}")
        print(f"Price       : {price}")

        response = place_order(symbol, side, order_type, quantity, price)

        print("\n===== ORDER RESPONSE =====")

        if "orderId" in response:
            print(f"Order ID    : {response['orderId']}")
            print(f"Status      : {response['status']}")
            print(f"ExecutedQty : {response['executedQty']}")
        else:
            print("Error:", response)

    except Exception as e:
        print("Error:", e)


# 🔹 BALANCE COMMAND
@app.command()
def balance():
    try:
        data = get_balance()

        print("\n===== ACCOUNT BALANCE =====")

        if data and "assets" in data:
            for asset in data["assets"]:
                if asset["asset"] == "USDT":
                    print(f"Asset        : {asset['asset']}")
                    print(f"Wallet       : {asset['walletBalance']}")
                    print(f"Available    : {asset['availableBalance']}")
                    return

        print("No balance found")

    except Exception as e:
        print("Error:", e)


# 🔥 NEW: STOP LOSS + TAKE PROFIT
@app.command()
def sltp(
    symbol: str,
    side: str,
    quantity: float,
    stop_price: float,
    take_profit_price: float
):
    try:
        print("\n===== SL/TP ORDER =====")
        print(f"Symbol        : {symbol}")
        print(f"Side          : {side}")
        print(f"Quantity      : {quantity}")
        print(f"Stop Loss     : {stop_price}")
        print(f"Take Profit   : {take_profit_price}")

        result = place_stop_loss_take_profit(
            symbol, side, quantity, stop_price, take_profit_price
        )

        print("\n===== SL/TP RESPONSE =====")
        print(result)

    except Exception as e:
        print("Error:", e)


# 🚀 MAIN ENTRY
if __name__ == "__main__":
    app()