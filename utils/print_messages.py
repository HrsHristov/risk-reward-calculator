def print_welcome_message():
    welcome_text = """
    *************************************************
    📢 Welcome to the Risk-To-Reward Calculator CLI! 📢
    
    This tool fetches historical price data from Binance, identifies the last higher high, 
    and calculates the risk-to-reward ratio based on your input parameters.
    
    You can use three different input modes:
    
      1. **Only Trading Pair Provided**
         - **Input:** <Trading Pair>
         - **Returns:** 
             • The last higher high 
             • The most recent lower low (price after the last higher high)
      
      2. **Trading Pair, Entry Price, and Take Profit (TP) Percentage Provided**
         - **Input:** <Trading Pair> <Entry Price> <TP Percentage>
         - **Returns:** 
             • The take profit target price (calculated from the entry price and TP percentage)
             • The expected bottom (based on the detected higher high)
             • The risk (using the actual drop from the last lower low)
             • The reward
             • The risk-to-reward (R/R) ratio
       
      3. **Trading Pair, Entry Price, TP Percentage, and Anticipated Drop Percentage Provided**
         - **Input:** <Trading Pair> <Entry Price> <TP Percentage> <Anticipated Drop Percentage>
         - **Returns:** 
             • The take profit target price
             • The expected bottom
             • The risk (calculated based on the anticipated drop provided by you)
             • The reward
             • The risk-to-reward (R/R) ratio
    
    **Example Input:**
    
       ETHUSDT 2543.25 25 40
    
    This means:
       - Trading Pair: ETHUSDT
       - Entry Price: $2543.25
       - Take Profit at: 25%
       - Anticipated total drop: 40% from the last higher high
    
    Let's begin!
    *************************************************
    """

    print(welcome_text)


def print_disclaimer():
    disclaimer = """
    *************************************************
    📢 DISCLAIMER!!! 📢
    Nothing in this content constitutes financial advice. All information provided is for informational and educational purposes only. 
    Trading and investing carry inherent risks, and you are solely responsible for your own trading decisions. 
    Before making any financial decisions, please consult a licensed financial advisor to ensure that your strategies align with your personal circumstances. 
    
    You retain full responsibility for your trading at all times.
    Before trading with actual money, first make sure your risk management is professional-level.
    *************************************************
    """

    print(disclaimer)
