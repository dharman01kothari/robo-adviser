# app/robo_advisor.py
import json
import requests
import datetime
import os
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
    elif len(tickers) > 4:
        print('Please enter valid string stock tickers. Maximum of 4 alphabets are allowed per NYSE/NASDAQ. Try again - Goodbye\n')
        quit()
    else:  
        return str(tickers.upper())

def recommendations(prices):
    if prices[0]>=prices[1]:
        print("\n-------------------------\n")
        print("RECOMMENDATION: BUY!!")
        print("\nREASON: MOMENTUM STRATEGY - TODAYS CLOSE -",usd_price(prices[0]), "WAS EQUAL OR MORE THAN YESTERDAYS -",usd_price(prices[1]), "CLOSE! - RISING STOCK!")
        print("\n-------------------------\n")
    else:
        print("\n-------------------------\n")
        print("RECOMMENDATION: DON'T BUY!!")
        print("\nREASON: MOMENTUM STRATEGY - TODAYS CLOSE -",usd_price(prices[0]), " WAS LESS THAN YESTERDAYS -",usd_price(prices[1]), "CLOSE! - FALLING STOCK!")
        print("\n-------------------------\n")
    

if __name__ == "__main__":
   
    ts = get_data()
     
    stock = get_ticker()
    time_executed =datetime.datetime.now()
    
    stock_data, meta_data = ts.get_daily(symbol=stock,outputsize="compact") #store the data and meta data seperately
    
    last_refresh =(meta_data['3. Last Refreshed'])
    
    #print(stock_data,'\n')
    #print(meta_data,'\n')

    latest_closing_price = float(next(iter(stock_data.items()))[1]['4. close'])

    #print(latest_closing_price)

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
    
    
    #df_stock_data = pd.DataFrame(list(stock_data))

    #print(df_stock_data)

    """ #csv_file_path = "data/prices.csv" 
    csv_file_path = os.path.join(os.path.dirname(__file__), "../data/prices.csv")

    csv_column_headers = ["timestamp", "open", "high", "low", "close", "volume"]

    with open(csv_file_path, "w") as csv_file:  
        writer = csv.DictWriter(csv_file, fieldnames=csv_column_headers)
        writer.writeheader()  """


    print("\n\n-------------------------\n")
    print("150%* PER YEAR EVERY YEAR** OR YOUR MONEY BACK*** ROBO STOCK ADVISOR\n")
    print("SELECTED SYMBOL:", stock)
    print("-------------------------\n")
    print("REQUESTING STOCK MARKET DATA...")
    print("REQUEST AT:",time_executed)
    print("-------------------------\n")
    
  
    print("LATEST DAY:",(timestamp[0])) 
    print("LATEST CLOSE:",usd_price(closing_prices[0]))
    print("RECENT HIGH:" ,usd_price(highest_price))
    print("RECENT LOW: ",usd_price(lowest_price))
 
    recommendations(closing_prices)
   
    print("DATA_TO_CSV:")  
    print("-------------------------")
    
    print("HAPPY INVESTING!")
    print("-------------------------") 
