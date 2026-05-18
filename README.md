# 📊 TradingBot: Binance Futures Automation Client

A robust command-line interface (CLI) automation tool built in Python to orchestrate, validate, and execute algorithmic digital asset transactions on the Binance Futures Testnet. Built with a strict separation of concerns, the architecture ensures deterministic parameter validation, comprehensive stream logging, and structured runtime telemetry.

---

## 📂 System Architecture & Workspace Layout

The framework utilizes modular scaling to isolate connection logic, state routing, input integrity verification, and downstream logging outputs.

### Dependency Flow Data Map

'''

![System Metrics Diagram](images/system_diagram.png)

'''

### Repository File Tree

```text
TradingBot/
│
├── bot/
│   ├── __init__.py
│   ├── client.py        # Exchange API engine setup & authentication boundary
│   ├── log_file.py      # Dual-stream (Console + File) logging subsystem
│   ├── order.py         # Futures order composition & execution routing
│   └── validators.py    # Deterministic validation matrix for payload inputs
│
├── .env                 # Security boundary file for local API key isolation
├── main.py              # Application entry point, CLI parser, and presentation layer
└── requirements.txt     # Production manifest tracking pinned external runtimes

```

---

## ⚙️ Local Environment Provisioning

Follow these structured steps to deploy the runtime workspace inside an isolated application layer.

### 1. Initialize Virtual Environment Infrastructure

Navigate to the root project directory and build a localized environment sandbox:

```bash
python -m venv venv

```

Activate the isolated shell layer matching your system configuration:

* **Windows PowerShell:**
```powershell
.\venv\Scripts\Activate.ps1

```


* **Git Bash / Linux / macOS:**
```bash
source venv/bin/activate

```



### 2. Deploy Manifest Dependencies

Install upstream production library requirements verified for this engine framework:

```bash
pip install -r requirements.txt

```

### 3. Establish Local Secrets Boundary

Generate a `.env` infrastructure file directly within the workspace root directory and supply your secure Binance Testnet API key strings:

```env
api_key=YOUR_BINANCE_API_KEY
secret_key=YOUR_BINANCE_SECRET_KEY

```

> ⚠️ **CRITICAL SECURITY POLICIES:** Never stage or commit the `.env` secret container file into public repository branches. This framework enforces configuration isolation via an explicit entry inside `.gitignore`.

---

## 🚀 CLI Interface Matrix & Argument Specifications

The execution engine processes localized trade parameters directly via runtime interface flags.

### Universal Invocation Template

```bash
python main.py --symbol <TICKER> --side <ACTION> --type <STRATEGY> --quantity <VOLUME> [--price <VALUE>]

```

### Configuration Property Ledger

| Argument Flag | Requirement Status | Explicit Type | Allowed Values | Parameter Scope |
| --- | --- | --- | --- | --- |
| `--symbol` | **Required** | String | Valid Asset Pairs (e.g., `BTCUSDT`) | The target asset pair tracking index |
| `--side` | **Required** | String | `BUY`, `SELL` | Order market posture positioning |
| `--type` | **Required** | String | `MARKET`, `LIMIT` | Algorithmic execution strategy logic |
| `--quantity` | **Required** | Float | Positive real numbers | Unit sizing asset allocation scale |
| `--price` | *Conditional* | Float | Positive real numbers | Execution threshold barrier (Required for `LIMIT`) |

---

## 🎯 Verification Testing Matrices

Use these sample runtime parameters to validate application connectivity against the public test sandbox.

### Profile 1: Market Execution Verification

Executes immediate routing at top-of-book order liquidity prices:

```powershell
python main.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.001

```

### Profile 2: Limit Target Execution Verification

Establishes a passive pricing threshold constraint within the transaction order book:

```powershell
python main.py --symbol BTCUSDT --side SELL --type LIMIT --quantity 0.001 --price 50000

```

---

## 🖥️ System Telemetry & Output Presentation

Upon safe execution and confirmation from the exchange gateway, raw network response arrays are intercepted and transformed into structured telemetry blocks inside both the standard terminal view and the automated logfile destination `mytraderbot.log`:

```text
===========================================================
               SYSTEM ORDER TRANSACTION METRICS
===========================================================
[DATETIME STAMP] : 2026-05-18 23:30:03
[SYMBOL TICKER]  : BTCUSDT
[MARKET POSTURE] : SELL [SHORT POSITION]
[ORDER LOGIC]    : LIMIT STRATEGY
[VOLUME SIZING]  : 0.001
[TARGET PRICE]   : $50000.00

------------------- NETWORK INGEST STATUS ------------------
▶ Order Reference ID : 8471920516
▶ Execution Status   : NEW / ACCEPTED BY BOOK
▶ Time-In-Force Type : GTC (Good 'Til Cancelled)
▶ Log Accumulation   : Written safely to [mytraderbot.log]
===========================================================
[PROCESS SUCCEEDED]: Validation passed. Order dispatched without error.

```

--- 