# -*- coding: utf-8 -*-
"""
Created on Wed Apr 19 21:58:14 2023

@author: Kiiro Tenshi
"""

import requests
import pandas as pd
from urllib.parse import quote
import json
from datetime import datetime, timezone, timedelta
from concurrent.futures import ThreadPoolExecutor, as_completed
from statistics import mean, median
from ortools.linear_solver import pywraplp

def get_item_id(sheet_id, sheet_name):
    url = f"https://docs.google.com/spreadsheets/d/{sheet_id}/gviz/tq?tqx=out:csv&sheet={sheet_name}"
    venture_hunt_df = pd.read_csv(url)
    item_ids = []
    for item in venture_hunt_df['venture']:
        item_ = quote(item)
        response = requests.get(f'https://xivapi.com/search?string={item_}').text
        json_response = json.loads(response)
        ids = {}
        for result in json_response['Results']:
            ids[result['Name']] = result['ID']
        correct_id = ids[item]
        item_ids.append(correct_id)
        
    venture_hunt_df['item_id'] = item_ids
    return venture_hunt_df

def fetch_item_price(item_id, world, price_window):
    response = requests.get(f'https://universalis.app/api/v2/history/{world}/{item_id}').text
    json_response = json.loads(response)
    if 'lastUploadTime' not in json_response:
        return item_id, 0
    else:
        last_upload_time = datetime.fromtimestamp(json_response['lastUploadTime']/1000, timezone.utc)
        one_week_ago = datetime.now(timezone.utc) - timedelta(weeks=1)
        if last_upload_time < one_week_ago:
            return item_id, 0
        else:
            entries = sorted(json_response['entries'], key=lambda x: x['timestamp'], reverse=True)
            prices = [entry['pricePerUnit'] for entry in entries]
            median_price = median(prices)
            mad_price = median([abs(price - median_price) for price in prices])
            filtered_prices = [price for price in prices if abs(price - median_price) <= 3*mad_price]
            latest_prices = filtered_prices[:price_window]
            average_price = mean(latest_prices)
            return item_id, int(average_price)

def get_latest_sale_price(sheet_id, sheet_name, world, process_no, price_window=10):
    url = f"https://docs.google.com/spreadsheets/d/{sheet_id}/gviz/tq?tqx=out:csv&sheet={sheet_name}"
    venture_hunt_df = pd.read_csv(url)
    with ThreadPoolExecutor(max_workers=process_no) as executor:
        futures = [executor.submit(fetch_item_price, item_id, world, price_window) for item_id in venture_hunt_df['item_id']]
        sale_prices = {}
        for future in as_completed(futures):
            item_id, price = future.result()
            sale_prices[item_id] = price
    venture_hunt_df['average_latest_sale_price'] = [sale_prices[item_id] for item_id in venture_hunt_df['item_id']]
    return venture_hunt_df

def hunting_venture_solver(retainers, venture_hunt_df):
    # Create the solver
    solver = pywraplp.Solver.CreateSolver('GLOP')
    
    # Create binary variables for each venture and retainer
    x = {}
    for index, venture in venture_hunt_df.iterrows():
        for retainer in retainers.keys():
            x[index, retainer] = solver.BoolVar(f'x_{index}_{retainer}')
    
    # Objective function: maximize profit
    objective = solver.Objective()
    for index, venture in venture_hunt_df.iterrows():
        for retainer in retainers.keys():
            objective.SetCoefficient(x[index, retainer], venture['average_latest_sale_price'] * venture['quantity'])
    objective.SetMaximization()
    
    # Constraint 1: each retainer can do at most one venture
    for retainer in retainers.keys():
        constraint = solver.Constraint(0, 1)
        for index, venture in venture_hunt_df.iterrows():
            constraint.SetCoefficient(x[index, retainer], 1)
    
    # Constraint 2: a venture can only be assigned to a retainer if the retainer meets the level and item_level requirements
    for index, venture in venture_hunt_df.iterrows():
        for retainer, retainer_info in retainers.items():
            if venture['level'] > retainer_info['level'] or venture['item_level'] > retainer_info['item_level']:
                solver.Add(x[index, retainer] == 0)
    
    # Solve the optimization problem
    status = solver.Solve()
    assigned_ventures = {}
    # Check the result
    if status == pywraplp.Solver.OPTIMAL:
        print(f"Objective value (max profit): {solver.Objective().Value()} gil")
    
        # Retrieve the assigned ventures for each retainer
        for retainer in retainers.keys():
            for index, venture in venture_hunt_df.iterrows():
                if x[index, retainer].solution_value() == 1:
                    assigned_ventures[retainer] = {'venture': venture['venture'], 'level': venture['level'], 
                                                   'price': venture['average_latest_sale_price']}
    
        print("Assigned ventures:", assigned_ventures)
    
    else:
        print("The problem does not have an optimal solution.")
    return assigned_ventures

if __name__ == '__main__':
    sheet_id = '1aEeVIDit7socb_EDqHNoh-v0v0V7aPRjPo5RkKClOYM'
    sheet_name = 'data'
    world = 'jenova'
    process_no = 50
    venture_hunt_df = get_latest_sale_price(sheet_id, sheet_name, world, process_no)
    
    retainers = {
        'A': {'item_level': 130, 'level': 60},
        'B': {'item_level': 130, 'level': 60}
        }
    
    assigned_ventures = hunting_venture_solver(retainers, venture_hunt_df)