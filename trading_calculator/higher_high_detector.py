def detect_higher_high(df, lookback = 20):
    """
    Detect the last higher high in the given historical data.
    
    Parameters:
        data (pandas.DataFrame): DataFrame containing a 'high' column.
    
    Returns:
        float: The last higher high found, or None if not found.
    """
    
    # Extract the "high" prices as a numpy array.
    highs = df["high"].values
    hh_index = None
    
    # Loop through the data, starting from "lookback" and ending before the last "lookback" elements.
    for i in range(lookback, len(highs) - lookback):
        # Check if the current high is greater than all highs in the previous "lookback" period
        # and also greater than all highs in the next "lookback" period.
        if highs[i] > max(highs[i-lookback:i]) and highs[i] > max(highs[i+1:i+lookback+1]):
            hh_index = i # Update the index if a higher high is found

    # If a higher high was detected, return its value.
    if hh_index:
        return df.iloc[hh_index]["high"]
    # Otherwise, return None.
    return None