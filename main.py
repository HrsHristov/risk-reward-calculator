from binance_client import get_historical_data
import utils

def main():
    
    # Set up logging
    logger = utils.setup_logger("main")
    logger.info("Starting Risk To Reward Calculator")
    #Fetch historical data from Binance
    data = get_historical_data()
    print(data)


main()