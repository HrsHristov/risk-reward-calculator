# Risk-Reward Calculator CLI Application

Simple app to calculate RR Ratio based on the last higher high

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install foobar.

```bash
pip install -r requirements.txt
```

## Usage

-   Fetches historical data from Binance.
-   Detects the last higher high in the data.
-   Calculates a risk-to-reward ratio based on an entry price, a take profit percentage, and an expected drop percentage.

## Instructions

1. **Ensure you have entered the proper trading pair, interval, and limit.**

2. **Pair with No Other Data:**  
   If you provide a pair with no other data, the app will provide only the most recent higher high.

3. **Take Profit Calculation:**  
   The app calculates a take profit target at a given percentage above the entry, and an expected bottom based on the detected higher high.

4. **Input Format:**  
   Provide the following details in a single line, separated by spaces:
    - **Trading Pair** (e.g., BTCUSDT, ETHUSDC)
    - **Entry Price** (e.g., 2543.25, 7.26, 0.54)
    - **Take Profit (TP) Percentage** (e.g., 25 for 25%)
    - **Expected Further Drop** (if you entered 30% down and expect another 10%, enter 40)

**Example Input:**
ETHUSDT 2543.25 25 40

_This means you entered ETHUSDT at $2543.25, set a TP at 25%, and expected it to drop 40% in total from the last higher high._

## Disclaimer

-   **No Financial Advice:**  
    Nothing in this content constitutes financial advice. All information is provided solely for informational and educational purposes.

-   **Risk Acknowledgment:**  
    Trading and investing carry inherent risks. You are solely responsible for your own trading decisions.

-   **Professional Consultation Recommended:**  
    Before making any financial decisions, consult a licensed financial advisor to ensure that your strategies are appropriate for your personal circumstances.

-   **Personal Responsibility:**  
    You retain full responsibility for your trading activities at all times. Ensure that your risk management practices meet professional standards before trading with real money.

## License

[MIT](https://choosealicense.com/licenses/mit/)
