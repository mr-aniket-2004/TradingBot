# Trading Bot Workspace

A simple Binance futures trading bot CLI built in Python. This project uses the `python-binance` client to place MARKET and LIMIT orders on Binance testnet, with logging and input validation.

## Project Structure

- `main.py` - Command-line interface entry point for placing trades.
- `bot/client.py` - Loads API credentials and creates the Binance client.
- `bot/order.py` - Validates inputs and submits MARKET or LIMIT orders.
- `bot/log_file.py` - Configures logging to console and file.
- `bot/validors.py` - Ensures order parameters are valid.
- `requirements.txt` - Python dependencies for the project.

## Setup

1. Create and activate a Python virtual environment.

```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```

2. Install dependencies.

```powershell
pip install -r requirements.txt
```

3. Create a `.env` file in the project root with your Binance API credentials.

```env
api_key=YOUR_BINANCE_API_KEY
secret_key=YOUR_BINANCE_SECRET_KEY
```

> Note: The client is configured for Binance testnet by default. Use testnet keys or update the endpoint before using live trading settings.

## Usage

Run the bot from the project root using the required arguments:

```powershell
python main.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.001
```

For a LIMIT order, provide `--price`:

```powershell
python main.py --symbol BTCUSDT --side SELL --type LIMIT --quantity 0.001 --price 50000
```

### Command Arguments

- `--symbol`: Trading pair symbol (example: `BTCUSDT`).
- `--side`: `BUY` or `SELL`.
- `--type`: `MARKET` or `LIMIT`.
- `--quantity`: Order quantity as a positive number.
- `--price`: Required only for `LIMIT` orders.

## Example for Testing

To verify the bot works without placing a live order, use Binance testnet credentials and a simple MARKET order command:

```powershell
python main.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.001
```

If the command runs successfully, you should see transaction details printed in the console and a log entry written to `mytraderbot.log`.

## Guidelines

- Keep API keys out of version control. Store them in `.env` only.
- Use testnet credentials for development and testing.
- Validate all parameters before executing: symbol, side, order type, quantity, and price for LIMIT orders.
- Review `mytraderbot.log` after execution for debugging and order status information.
- If modifying the bot, maintain the separation of concerns:
  - `client.py` for connection setup
  - `order.py` for order logic
  - `log_file.py` for logging
  - `validors.py` for input checks

## Notes

- This project currently supports Binance futures testnet trading.
- For LIMIT orders, `price` must be a positive number.
- The bot prints a summary of the order response and writes logs to `mytraderbot.log`.
