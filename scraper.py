import csv
import json
import sys
from pathlib import Path

import requests
from bs4 import BeautifulSoup

DEFAULT_URL = "http://quotes.toscrape.com"
CSV_OUTPUT = Path("example_output.csv")
JSON_OUTPUT = Path("example_output.json")
TIMEOUT = 10


def fetch_html(url: str) -> str:
    response = requests.get(url, timeout=TIMEOUT)
    response.raise_for_status()
    return response.text


def parse_quotes(html: str) -> list[dict]:
    soup = BeautifulSoup(html, "html.parser")
    quotes = []

    for quote in soup.select(".quote"):
        text_element = quote.select_one(".text")
        author_element = quote.select_one(".author")
        tag_elements = quote.select(".tags .tag")

        if not text_element or not author_element:
            continue

        quotes.append(
            {
                "quote": text_element.get_text(strip=True),
                "author": author_element.get_text(strip=True),
                "tags": ", ".join(tag.get_text(strip=True) for tag in tag_elements),
            }
        )

    return quotes


def save_csv(data: list[dict], output_path: Path) -> None:
    with output_path.open("w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=["quote", "author", "tags"])
        writer.writeheader()
        writer.writerows(data)


def save_json(data: list[dict], output_path: Path) -> None:
    with output_path.open("w", encoding="utf-8") as file:
        json.dump(data, file, indent=2, ensure_ascii=False)


def main() -> None:
    url = sys.argv[1] if len(sys.argv) > 1 else DEFAULT_URL

    try:
        print(f"Fetching data from: {url}")
        html = fetch_html(url)

        print("Parsing content...")
        data = parse_quotes(html)

        if not data:
            print("No records found.")
            sys.exit(1)

        save_csv(data, CSV_OUTPUT)
        save_json(data, JSON_OUTPUT)

        print(f"Found {len(data)} records")
        print(f"Saved CSV: {CSV_OUTPUT}")
        print(f"Saved JSON: {JSON_OUTPUT}")
        print("Done.")

    except requests.RequestException as error:
        print(f"Request failed: {error}")
        sys.exit(1)
    except Exception as error:
        print(f"Unexpected error: {error}")
        sys.exit(1)


if __name__ == "__main__":
    main()