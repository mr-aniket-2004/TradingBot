import argparse
from datetime import datetime
import sys
from bot.log_file import set_logs
from bot.client import get_client
from bot.order import create_order



def main():
    # Instantiate the application logging engine
    logger = set_logs()
    
    parser = argparse.ArgumentParser(description="Trading Bot Command-Line Interface")
    parser.add_argument("--symbol", required=True, help="Token ticker pair identifier (e.g. BTCUSDT)")
    parser.add_argument("--side", required=True, choices=["BUY", "SELL", "buy", "sell"], help="Order execution direction")
    parser.add_argument("--type", required=True, choices=["MARKET", "LIMIT", "market", "limit"], help="Execution strategy")
    parser.add_argument("--quantity", required=True, help="Volume parameter scale units size")
    parser.add_argument("--price", required=False, default=None, help="Target threshold execution cost boundary (LIMIT exclusive)")
    
    args = parser.parse_args()
    
    try:
        client = get_client()
        
        response = create_order(
            symbol=args.symbol,
            side=args.side,
            order_type=args.type,
            quantity=args.quantity,
            price=args.price
        )

        raw_ms = response.get('updateTime', 0)
        formatted_time = "N/A"
        if raw_ms:
            formatted_time = datetime.fromtimestamp(raw_ms / 1000.0).strftime('%Y-%m-%d %H:%M:%S')


        avg_price = response.get('avgPrice', '0.0')
        if float(avg_price) == 0.0 and args.price:
            avg_price = f"{args.price} (Pending Limit)"



        print("\n" + "="*45)
        print("          === Transaction Details===")
        print(f" Target Trade Pair   : {args.symbol.upper()}")
        print(f" Execution Direction : {args.side.upper()}")
        print(f" Order Type Strategy : {args.type.upper()}")
        print(f" Asset Order Volume  : {args.quantity}")
        if args.price:
            print(f" Cost Limit Capital  : ${args.price}")
            
        print("\n          === MOCK EXCHANGE METRICS ===")
        print(f" Order Tracking ID   : {response.get('orderId')}")
        print(f" Execution Status    : {response.get('status')}")
        print(f" Filled Asset Units  : {response.get('executedQty')}")
        print(f" Weighted Average Px : ${response.get('avgPrice', 'N/A')}")
        print("="*45)
        print("[PROCESS COMPLETED] Workflow executed safely.")
        
    except Exception as e:
        print(f"\n[EXECUTION FAILED] Terminal operation stopped prematurely: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    main()