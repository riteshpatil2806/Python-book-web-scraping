import requests
from bs4 import BeautifulSoup
import pandas as pd
import time


# Base URL
base_url = "https://books.toscrape.com/catalogue/page-{}.html"


# Empty list to store data
books_data = []


# Loop through 50 pages
for page in range(1, 51):

    url = base_url.format(page)

    print(f"Scraping page {page}...")

    try:

        # Send request
        response = requests.get(
            url,
            timeout=15
        )

        # Check for HTTP errors
        response.raise_for_status()

        # Parse HTML
        soup = BeautifulSoup(
            response.content,
            "html.parser"
        )

        # Find all books
        books = soup.select(
            "article.product_pod"
        )

        # Extract data from each book
        for book in books:

            # Book title
            title = book.select_one(
                "h3 a"
            )["title"]

            # Price
            price_text = book.select_one(
                ".price_color"
            ).get_text(strip=True)

            price = float(
                price_text
                .replace("£", "")
                .replace("Â", "")
            )

            # Rating
            rating = book.select_one(
                ".star-rating"
            ).get("class")[-1]

            # Availability
            availability = book.select_one(
                ".availability"
            ).get_text(
                " ",
                strip=True
            )

            # Store data
            books_data.append({

                "Title": title,

                "Price": price,

                "Rating": rating,

                "Availability": availability,

                "Page": page,

                "URL": url
            })

        # Wait between requests
        time.sleep(1)

    except requests.RequestException as error:

        print(
            f"Error on page {page}: {error}"
        )


# Convert list to DataFrame
df = pd.DataFrame(books_data)


# Display information
print("\nScraping completed!")

print(
    "Total books:",
    len(df)
)

print("\nFirst 5 records:")

print(df.head())


# Save data
df.to_csv(
    "books_data.csv",
    index=False,
    encoding="utf-8-sig"
)


print(
    "\nDataset saved as books_data.csv"
)