# app/robo_advisor.py
import json
import requests
import datetime


if __name__ == "__main__":

    stock = input('Enter your stock symbol:')

    print("-------------------------")
    print("SELECTED SYMBOL:", stock)
    print("-------------------------")
    print("REQUESTING STOCK MARKET DATA...")
    print("REQUEST AT:",datetime.datetime.now())
    print("-------------------------")
    print("LATEST DAY: 2018-02-20")
    print("LATEST CLOSE: $100,000.00")
    print("RECENT HIGH: $101,000.00")
    print("RECENT LOW: $99,000.00")
    print("-------------------------")
    print("RECOMMENDATION: BUY!")
    print("RECOMMENDATION REASON: TODO")
    print("-------------------------")
    print("HAPPY INVESTING!")
    print("-------------------------")