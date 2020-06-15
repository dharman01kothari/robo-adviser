# app/robo_advisor.py
import json
import requests
import datetime
import os
import re
import pandas as pd
import csv
from dotenv import load_dotenv
from alpha_vantage.timeseries import TimeSeries
from pandas import DataFrame

def usd_price(last_closing_price):
    return f"${last_closing_price:,.2f}"  

def get_data(): #Securely brining in personal API Key and getting data
    
    load_dotenv() 
    my_API_key = (os.environ.get("ALPHAVANTAGE_API_KEY")) 
    info = TimeSeries(key=my_API_key,output_format='json')
    
    return info

def get_ticker(): # Get list of sticker - for later - for now only 1
    
    tickers = input('Enter your stock symbol:')
    
    if tickers.isdigit():
        print('Please enter valid string stock tickers. Try again - Goodbye\n')
        quit()
    elif len(tickers) > 4 or not re.match("^[A-Za-z]*$", tickers):
        print('Please enter valid alphabetical string stock tickers. Maximum of 4 alphabets are allowed per NYSE/NASDAQ. Try again - Goodbye\n')
        quit()
    else:  
        return str(tickers.upper())

def recommendations(prices): # recommendation based on closing prices
    if prices[0]>=prices[1]:
        print("\n-------------------------\n")
        print("**RECOMMENDATION**: BUY!!")
        print("\n**REASON**: MOMENTUM STRATEGY - TODAYS CLOSE -",usd_price(prices[0]), "WAS EQUAL OR MORE THAN YESTERDAYS -",usd_price(prices[1]), "CLOSE! - RISING STOCK!")
        print("\n-------------------------\n")
    else:
        print("\n-------------------------\n")
        print("**RECOMMENDATION**: DON'T BUY!!")
        print("\n**REASON**: MOMENTUM STRATEGY - TODAYS CLOSE -",usd_price(prices[0]), " WAS LESS THAN YESTERDAYS -",usd_price(prices[1]), "CLOSE! - FALLING STOCK!")
        print("\n-------------------------\n")

if __name__ == "__main__":
       
    print("\n\n-------------------------\n")
    print("150%* PER YEAR EVERY YEAR** OR YOUR MONEY BACK*** ROBO STOCK ADVISOR\n")
    print("-------------------------\n")

    #Getting the data from internet----------------------------------------------   
    ts = get_data()
    stock = get_ticker()
    stock_data, meta_data = ts.get_daily(symbol=stock,outputsize="compact") #store the data and meta data seperately
    
    #Getting the relevant data----------------------------------------------   

    last_refresh =(meta_data['3. Last Refreshed'])
    latest_closing_price = float(next(iter(stock_data.items()))[1]['4. close'])
   
    timestamp=[]
    opening_prices=[]
    high_prices=[]
    low_prices=[]
    closing_prices=[]
    volumes=[]

    for i in stock_data.items():
        timestamp.append(i[0])
        opening_prices.append(float(i[1]['1. open']))
        high_prices.append(float(i[1]['2. high']))
        low_prices.append(float(i[1]['3. low']))
        closing_prices.append(float(i[1]['4. close']))
        volumes.append(int(i[1]['5. volume']))

    highest_price = max(high_prices)
    lowest_price = min(low_prices)

    csv_file_path = os.path.join(os.path.dirname(__file__), "../data/prices.csv")

    #Showing Output ----------------------------------------------------
    print("\n**SELECTED SYMBOL**:", stock)
    print("-------------------------\n")
    print("\nREQUESTING STOCK MARKET DATA...\n")
    print("**REQUEST AT**:",datetime.datetime.now().strftime('%d %B %Y at time %H:%M:%S'))
    print("-------------------------\n")
    
  
    print("**LATEST DATA FROM DAY**:",(timestamp[0])) 
    print("**LATEST CLOSE**:",usd_price(closing_prices[0]))
    print("**RECENT HIGH**:" ,usd_price(highest_price))
    print("**RECENT LOW**: ",usd_price(lowest_price))
 
    recommendations(closing_prices)
   
    print("DATA_TO_CSV: Done and under the data folder")  
    print("\n-------------------------")
    
    print("HAPPY INVESTING!")
    print("-------------------------") 

    #CSV File stuff ----------------------------------------------------

    csv_column_headers = ["timestamp", "open", "high", "low", "close", "volume"]

    i = 0
    with open(csv_file_path, "w",newline='') as csv_file:  
        csv_stuff = csv.writer(csv_file)
        csv_stuff.writerow(csv_column_headers)
        while i <= (len(timestamp)-1):
            csv_stuff.writerow([timestamp[i],opening_prices[i],high_prices[i],low_prices[i],closing_prices[i],volumes[i]])
            i = i + 1   