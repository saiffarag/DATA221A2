from collections import defaultdict

# Define normalization function
def normalize_line(line: str) -> str:
    line = line.lower()
    return "".join(ch for ch in line if ch.isalnum())

# Open the file
with open("sample-file.txt", "r", encoding="utf-8") as f:
    lines = f.readlines()

groups = defaultdict(list)   # norm -> [(line_num, original_line)]
order = []                   # norms in first-seen order

# Normalize all the lines in the text
for i, line in enumerate(lines, start=1):
    original = line.rstrip("\n")
    norm = normalize_line(original)

    # Skip lines that become empty after normalization
    if norm == "":
        continue

    if norm not in groups:
        order.append(norm)
    groups[norm].append((i, original))

dup_sets = [norm for norm in order if len(groups[norm]) >= 2]

# Print results
print("There are", len(dup_sets), "near-duplicate lines in the text")

print("The first two sets and their line numbers and original lines are:")
for set_index, norm in enumerate(dup_sets[:2], start=1):
    print(f"\nSet {set_index}:")
    for line_num, original_line in groups[norm]:
        print(f"{line_num}: {original_line}")
