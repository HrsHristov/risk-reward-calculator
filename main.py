from binance_client import get_historical_data
from trading_calculator import (
    detect_higher_high,
    detect_lower_low,
    calculate_risk_reward,
)
from utils import setup_logger, print_welcome_message, print_disclaimer


def main():
    # Set up logger
    logger = setup_logger("main")

    # Print welcome message and instructions
    print_welcome_message()
    # Print Disclaimer
    print_disclaimer()

    logger.info("Starting Risk To Reward Calculator")

    # Get the user input and split it by spaces.
    # The first element of the input is always the trading pair (e.g., "ETHUSDT").
    pair, *values = input("Your Input: ").split()

    # Fetch historical data from Binance
    data = get_historical_data(pair.upper())
    # print(data)

    # Detect the last higher high using our trading calculator module
    higher_high, hh_index = detect_higher_high(data)
    if higher_high:
        logger.info(f"Detected higher high: {higher_high}")
    else:
        logger.info("No higher high detected in recent data")

    # Detect the last lower low using our trading calculator module
    lower_low = detect_lower_low(data, hh_index)
    if lower_low:
        logger.info(f"Detected lower low: {lower_low}")

        # Actual drop % based on the lowest price after the last higher high
        actual_drop = round((1 - (lower_low / higher_high)) * 100, 2)
    else:
        logger.info("No lower low detected in recent data")

    if len(values) > 1:
        # If all details are provided, unpack the remaining values.
        entry_price, tp_percent = map(float, values[:2])
        # If no expected drop % is provided, drop_percent defaults to the actual_drop %
        drop_percent = float(values[2] if len(values) > 2 else actual_drop)
        # Calculate the risk-to-reward ratio using the provided entry price and the detected higher high.
        result = calculate_risk_reward(
            entry_price, higher_high, tp_percent, drop_percent
        )

        logger.info("Trade Setup:")
        for key, value in result.items():
            print(f"{key}: {value:.2f}")


if __name__ == "__main__":
    main()
