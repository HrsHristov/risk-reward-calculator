from binance_client import get_historical_data
from trading_calculator import detect_higher_high, detect_lower_low, calculate_risk_reward
from utils import setup_logger, print_welcome_message, print_disclaimer

def main():
    
    # Set up logger
    logger = setup_logger("main")
    
    # Print welcome message and instructions
    print_welcome_message()
    #Print Disclaimer
    print_disclaimer()
    
    logger.info("Starting Risk To Reward Calculator")
    
    # Get the user input and split it by spaces.
    # The first element of the input is always the trading pair (e.g., "ETHUSDT").
    pair, *values = input("Your Input: ").split()
    
    #Fetch historical data from Binance
    data = get_historical_data(pair)
    # print(data)
    
    # Detect the last higher high using our trading calculator module
    higher_high = detect_higher_high(data)
    if higher_high:
        logger.info(f"Detected higher high: {higher_high}")
    else:
        logger.info("No higher high detected in recent data")
    
    # Detect the last lower low using our trading calculator module
    lower_low = detect_lower_low(data)
    if lower_low:
        logger.info(f"Detected lower low: {lower_low}")
    else:
        logger.info("No lower low detected in recent data")
    
    if len(values) == 3:
        # If all details are provided, unpack the remaining values.
        entry_price, tp_percent, expected_drop_percent = map(float, values)
        # Calculate the risk-to-reward ratio using the provided entry price and the detected higher high.
        result = calculate_risk_reward(entry_price, higher_high, tp_percent, expected_drop_percent)

        logger.info("Trade Setup:")
        for key, value in result.items():
            print(f"{key}: {value:.2f}")
    
if __name__ == "__main__":      
    main()