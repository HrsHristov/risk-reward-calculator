from binance_client import get_historical_data
import utils
from trading_calculator import detect_higher_high

def main():
    
    # Set up logging
    logger = utils.setup_logger("main")
    logger.info("Starting Risk To Reward Calculator")
    #Fetch historical data from Binance
    data = get_historical_data()
    print(data)
    print(f"higher high: {detect_higher_high(data)}")


main()