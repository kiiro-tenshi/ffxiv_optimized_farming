# -*- coding: utf-8 -*-
"""
Created on Wed Apr 19 23:58:01 2023

@author:
"""

from retainer_hunting_venture_solver import get_latest_sale_price, hunting_venture_solver

# You may need to adjust these constants based on your actual test data
sheet_id = '1aEeVIDit7socb_EDqHNoh-v0v0V7aPRjPo5RkKClOYM'
sheet_name = 'data'
world = 'jenova'
process_no = 50
retainers = {
    'A': {'item_level': 60, 'level': 100},
    'B': {'item_level': 60, 'level': 100}
}

def test_get_latest_sale_price():
    venture_hunt_df = get_latest_sale_price(sheet_id, sheet_name, world, process_no)
    assert 'average_latest_sale_price' in venture_hunt_df.columns

def test_hunting_venture_solver():
    venture_hunt_df = get_latest_sale_price(sheet_id, sheet_name, world, process_no)
    assigned_ventures = hunting_venture_solver(retainers, venture_hunt_df)
    assert isinstance(assigned_ventures, dict)
    assert all(retainer in assigned_ventures for retainer in retainers.keys())
