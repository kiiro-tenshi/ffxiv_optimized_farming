# -*- coding: utf-8 -*-
"""
Created on Mon Apr 17 23:46:25 2023
@author: Kiiro Tenshi
"""

import pandas as pd
from ortools.linear_solver import pywraplp

def moggle_tome_farm(sheet_id, sheet_name, capacity):
    url = f"https://docs.google.com/spreadsheets/d/{sheet_id}/gviz/tq?tqx=out:csv&sheet={sheet_name}"
    dungeons = pd.read_csv(url)
    # Extract data from DataFrame
    dungeon_names = dungeons['dungeon_name'].tolist()
    dungeon_times = dungeons['estimated_completion_time'].tolist()
    tome_rewards = dungeons['no_irregular_tomestones_of_mendacity'].tolist()
    
    # Create a linear solver object
    solver = pywraplp.Solver.CreateSolver('SCIP')
    
    # Define variables
    num_dungeons = len(dungeon_names)
    x = [solver.IntVar(0, solver.infinity(), f'x{i}') for i in range(num_dungeons)]
    
    # Define objective function
    objective = solver.Objective()
    for i in range(num_dungeons):
        objective.SetCoefficient(x[i], tome_rewards[i]) # set tome rewards as coefficients
    objective.SetMaximization() # maximize tome rewards
    
    # Define constraint
    constraint = solver.Constraint(0, capacity)
    for i in range(num_dungeons):
        constraint.SetCoefficient(x[i], dungeon_times[i]) # set play time as coefficients
        # The total play time used must be less than or equal to the capacity
    
    results = {}
    # Solve the problem then print the results
    if solver.Solve() == pywraplp.Solver.OPTIMAL:
        print('Optimal solution found!')
        print(f'Total tome gained: {int(objective.Value())}') # print the total tome rewards obtained
        for i in range(num_dungeons):
            if int(x[i].SolutionValue()) != 0:
                results[dungeon_names[i]] = {'run_times': int(x[i].SolutionValue()), 'total_time': int(x[i].SolutionValue())*dungeon_times[i]}
                print(f'{dungeon_names[i]}: run {int(x[i].SolutionValue())} times') # print how many times each dungeon should be run
        total_playtime = sum(item['total_time'] for item in results.values())
        print(f'Total play time: {total_playtime} minutes') # print how many times each dungeon should be run
    else:
        print('No optimal solution found.') # if there is no solution found by the solver
        
    return dungeons, results

if __name__ == '__main__':
    # Define input data as a pandas DataFrame
    sheet_id = '10wZiv70IZLeQlOaT2XX6e5vrWXERKudjX5Vjq65RaHc'
    sheet_name = 'data'
    capacity = 240  # capacity of play time per day
    dungeons, results = moggle_tome_farm(sheet_id, sheet_name, capacity)
        
    