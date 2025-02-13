def print_welcome_message():
    welcome_text = """
    *************************************************
    📢 Welcome to the Risk To Reward Calculator App! 📢
    
    This tool will:
      - Fetch historical price data from Binance.
      - Detect the last higher high from the data.
      - Calculate the risk-to-reward ratio based on your trade parameters and the last higher high.
    
    Instructions:
      1. Ensure you have entered the proper trading pair, interval, and limit.
      2. If you provide a pair with no other data, the app will provide only the most recent higher high
      3. It calculates a take profit target at a given percentage above the entry,
         and an expected bottom based on the detected higher high.
      4. Please provide the following details in a single line, separated by spaces:
        4.1. Trading pair(e.g., BTCUSDT, ETHUSDC)
        4.2. Entry price(e.g., 2543.25, 7.26, 0.54)
        4.3. Take Profit(TP) percentage(e.g., 25 for 25%)
        4.4. Expected further drop(if you entered 30% down and expect another 10%, enter 40)
        
        Example input: ETHUSDT 2543.25 25 40
        Meaning you entered ETHUSDT at $2543.25, set a TP at 25%, and expected it drop 40% in total from the last higher high
        
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
