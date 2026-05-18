import logging
from binance.exceptions import BinanceAPIException
from .client import get_client
from .validors import check_validations as validate_inputs


logger = logging.getLogger('mytraderbot.log')

def create_order(symbol, side, order_type, quantity, price=None):
    validate_inputs(symbol, side, order_type, quantity, price)
    client = get_client()
    try:
        if order_type.upper() == 'MARKET':
            order = client.futures_create_order(
                symbol=symbol,
                side=side.upper(),
                type=order_type.upper(),
                quantity=float(quantity),
                newOrderRespType="RESULT"
            )
        elif order_type.upper() == 'LIMIT':
            order = client.futures_create_order(
                symbol=symbol,
                side=side.upper(),
                type=order_type.upper(),
                quantity=float(quantity),
                newOrderRespType="RESULT",
                price=float(price), 
                timeInForce='GTC'
            )
        
        logger.info(f"Order processed successfully via server. Order ID: {order.get('orderId')}")
        return order
        
    except BinanceAPIException as e:
        logger.error(f"Failed to create order: {e.message} (Status Code: {e.status_code})")
        raise
    except Exception as e:
        logger.error(f"An unexpected error occurred: {e}")
        raise