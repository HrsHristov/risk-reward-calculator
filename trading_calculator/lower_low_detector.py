def detect_lower_low(df, hh_index):
    """
    Detect the lowest low between the given higher high index and the current price.
    
    Parameters:
        data (pandas.DataFrame): DataFrame containing a 'high' column.
        hh_index (int): The index of the last higher high.
        
    Returns:
        float: The lowest low between the higher high and the current price.
    """
    if hh_index is None:
        return None

    # Slice the DataFrame from the higher high to the end (current price)
    subset = df.iloc[hh_index:]["low"]
    # Find the minimum low in that range
    lowest_low = subset.min()
    return lowest_low