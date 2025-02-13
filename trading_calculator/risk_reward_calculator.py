def calculate_risk_reward(entry_price, higher_high, tp_percent, drop_percent):
    """
    Calculate the risk-to-reward ratio.

    Parameters:
        entry_price (float): The price at which the trade is entered.
        higher_high (float): The detected higher high price.
        tp_percent (float): Percentage increase from entry for take profit.
        drop_percent (float): Expected percentage drop (from higher high).

    Returns:
        dict: Contains entry_price, take_profit, expected_bottom, risk, reward, and risk_reward_ratio.
    """

    # Calculate take profit as entry_price increased by tp_percent
    take_profit = entry_price * (1 + tp_percent / 100)
    # Calculate expected bottom from the higher high by reducing it by expected_drop_percent
    if drop_percent > 0:
        expected_bottom = higher_high * (1 - drop_percent / 100)
    else:
        expected_bottom = entry_price

    # Risk is the difference between entry price and expected bottom
    risk = entry_price - expected_bottom
    # Reward is the difference between take profit and entry price
    reward = take_profit - entry_price
    rr_ratio = reward / (risk if risk > 0 else 1)

    return {
        "Entry price": entry_price,
        "Take Profit": take_profit,
        "Expected Bottom": expected_bottom,
        "Risk": risk,
        "Reward": reward,
        "R/R Ratio": round(rr_ratio, 2),
    }
