# -*- coding: utf-8 -*-
"""
Created on Mon May 22 20:05:36 2023

@author: Kiiro Tenshi
"""
import requests, json
from urllib.parse import quote
import datetime
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.ticker as ticker

def get_item_id(item):
    item_ = quote(item)
    response = requests.get(f'https://xivapi.com/search?string={item_}').text
    json_response = json.loads(response)
    for result in json_response['Results']:
        item_id = result['ID']
    return item_id

def fetch_item_price(item_name, world):
    item_id = get_item_id(item_name)
    response = requests.get(f'https://universalis.app/api/v2/history/{world}/{item_id}').text
    json_response = json.loads(response)
    entries = sorted(json_response['entries'], key=lambda x: x['timestamp'], reverse=True)
    
    data = {}
    for entry in entries:
        timestamp = datetime.datetime.fromtimestamp(entry['timestamp']).strftime('%Y-%m-%d %H:%M:%S')
        price = entry['pricePerUnit']
        data[timestamp] = price
    
    # Extract the timestamps and prices from the data dictionary
    timestamps = list(data.keys())
    prices = list(data.values())
    
    # Convert timestamps to datetime objects for plotting
    timestamps = [datetime.datetime.strptime(ts, '%Y-%m-%d %H:%M:%S') for ts in timestamps]
    
    # Calculate the moving average
    ma_window = 7  # Moving average window size
    ma_prices = np.convolve(prices, np.ones(ma_window) / ma_window, mode='valid')
    ma_timestamps = timestamps[ma_window - 1:]
    
    # Create the plot
    fig, ax = plt.subplots()
    plt.plot(timestamps, prices, label='Prices')
    plt.plot(ma_timestamps, ma_prices, label='Moving Average (7 days)')
    plt.xlabel('Timestamp')
    plt.ylabel('Price')
    plt.title(f'{item_name} Price History - {world}')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.legend()
    
    # Format Y-axis ticks with thousands separators
    ax.yaxis.set_major_formatter(ticker.FuncFormatter(lambda x, pos: '{:,.0f}'.format(x)))
    
    # Add label to the latest price
    latest_price = prices[0]
    latest_price_formatted = '{:,.0f}'.format(latest_price)
    ax.annotate(f'Latest: {latest_price_formatted}', xy=(timestamps[0], prices[0]), xytext=(10, -20),
                textcoords='offset points', arrowprops=dict(arrowstyle='->'))
    
    # Adjust the position of the plot
    plt.subplots_adjust(top=0.85)
    
    # Display the plot
    plt.show()
    
    return data

if __name__ == '__main__':
    item_name = 'Modern Aesthetics - Gyr Abanian Plait'
    world = 'Jenova'
    data =  fetch_item_price(item_name, world)