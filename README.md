# Python Web Scraper Demo

This project demonstrates a simple Python web scraper that extracts structured data from a website and exports it to CSV and JSON formats.

The scraper collects quotes, authors, and tags from a demo website and converts them into machine-readable datasets.

---

## Features

- Web scraping using **Requests**
- HTML parsing using **BeautifulSoup**
- Export to **CSV**
- Export to **JSON**
- Clean and minimal Python script
- Reproducible environment with `requirements.txt`

---

## Installation

Clone the repository:
git clone https://github.com/YOUR-USERNAME/web-scraper-demo.git

cd web-scraper-demo


Create a virtual environment:
python3 -m venv .venv
source .venv/bin/activate

Install dependencies:
pip install -r requirements.txt


---

## Usage

Run the scraper:
python scraper.py


The script will create two files:
example_output.csv
example_output.json


---

## Example Output

The dataset contains:

| Quote | Author | Tags |
|------|------|------|
| Quote text | Author name | Tag list |

---

## Technologies Used

- Python
- Requests
- BeautifulSoup
- CSV / JSON data export

---

## Use Case

This script demonstrates a typical freelance task where website data needs to be extracted and delivered as structured datasets.

Common use cases:

- Data collection
- Web scraping
- Dataset generation
- Automation scripts