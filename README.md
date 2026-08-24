# Weather Data Analyzer

A Python project that retrieves historical weather data from the Open-Meteo API, processes it with pandas, performs temperature analysis, and generates visual reports with Matplotlib.

## Features

* Accepts a latitude and longitude from the user
* Accepts a historical start and end date
* Validates coordinate and date inputs
* Checks that the date range is valid
* Retrieves historical weather data from the Open-Meteo API
* Handles common API and network errors
* Converts API data into a pandas DataFrame
* Calculates:

  * Maximum temperature
  * Minimum temperature
  * Average maximum temperature
  * Average minimum temperature
  * Overall average temperature
  * Daily average temperature
  * Hottest day
  * Coldest day
  * Average daily temperature range
* Exports weather data to CSV
* Generates temperature graphs using Matplotlib

## Technologies

* Python
* Requests
* pandas
* Matplotlib
* Open-Meteo API
* uv

## Project Structure

```text
weather_project/
├── src/
│   └── weather_project/
│       ├── main.py
│       └── functions.py
├── data/
│   └── weather_data.csv
├── output/
│   ├── max_min_report.png
│   └── avg_daily_temp.png
├── pyproject.toml
└── README.md
```

## How It Works

The program first asks the user for a location and date range.

The inputs are validated before an API request is made. The program then sends a request to the Open-Meteo Historical Weather API and receives the weather data as JSON.

The JSON data is converted into a pandas DataFrame, where the temperature data can be analysed efficiently.

The program then calculates temperature statistics and generates visualisations showing the weather over the selected period.

## Error Handling

The project includes error handling for common problems, including:

* Invalid latitude or longitude input
* Invalid date formats
* Invalid date ranges
* Connection errors
* HTTP errors
* Invalid JSON responses
* Missing expected API data

The program returns `None` when an API operation fails so that the rest of the program does not attempt to process invalid data.

## Running the Project

Install the project dependencies using `uv`, then run the project from the project directory:

```bash
uv run python -m weather_project.main
```

The program will ask for:

```text
Latitude
Longitude
Start date (YYYY-MM-DD)
End date (YYYY-MM-DD)
```

Example:

```text
Latitude: 51.5577
Longitude: 0.0728
Start date: 2008-06-12
End date: 2008-07-17
```

## What I Learned

This project was built to develop practical Python and software-engineering skills rather than simply following a tutorial.

Key concepts practised include:

* Functions and modular code
* Importing functions between modules
* HTTP GET requests
* Constructing API request URLs
* Working with REST APIs
* JSON data
* Exception handling with `try`/`except`
* Input validation
* `datetime`
* pandas DataFrames and Series
* Vectorised pandas calculations
* Indexing with `.loc`
* Finding values with `.max()`, `.min()`, `.idxmax()` and `.idxmin()`
* Data visualisation with Matplotlib
* CSV data output
* Project organisation
* Running Python projects with `uv`

## Purpose

This project was built as practical training for AI automation/software engineering work and to demonstrate applied Python skills for degree apprenticeship applications.
