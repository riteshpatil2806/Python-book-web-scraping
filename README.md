# 📚 Book Web Scraping and Data Analysis

## Project Overview

This project uses Python to scrape book information from the Books to Scrape demo website. The collected data is stored in CSV format, cleaned using Pandas, and analyzed to identify pricing and rating patterns.

## Objectives

* Learn web scraping using Python.
* Extract information from multiple website pages.
* Store scraped data in CSV format.
* Clean and analyze data using Pandas.
* Visualize data using Matplotlib.
* Prepare data for a Power BI dashboard.

## Technologies Used

* Python
* Requests
* BeautifulSoup
* Pandas
* Matplotlib
* Power BI
* GitHub

## Data Collected

* Book Title
* Price
* Rating
* Availability
* Page Number
* Source URL

## Project Workflow

Website → Web Scraping → Data Extraction → Data Cleaning → CSV Dataset → Data Analysis → Visualization → Power BI Dashboard

## Project Structure

```text
Python_Web_Scraping_Project/
├── scraper.py
├── analysis.py
├── visualization.py
├── books_data.csv
├── books_cleaned.csv
├── requirements.txt
├── .gitignore
└── README.md
```

## Installation

Install the required libraries:

```bash
pip install requests beautifulsoup4 pandas matplotlib
```

## How to Run

### 1. Scrape the website

```bash
python scraper.py
```

### 2. Analyze the dataset

```bash
python analysis.py
```

### 3. Generate visualizations

```bash
python visualization.py
```

## Analysis Performed

* Total number of books
* Average, minimum, and maximum price
* Median book price
* Rating distribution
* Average price by rating
* Top 10 most expensive books
* Top 10 cheapest books

## Data Source

Books to Scrape: https://books.toscrape.com/

This is a demo website created for practicing web scraping. Its displayed prices and ratings are not intended to represent real-world book-market data.

## Disclaimer

This project is for educational purposes and demonstrates web scraping, data processing, and visualization using Python.
