

def check_validations(symbol,side,order_type,quantity,price):
    if symbol is None or not isinstance(symbol, str):
        raise ValueError("Symbol must be a non-empty string.(e.g., 'BTCUSDT')")  
    

    if side.upper() not in ['BUY','SELL']:
        raise ValueError("Side must be either 'BUY' or 'SELL'.")

    if order_type.upper() not in ['MARKET','LIMIT']:
        raise ValueError("Order type must be either 'MARKET' or 'LIMIT'.")

    try:
        quantity = float(quantity)
        if quantity <= 0:
            raise ValueError()
    except ValueError:
        raise ValueError("Quantity must be a positive number.")
    

    if order_type.upper() == 'LIMIT':
        if price is None:
            raise ValueError("Price must be provided for LIMIT orders.")
        try:
            price = float(price)
            if price <= 0:
                raise ValueError()
        except ValueError:
            raise ValueError("Price must be a positive number for LIMIT orders.")
