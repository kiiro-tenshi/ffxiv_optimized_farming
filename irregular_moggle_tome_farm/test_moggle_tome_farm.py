# -*- coding: utf-8 -*-
"""
Created on Tue Apr 18 23:39:27 2023

@author: Kiiro Tenshi
"""

import pandas as pd
from irregular_tome_grind_solver import moggle_tome_farm

def test_moggle_tome_farm():
    sheet_id = '10wZiv70IZLeQlOaT2XX6e5vrWXERKudjX5Vjq65RaHc'
    sheet_name = 'data'
    capacity = 240
    dungeons, results = moggle_tome_farm(sheet_id, sheet_name, capacity)
    
    # Assert that the function returns a pandas DataFrame
    assert isinstance(dungeons, pd.DataFrame)
    
    # Assert that the results dictionary is not empty
    assert bool(results)
    
    # Assert that the total play time is less than or equal to the capacity
    total_playtime = sum(item['total_time'] for item in results.values())
    assert total_playtime <= capacity