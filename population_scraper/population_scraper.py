import os
import pandas as pd
import requests
from io import StringIO

# -----------------------------
# Step 1: Setup project folder
# -----------------------------
# Ensure all outputs (CSV/Excel) are saved in the same folder as this script
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# -----------------------------
# Step 2: Get the Wikipedia page
# -----------------------------
url = "https://en.wikipedia.org/wiki/List_of_countries_and_dependencies_by_population"
headers = {"User-Agent": "Mozilla/5.0"}  # fake browser to avoid 403 error
response = requests.get(url, headers=headers)

if response.status_code != 200:
    raise Exception(f"Failed to fetch page: {response.status_code}")

# -----------------------------
# Step 3: Parse tables from page
# -----------------------------
tables = pd.read_html(StringIO(response.text), attrs={"class": "wikitable"})
df = tables[0]  # first wikitable = countries by population

# -----------------------------
# Step 4: Clean column names
# -----------------------------
df.columns = [col.strip() for col in df.columns]

# -----------------------------
# Step 5: Clean specific columns
# -----------------------------
# Clean Notes column: replace "nan" text & NaN values with empty string
if "Notes" in df.columns:
    df["Notes"] = df["Notes"].replace("nan", "").fillna("")

# Convert Population to integer
if "Population" in df.columns:
    df["Population"] = pd.to_numeric(df["Population"], errors="coerce").astype("Int64")

# Convert "% of world" to decimal (e.g., 17.3% → 0.173)
if "% of world" in df.columns:
    df["% of world"] = df["% of world"].astype(str).str.replace("%", "", regex=False)
    df["% of world"] = pd.to_numeric(df["% of world"], errors="coerce") / 100

# -----------------------------
# Step 6: Save cleaned CSV
# -----------------------------
csv_path = os.path.join(BASE_DIR, "countries_by_population_clean.csv")
df.to_csv(csv_path, index=False, encoding="utf-8")

# -----------------------------
# Step 7: Save cleaned Excel (with bold headers)
# -----------------------------
excel_path = os.path.join(BASE_DIR, "countries_by_population_clean.xlsx")
with pd.ExcelWriter(excel_path, engine="xlsxwriter") as writer:
    df.to_excel(writer, index=False, sheet_name="Population")

    # Format headers bold
    workbook = writer.book
    worksheet = writer.sheets["Population"]
    header_format = workbook.add_format({"bold": True, "bg_color": "#D9D9D9"})
    for col_num, value in enumerate(df.columns.values):
        worksheet.write(0, col_num, value, header_format)

# -----------------------------
# Step 8: Show sample output
# -----------------------------
print("✅ Clean data saved!")
print(df.head(10))  # show first 10 rows
