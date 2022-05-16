import datetime
import pandas as pd
import pandas_datareader as pdr
import matplotlib.pyplot as plt
import numpy as np
import requests
import math
import json
import os
import asyncio
import sys
sys.path.append('../crypto-signals')
from main.exchange import data_stream
from main.strategy import Strategy
from main.order_manager import OrderManager

class Testing():
    def __init__(self, pair, ):
        self.pair = pair

    async def test_connection(self):
        data = await data_stream(self.pair)
        if data:
            print(f"Connection is working")
        else:
            f"Connection not working"

    async def test_market_depth(self):
        data = await data_stream(self.pair)
        assert type(data[0]) is dict, f"The order book depth data type should be a dictionary, got: {type(data)}"

    async def test_historical_klines(self):
        data = await data_stream(self.pair)
        assert type(data[1]) is list, f"The historical klines data type should be a list, got: {type(data)}"

    async def test_buy_signal(self):
        result = {}

        data = await data_stream(self.pair)
        # Below i turned the historical klines lists to a dataframe for easier
        # calculations
        hist_df = pd.DataFrame(data[1], columns = [
            'Open_time',
            'Open',
            'High',
            'Low',
            'Close',
            'Volume',
            'Close_time',
            'Quote_asset_vol',
            'No_trades',
            'Taker_buy_base',
            'Taker_buy_quote',
            'Ignore'
            ])
        # convert close price to float and round the decimals
        hist_df['Close'] = hist_df.Close.astype(float)
        hist_df['Close'].round(decimals=2)

        closing_prices = hist_df['Close']

        # simple moving average calculation
        sma = closing_prices.rolling(20).mean().iloc[-1]
        # standard deviation calculation
        std = closing_prices.rolling(20).std().iloc[-1]
        # calculations to get bollinger bands
        bb_upper = (sma + std*2)
        bb_lower = (sma - std*2)

        """
        Below i built a dictionary by putting together all the data calculated
        above: current average price, SMA, Upper BB, Lower BB
        """
        # i set the ticker price to be equal to the lower bollinger band in order
        # to assert if the buy signal is loged
        result['current'] = bb_lower
        result['SMA'] = sma
        result['BB_UPPER'] = bb_upper
        result['BB_LOWER'] = bb_lower

        # Below is the logic to generate buy or sell signals using the data in the
        # dictionary stored in "self.result"
        if result['current'] >= result['BB_UPPER']:
            signal = f"sell"

        elif result['current'] <= result['BB_LOWER']:
            signal = f"buy"
        else:
            signal = f"wait"

        assert signal == "buy", f"The logged message should be 'buy', got: {ord}"

    async def test_sell_signal(self):
        result = {}
        data = await data_stream(self.pair)
        # Below i turned the historical klines lists to a dataframe for easier
        # calculations
        hist_df = pd.DataFrame(data[1], columns = [
            'Open_time',
            'Open',
            'High',
            'Low',
            'Close',
            'Volume',
            'Close_time',
            'Quote_asset_vol',
            'No_trades',
            'Taker_buy_base',
            'Taker_buy_quote',
            'Ignore'
            ])
        # convert close price to float and round the decimals
        hist_df['Close'] = hist_df.Close.astype(float)
        hist_df['Close'].round(decimals=2)

        closing_prices = hist_df['Close']

        # simple moving average calculation
        sma = closing_prices.rolling(20).mean().iloc[-1]
        # standard deviation calculation
        std = closing_prices.rolling(20).std().iloc[-1]
        # calculations to get bollinger bands
        bb_upper = (sma + std*2)
        bb_lower = (sma - std*2)

        """
        Below i built a dictionary by putting together all the data calculated
        above: current average price, SMA, Upper BB, Lower BB
        """
        # i set the ticker price to be equal to the lower bollinger band in order
        # to assert if the buy signal is loged
        result['current'] = bb_upper
        result['SMA'] = sma
        result['BB_UPPER'] = bb_upper
        result['BB_LOWER'] = bb_lower

        # Below is the logic to generate buy or sell signals using the data in the
        # dictionary stored in "self.result"
        if result['current'] >= result['BB_UPPER']:
            signal = f"sell"

        elif result['current'] <= result['BB_LOWER']:
            signal = f"buy"
        else:
            signal = f"wait"

        assert signal == "sell", f"The logged message should be 'sell', got: {ord}"

# def test_signals(pair:str, interval: int = None):
#     client = await AsyncClient.create(testnet=True)


if __name__ == "__main__":
    # Fetch the CLI command first argument, which should be btcusdt
    sym = sys.argv[1].upper()
    # Printing a notice on what is being streamed into the command terminal
    print(f"Will stream pair: {sym}")
    print(f"Starting...")
    # Execution of the program
    loop = asyncio.get_event_loop()
    loop.run_until_complete(Testing(sym).test_connection())
    loop.run_until_complete(Testing(sym).test_market_depth())
    loop.run_until_complete(Testing(sym).test_market_depth())
    loop.run_until_complete(Testing(sym).test_buy_signal())
    loop.run_until_complete(Testing(sym).test_sell_signal())
    # loop.run_until_complete(Testing(sym).test_sadsa())
