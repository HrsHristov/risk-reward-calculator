from binance_client import get_historical_data

def main():
    
    #Fetch historical data from Binance
    data = get_historical_data()
    print(data)


main()