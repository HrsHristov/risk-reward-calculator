def detect_lower_low(df, lookback=20):
    """
    Detect the last lower low in the given historical data.
    
    Parameters:
        df (pandas.DataFrame): DataFrame containing a 'low' column.
    
    Returns:
        float: The last lower low found, or None if not found.
    """
    
    # Extract the "low" prices as a numpy array.
    lows = df["low"].values
    ll_index = None
    
    # Loop through the data, starting from "lookback" and ending before the last "lookback" elements.
    for i in range(lookback, len(lows) - lookback):
        # Check if the current low is lower than all lows in the previous "lookback" period
        # and also lower than all lows in the next "lookback" period.
        if lows[i] < min(lows[i-lookback:i]) and lows[i] < min(lows[i+1:i+lookback+1]):
            ll_index = i  # Update the index if a lower low is found

    # If a lower low was detected, return its value.
    if ll_index is not None:
        return df.iloc[ll_index]["low"]
    # Otherwise, return None.
    return None