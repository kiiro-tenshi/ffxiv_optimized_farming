<!DOCTYPE html>
<html>
<head>
  <meta charset="utf-8">
</head>
<body>
  <h1>Optimized Moggle Tome Farm</h1>

  <p>This project is a Python script that helps you optimize your daily farming routine in the moggle tomes in Final Fantasy XIV. The script uses linear programming to determine the optimal number of times to run each dungeon in order to maximize the number of Irregular Tomestones of Mendacity obtained while staying within a given play time capacity.</p>

  <h2>Installation</h2>

  <ol>
    <li>Clone the repository to your local machine:</li>
    <code>git clone https://github.com/kiiro-tenshi/ffxiv_optimized_farming</code>
    <li>Install the required Python packages:</li>
    <code>pip install -r requirements.txt</code>
  </ol>

  <h2>Usage</h2>

  <ol>
    <li>Make sure you have a Google Sheets document with the dungeon data in the following format:</li>
    <pre>
      | Dungeon Name          | Estimated Completion Time | Number of Irregular Tomestones of Mendacity |
      |-----------------------|---------------------------|---------------------------------------------|
      | Moggle Mog XII Extreme| 15                        | 40                                          |
      | ...                   | ...                       | ...                                         |
    </pre>
    <li>Find the ID of your Google Sheets document by looking at the URL. It should be a long string of letters and numbers between <code>/d/</code> and <code>/edit#gid=</code>.</li>
    <li>Open the <code>moggle_tome_farm.py</code> file and replace the <code>sheet_id</code>, <code>sheet_name</code>, and <code>capacity</code> variables with your own values.</li>
    <li>Run the script:</li>
    <code>python moggle_tome_farm.py</code>
    <p>The script will print the optimal number of times to run each dungeon and the total number of Irregular Tomestones of Mendacity obtained.</p>
  </ol>

  <h2>Testing</h2>

  <p>To run the unit tests for this project, install <code>pytest</code> and run the following command:</p>

  <code>pytest</code>

  <p>This will run all the test functions in the <code>test_moggle_tome_farm.py</code> file and report any failures or errors that occurred during the test run.</p>

  <h2>License</h2>

  <p>This project is licensed under the MIT License.</p>
</body>
</html>
