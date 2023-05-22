# -*- coding: utf-8 -*-
"""
Created on Mon May 22 20:43:21 2023

@author: Kiiro Tenshi
"""

from item_prices_monitor import get_item_id, fetch_item_price

def test_get_latest_sale_price():
    item_name = 'Modern Aesthetics - Gyr Abanian Plait'
    item_id = get_item_id(item_name)
    assert item_id == 23369

def test_hunting_venture_solver():
    item_name = 'Modern Aesthetics - Gyr Abanian Plait'
    world = 'Jenova'
    data =  fetch_item_price(item_name, world)
    assert isinstance(data, dict)
    assert len(data) > 0

