from binance_client import get_historical_data
import utils
from trading_calculator import detect_higher_high, calculate_risk_reward

def main():
    
    # Set up logging
    logger = utils.setup_logger("main")
    logger.info("Starting Risk To Reward Calculator")
    #Fetch historical data from Binance
    data = get_historical_data()
    # print(data)
    print(f"higher high: {detect_higher_high(data)}")
    hh = detect_higher_high(data)

    result = calculate_risk_reward(105000, hh, 20, 30)
    for key, value in result.items():
        print(f"{key}: {value:.2f}")
        
main()