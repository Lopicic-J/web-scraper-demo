import csv
import json
import requests
from bs4 import BeautifulSoup

URL = "http://quotes.toscrape.com"


def scrape_quotes():
    response = requests.get(URL, timeout=10)
    response.raise_for_status()
    soup = BeautifulSoup(response.text, "html.parser")

    quotes = []

    for quote in soup.select(".quote"):
        text = quote.select_one(".text").get_text(strip=True)
        author = quote.select_one(".author").get_text(strip=True)
        tags = [tag.get_text(strip=True) for tag in quote.select(".tags .tag")]

        quotes.append(
            {
                "quote": text,
                "author": author,
                "tags": ", ".join(tags),
            }
        )

    return quotes


def save_csv(data):
    with open("example_output.csv", "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=["quote", "author", "tags"])
        writer.writeheader()
        writer.writerows(data)


def save_json(data):
    with open("example_output.json", "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)


def main():
    print("Scraping website...")
    data = scrape_quotes()
    print(f"Found {len(data)} quotes")
    save_csv(data)
    save_json(data)
    print("Saved example_output.csv")
    print("Saved example_output.json")


if __name__ == "__main__":
    main()
