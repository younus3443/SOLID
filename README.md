## OVERVIEW


It consists of three main components:

DataExtractor – Reads data from a file and returns it in a structured format.

DataAnalyzer – Performs analysis on the extracted data (e.g., finds the minimum difference between two columns).

Calculator – Links the extractor and analyzer to execute a complete workflow.


## Features

* Reads structured data files (.csv or .dat)

* Skips header or metadata lines if needed (skip_lines)

* Extracts only the specified columns

* Finds the row with the minimum difference between two numeric columns

* Modular and reusable design


## File Structure

```text
solid/
├─ Data/
│   ├─ weather.dat
│   ├─ football.dat
│
├─ Data_munging first/
│   └─ first_version.py
│
├─ second_version/
│   ├─ data_extractor.py
│   ├─ data_analyzer.py
│   ├─ calculator.py
│   ├─ weather.py
│   └─ soccer.py
│
├─ README.md
└─ venv/

```