# app/robo_advisor.py
import json
import requests
import datetime
import os
import pandas
import csv
from dotenv import load_dotenv
from alpha_vantage.timeseries import TimeSeries
from pandas import DataFrame

def usd_price(last_closing_price):
    return f"${last_closing_price:,.2f}"  # > $12,000.71

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


if __name__ == "__main__":
   
    ts = get_data()
     
    stock = get_ticker()

    #store the data and meta data seperately
    stock_data, meta_data = ts.get_daily(symbol=stock,outputsize="compact")
    
    last_refresh =(meta_data['3. Last Refreshed'])
    
    # parse use the json module called jason.loads to change response.text to dictionary
    #parsed_response = stock_data["Meta Data"]["3. Last Refreshed"]
    #print(parsed_response)
    #print(len(stock_data))

    print(type(stock_data))

    #csv_file_path = "data/prices.csv" 
    csv_file_path = os.path.join(os.path.dirname(__file__), "../data/prices.csv")

    csv_column_headers = ["timestamp", "open", "high", "low", "close", "volume"]

    with open(csv_file_path, "w") as csv_file:  
        writer = csv.DictWriter(csv_file, fieldnames=csv_column_headers)
        writer.writeheader() 
        
    """     
       
 
   
    print("-------------------------")
    print("SELECTED SYMBOL:", stock)
    print("-------------------------")
    print("REQUESTING STOCK MARKET DATA...")
    print("REQUEST AT:",datetime.datetime.now())
    print("-------------------------")
    
  
    print(f"LATEST DAY: 
    print(f"LATEST CLOSE: 
    print(f"RECENT HIGH: 
    print(f"RECENT LOW: 
 
    
    print("-------------------------")
    print("RECOMMENDATION: BUY!")
    print("RECOMMENDATION REASON: TODO")
    
  
    print("-------------------------")
    print("DATA_TO_CSV: 
    print("-------------------------")
   
    
    print("-------------------------")
    print("HAPPY INVESTING!")
    print("-------------------------") 
 """