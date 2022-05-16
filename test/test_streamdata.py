import os
import asyncio
import sys
sys.path.append('../crypto-signals')
from main.exchange import data_stream
from main.strategy import Strategy
from main.order_manager import OrderManager
from mock_data import mock_data

def test_market_depth(pair:str='btcusdt'):
    data = mock_data()
    assert type(data[0]) is dict, f"The order book depth data type should be a dictionary, got: {type(data)}"

def test_historical_klines(pair:str='btcusdt'):
    data = mock_data()
    assert type(data[1]) is list, f"The historical klines data type should be a list, got: {type(data)}"


# if __name__ == "__main__":
#     # Fetch the CLI command first argument, which should be btcusdt
#     sym = sys.argv[1].upper()
#     # Printing a notice on what is being streamed into the command terminal
#     print(f"Will stream pair: {sym}")
#     print(f"Starting...")
#     # Execution of the program
#     loop = asyncio.get_event_loop()
#     loop.run_until_complete(Testing(sym).test_market_depth())
#     loop.run_until_complete(Testing(sym).test_market_depth())
