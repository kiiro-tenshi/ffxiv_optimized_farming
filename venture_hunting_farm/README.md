<!DOCTYPE html>
<html>
<head>
  <meta charset="utf-8">
</head>
<body>
  <h1>Optimized Retainer Venture Farm</h1>

  <p>This project is a Python script that helps you maximize your profit from retainer ventures in Final Fantasy XIV by assigning the best venture tasks to your retainers based on their levels and item levels. The script uses linear programming with the OR-Tools library to optimize the selection of ventures, considering the latest average sale prices of items and the quantity of items obtained from each venture.</p>

  <h2>Installation</h2>

  <ol>
    <li>Clone the repository to your local machine:</li>
    <code>git clone https://github.com/kiiro-tenshi/ffxiv_optimized_farming</code>
    <li>Install the required Python packages:</li>
    <code>pip install -r requirements.txt</code>
  </ol>

  <h2>Usage</h2>

  <ol>
    <li>Make sure you have a Google Sheets document with the venture data in the following format:</li>
    <pre>
      | level | venture      | quantity | item_level | duration | cost | experience | item_id |
      |-------|--------------|----------|------------|----------|------|------------|---------|
      | 1     | Copper Ore   | 5        | 1          | 40       | 5    | 100        | 12345   |
      | ...   | ...          | ...      | ...        | ...      | ...  | ...        | ...     |
    </pre>
    <li>Find the ID of your Google Sheets document by looking at the URL. It should be a long string of letters and numbers between <code>/d/</code> and <code>/edit#gid=</code>.</li>
    <li>Open the <code>retainer_hunting_venture_solver.py</code> file and replace the <code>sheet_id</code>, <code>sheet_name</code>, <code>world</code>, and <code>process_no</code> variables with your own values. Also, provide the appropriate information about your retainers in the <code>retainers</code> dictionary.</li>
    <li>Run the script:</li>
    <code>python retainer_hunting_venture_solver.py</code>
    <p>The script will print the assigned ventures for each retainer and the maximum profit.</p>
  </ol>

  <h2>Testing</h2>

  <p>To run the unit tests for this project, install <code>pytest</code> and run the following command:</p>

  <code>pytest</code>

  <p>This will run all the test functions in the <code>test_optimized_retainer_venture_farm.py</code> file and report any failures or errors that occurred during the test run.</p>

  <h2>License</h2>

  <p>This project is licensed under the MIT License.</p>
</body>
</html>

