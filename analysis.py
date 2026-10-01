import pandas as pd


# Load dataset
df = pd.read_csv("books_data.csv")


# -----------------------------
# DATA CLEANING
# -----------------------------

# Convert rating to numerical value
rating_mapping = {
    "One": 1,
    "Two": 2,
    "Three": 3,
    "Four": 4,
    "Five": 5
}

df["Rating_Number"] = df["Rating"].map(
    rating_mapping
)


# Remove duplicate records
df = df.drop_duplicates()


# -----------------------------
# BASIC INFORMATION
# -----------------------------

print("Dataset Shape:")
print(df.shape)

print("\nMissing Values:")
print(df.isnull().sum())

print("\nDuplicate Rows:")
print(df.duplicated().sum())


# -----------------------------
# PRICE ANALYSIS
# -----------------------------

print("\nAverage Price:")
print(round(df["Price"].mean(), 2))

print("\nMaximum Price:")
print(df["Price"].max())

print("\nMinimum Price:")
print(df["Price"].min())

print("\nMedian Price:")
print(df["Price"].median())


# -----------------------------
# MOST EXPENSIVE BOOK
# -----------------------------

print("\nMost Expensive Book:")

print(
    df.loc[
        df["Price"].idxmax()
    ]
)


# -----------------------------
# CHEAPEST BOOK
# -----------------------------

print("\nCheapest Book:")

print(
    df.loc[
        df["Price"].idxmin()
    ]
)


# -----------------------------
# RATING ANALYSIS
# -----------------------------

print("\nRating Distribution:")

print(
    df["Rating"].value_counts()
)


# -----------------------------
# AVERAGE PRICE BY RATING
# -----------------------------

print(
    "\nAverage Price by Rating:"
)

print(
    df.groupby(
        "Rating_Number"
    )["Price"].mean()
)


# -----------------------------
# TOP 10 EXPENSIVE BOOKS
# -----------------------------

print(
    "\nTop 10 Expensive Books:"
)

print(
    df.sort_values(
        "Price",
        ascending=False
    ).head(10)
)


# -----------------------------
# SAVE CLEAN DATASET
# -----------------------------

df.to_csv(
    "books_cleaned.csv",
    index=False,
    encoding="utf-8-sig"
)

print(
    "\nCleaned dataset saved!"
)