from collections import defaultdict

def normalize_line(line: str) -> str:
    line = line.lower()
    return "".join(ch for ch in line if ch.isalnum())

with open("sample-file.txt", "r", encoding="utf-8") as f:
    lines = f.readlines()

groups = defaultdict(list)   # norm -> [(line_num, original_line)]
order = []                   # norms in first-seen order

for i, line in enumerate(lines, start=1):
    original = line.rstrip("\n")
    norm = normalize_line(original)

    # ✅ Skip lines that become empty after normalization (blank lines / punctuation-only)
    if norm == "":
        continue

    if norm not in groups:
        order.append(norm)
    groups[norm].append((i, original))

dup_sets = [norm for norm in order if len(groups[norm]) >= 2]

print(len(dup_sets))

for set_index, norm in enumerate(dup_sets, start=1):
    print(f"\nSet {set_index}:")
    for line_num, original_line in groups[norm]:
        print(f"{line_num}: {original_line}")
