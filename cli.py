import typer
from bot.orders import place_order, get_balance
from bot.validators import validate_order

app = typer.Typer()


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


@app.command()
def balance():
    try:
        data = get_balance()

        print("\n===== ACCOUNT BALANCE =====")

        if data:
            print(f"Asset        : {data['asset']}")
            print(f"Wallet       : {data['walletBalance']}")
            print(f"Available    : {data['availableBalance']}")
        else:
            print("No balance found")

    except Exception as e:
        print("Error:", e)


if __name__ == "__main__":
    app()