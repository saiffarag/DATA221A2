def find_lines_containing(filename, keyword):
    """
    Returns a list of (line_number, line_text) for lines that contain
    keyword (case-insensitive). Line numbers start at 1.
    """
    results = []
    keyword = keyword.lower()

    with open(filename, "r", encoding="utf-8") as f:
        for i, line in enumerate(f, start=1):
            if keyword in line.lower():
                results.append((i, line.rstrip("\n")))

    return results

matches = find_lines_containing("sample-file.txt", "data")

# Print how many matching lines were found
print("This word appears", len(matches), "times in this file")
if len(matches) < 3:
    print("Fewer than 3 matching lines found.")


# Print the first 3 matching lines
for line_num, text in matches[:3]:
    print(f"{line_num}: {text}")
