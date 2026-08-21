# Data Cleaner

A terminal-based Python tool for cleaning messy CSV datasets — no dependencies on Streamlit or any GUI framework, just a clean menu-driven CLI.

## Overview

Data Cleaner walks a CSV file through a series of cleaning operations: handling missing values, removing duplicates, stripping special characters, and fixing data types. It's built and tested against `business_sales.csv`, a practice dataset with intentional messiness (missing values, duplicate rows, inconsistent formatting).

## Features

- Load and inspect CSV files
- View file info and a summary report before/after cleaning
- Remove rows with missing data
- Fill missing numeric values with the column mean
- Fill missing text values with a placeholder
- Remove duplicate rows
- Clean special characters from text fields
- Convert columns to correct data types
- View cleaned data in the terminal
- Save cleaned output to a new file

## Architecture

The tool is built around 12 core functions plus a main loop:

1. `load_file` — reads the CSV into memory
2. `show_file_info` — displays shape, columns, dtypes
3. `show_menu` — renders the CLI menu
4. `remove_missing_rows` — drops rows with nulls
5. `fill_missing_mean` — fills numeric NaNs with column mean
6. `fill_missing_text` — fills text NaNs with a placeholder
7. `remove_duplicates` — drops duplicate rows
8. `clean_special_chars` — strips unwanted characters from text
9. `convert_data_types` — casts columns to correct dtypes
10. `show_cleaned_data` — prints the cleaned dataframe
11. `show_report` — summarizes what was cleaned
12. `save_files` — writes the cleaned CSV to disk

A `main()` loop ties these together via the menu, letting the user pick operations interactively until they choose to save and exit.

## Status

Functions 1–6 are written and debugged (fixed issues: a misplaced `return` inside a loop, a wrong dtype selector, incorrect `len()` usage, and using `print` instead of `inplace=True` for `fillna`). Functions 7–12 are next.

## Roadmap

Planned integration into the flagship [Personal Finance Tracker](.) project as part of Phase 2, where this cleaning logic will handle messy imported transaction data.

## Usage

```bash
python data_cleaner.py
```

Follow the on-screen menu to load a CSV and apply cleaning operations in sequence.
