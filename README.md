# Risk-Reward Calculator CLI Application

This CLI tool calculates the risk-to-reward ratio based on historical price data from Binance and your input parameters. Depending on the details provided, the tool returns different outputs.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install foobar.

```bash
pip install -r requirements.txt
```

## Usage

-   Fetches historical data from Binance.
-   It identifies the last higher high and the subsequent lowest price.
-   Based on your input, it calculates the take profit target, expected bottom, risk, reward, and the risk-to-reward ratio.

## Instructions

Provide your input as a single line with details separated by spaces. The tool accepts three types of inputs:

### Only Trading Pair Provided

-   **Input:** `<Trading Pair>`
-   **Returns:**
    -   The last higher high
    -   The most recent lower low (price after the last higher high)

### Trading Pair, Entry Price, and Take Profit (TP) Percentage Provided

-   **Input:** `<Trading Pair> <Entry Price> <TP Percentage>`
-   **Returns:**
    -   The take profit target price (calculated from the entry price and TP percentage)
    -   The expected bottom (based on the detected higher high)
    -   The risk, determined using the actual drop (i.e., the last lower low)
    -   The reward
    -   The risk-to-reward (R/R) ratio

### Trading Pair, Entry Price, TP Percentage, and Anticipated Drop Percentage Provided

-   **Input:** `<Trading Pair> <Entry Price> <TP Percentage> <Anticipated Drop Percentage>`
-   **Returns:**
    -   The take profit target price
    -   The expected bottom
    -   The risk, calculated based on the anticipated drop provided by the user
    -   The reward
    -   The risk-to-reward (R/R) ratio

**Example Input:**
ETHUSDT 2543.25 25 40

This means you entered:

-   **Trading pair:** ETHUSDT
-   **Entry price:** $2543.25
-   **Take profit:** 25%
-   **Anticipated total drop:** 40% from the last higher high

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
