import requests
from bs4 import BeautifulSoup
import csv

url = "https://en.wikipedia.org/wiki/Machine_learning"
headers = {"User-Agent": "Mozilla/5.0"}

html = requests.get(url, headers=headers).text
soup = BeautifulSoup(html, "html.parser")

content_div = soup.find("div", id="mw-content-text")
if content_div is None:
    raise RuntimeError("Could not find div with id='mw-content-text'")

def clean_cell_text(cell):
    # keep spacing between nested tags readable
    return cell.get_text(" ", strip=True)

selected_table = None
selected_rows = None

# Locate the first table with at least 3 data rows (rows containing <td>)
for table in content_div.find_all("table"):

    table_classes = table.get("class", [])
    if any(cls in table_classes for cls in ["navbox", "vertical-navbox", "sidebar", "infobox"]):
        continue

    rows = table.find_all("tr")
    data_rows = [r for r in rows if r.find("td") is not None]

    if len(data_rows) >= 3:
        selected_table = table
        selected_rows = rows
        break

if selected_table is None:
    raise RuntimeError("No table with at least 3 data rows found in mw-content-text")

# Try to extract headers from <th> (prefer a header row)
header = []
header_row = None
for r in selected_rows:
    ths = r.find_all("th")
    tds = r.find_all("td")
    if ths and not tds:  # a pure header row
        header_row = r
        break

if header_row:
    header = [clean_cell_text(th) for th in header_row.find_all("th")]

# Extract all data rows
data = []
max_cols = 0

for r in selected_rows:
    tds = r.find_all("td")
    if not tds:
        continue
    row = [clean_cell_text(td) for td in tds]
    data.append(row)
    if len(row) > max_cols:
        max_cols = len(row)

# If no headers, create col1, col2, ...
if not header:
    header = [f"col{i}" for i in range(1, max_cols + 1)]
else:
    # If headers exist but are fewer than max columns, pad header too
    if len(header) < max_cols:
        header += [f"col{i}" for i in range(len(header) + 1, max_cols + 1)]
    # If headers are longer than max columns, trim to max columns
    if len(header) > max_cols:
        header = header[:max_cols]

# Pad each row to max_cols with empty strings
for row in data:
    if len(row) < max_cols:
        row.extend([""] * (max_cols - len(row)))
    elif len(row) > max_cols:
        del row[max_cols:]

print("Columns:", len(header))
print("Rows:", len(data))
print("First row:", data[0])


# Save to CSV
with open("wiki_table.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(header)
    writer.writerows(data)
