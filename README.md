# Customer Data Analysis (Python)

A beginner Python project that reads a customer text file and answers 20 questions using core Python only (no libraries).

## What it does
- Reads records from `customer_data.txt` into a list
- Filters by age, country, city, profession and gender
- Combines conditions (e.g. Indian Engineers or Doctors above 30)
- Counts records by profession and country using dictionaries
- Finds the oldest and youngest person and the average age

## Concepts used
File handling (`open()`, `with`), lists, loops, conditions, dictionaries, `.get()`, `int()`

## How to run
1. Keep `customer_analysis.py` and `customer_data.txt` in the same folder
2. Run: `python customer_analysis.py`

## Data
`customer_data.txt` contains 20 sample records (made-up data). Columns: id, first name, last name, age, gender, city, country, profession.

## Next steps
Rewrite using functions to remove repeated loops.
