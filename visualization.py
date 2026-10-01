import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv(
    "books_cleaned.csv"
)


# -------------------------
# Price Distribution
# -------------------------

plt.figure(figsize=(8, 5))

plt.hist(
    df["Price"],
    bins=20
)

plt.xlabel("Price")

plt.ylabel("Number of Books")

plt.title("Book Price Distribution")

plt.show()

rating_counts = df[
    "Rating"
].value_counts()

rating_counts = rating_counts.reindex(
    ["One", "Two", "Three", "Four", "Five"]
)

plt.figure(figsize=(8, 5))

plt.bar(
    rating_counts.index,
    rating_counts.values
)

plt.xlabel("Rating")

plt.ylabel("Number of Books")

plt.title("Books by Rating")

plt.show()

top_books = df.sort_values(
    "Price",
    ascending=False
).head(10)

plt.figure(figsize=(10, 6))

plt.barh(
    top_books["Title"],
    top_books["Price"]
)

plt.xlabel("Price")

plt.ylabel("Book")

plt.title(
    "Top 10 Most Expensive Books"
)

plt.gca().invert_yaxis()

plt.show()