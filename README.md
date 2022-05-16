# Cryptocurrency trading signals

## Disclaimer
This software is not for real-world use. It's designed for educational use. The trading strategy it works by, is not effective at all!
Also, DO NOT risk money which you are afraid to lose and ALWAYS do your own research. USE THE SOFTWARE AT YOUR OWN RISK. THE AUTHORS AND ALL AFFILIATES ASSUME NO RESPONSIBILITY FOR YOUR TRADING RESULTS.

## Supported Exchange marketplaces

- [X] [Binance](https://www.binance.com/)

## Features

- [x] **Based on Python 3.8**
- [x] **It's using bollinger bands as a trading strategy**
- [x] **It will log "BUY" messages into the terminal when BTC price is at the lower bollinger band & "SELL" messages when BTC price is at the upper bollinger bands, otherwise it will print "WAIT"**

## Quick start
***
** NOTE **
- **This section assumes docker & python3.8+ is already installed and that**

* Clone the repository into a docker container using command:
```<Language>

///docker build -t <your folder name> https://github.com/ungureanudaniel/crypto-signals.git

```
* cd into the crypto-signals directory
* Run the Dockerfile, located in the main directory crypto-signals using command:
```<Language>

///docker run crypto-signals

```

---

## Technologies & Libraries
***
A list of technologies used within the project:
* [python](https://example.com): Version 3.8
* [docker](https://example.com): Version 20.10.16
* [python-binance](https://python-binance.readthedocs.io/en/latest/): Version 1.0.16
* [websocket-client](https://python-binance.readthedocs.io/en/latest/): Version 1.3.2
* [numpy](https://python-binance.readthedocs.io/en/latest/): Version 1.22
* [pandas](https://python-binance.readthedocs.io/en/latest/): Version 1.4.2
* [pandas-datareader](https://python-binance.readthedocs.io/en/latest/): Version 0.10
* [matplotlib](https://python-binance.readthedocs.io/en/latest/): Version 1.0.16
* [loguru](https://python-binance.readthedocs.io/en/latest/): Version 0.6
* [pytest](https://python-binance.readthedocs.io/en/latest/): Version 7.1.2
