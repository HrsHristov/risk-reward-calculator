import requests
import pandas as pd

BASE_URL = "https://api.binance.com/api/v3/klines"

def get_historical_data(symbol="BTCUSDT", interval='1d', limit=100):
    """
    Fetch historical kline data frm Binance
    """
    
    params = {
        "symbol": symbol,
        "interval": interval,
        "limit": limit
    }
    
    response = requests.get(BASE_URL, params=params)
    data = response.json()
    
    #Define column names based on Binance API documentation
    columns = [
        "open_time", "open", "high", "low", "close", "volume",
        "close_time", "quote_asset_volume", "number_of_trades",
        "taker_buy_base_asset_volume", "taker_buy_quote_asset_volume", "ignore"
    ]
    df = pd.DataFrame(data, columns=columns)
    
    #Convert numeric olumns to float
    for col in ["open", "high", "low", "close"]:
        df[col] = pd.to_numeric(df[col])
    return df