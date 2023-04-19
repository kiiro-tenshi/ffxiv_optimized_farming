<!DOCTYPE html>
<html>
<head>
  <meta charset="utf-8">

</head>
<body>
  <h1>Optimized FFXIV Farming</h1>

  <p>This repository contains a collection of scripts and tools that help you optimize your farming routines in various video games and other applications. The scripts use various algorithms and techniques, such as linear programming, genetic algorithms, and machine learning, to determine the optimal strategies for maximizing your gains while minimizing your costs and time investments. The scripts required Python version at least 3.9 to run correctly.</p>

  <h2>Optimized Moggle Tome Farm</h2>

  <p>Optimized Moggle Tome Farm is a Python script that optimizes your daily farming routine to get the moggle tomes in Final Fantasy XIV. The script uses linear programming to determine the optimal number of times to run each dungeon, allowing you to maximize the number of Irregular Tomestones of Mendacity obtained while staying within a given play time capacity.</p>

  <p>To use this application, follow the instructions in the <code>irregular_moggle_tome_farm</code> directory. Make sure you have a Google Sheets document with the dungeon data in the required format, and replace the <code>sheet_id</code>, <code>sheet_name</code>, and <code>capacity</code> variables with your own values. Then run the script using the command <code>python moggle_tome_farm.py</code>.</p>
  
  <h2>Optimized Retainer Venture Farm</h2>

  <p>Optimized Retainer Venture Farm is a Python script that maximizes your profit from retainer ventures in Final Fantasy XIV by assigning the best venture tasks to your retainers based on their levels and item levels. The script uses linear programming with the OR-Tools library to optimize the selection of ventures, considering the latest average sale prices of items and the quantity of items obtained from each venture.</p>

  <p>To use this application, follow the instructions in the main script. Make sure you have a Google Sheets document with the venture data in the required format, and replace the <code>sheet_id</code>, <code>sheet_name</code>, <code>world</code>, and <code>process_no</code> variables with your own values. Also, provide the appropriate information about your retainers in the <code>retainers</code> dictionary. Then run the script using the command <code>python retainer_hunting_venture_solver.py</code>.</p>


  <h2>License</h2>

  <p>This repository is licensed under the MIT License.</p>
</body>
</html>

