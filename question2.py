from collections import Counter
import string

# Read the file
with open("sample-file.txt", "r", encoding="utf-8") as f:
    text = f.read()

# Split into tokens
tokens = text.split()

cleaned = []

for token in tokens:
    # Convert to lowercase
    token = token.lower()
    
    # Remove punctuation from beginning and end
    token = token.strip(string.punctuation)
    
    # Keep tokens with at least two alphabetic characters
    alpha_count = sum(1 for c in token if c.isalpha())
    if alpha_count >= 2:
        cleaned.append(token)

# Construct bigrams
bigrams = []
for i in range(len(cleaned) - 1):
    bigrams.append((cleaned[i], cleaned[i + 1]))

# Count bigram frequencies
bigram_counts = Counter(bigrams)

# Print the 5 most frequent bigrams
for (w1, w2), count in bigram_counts.most_common(5):
    print(f"{w1} {w2} -> {count}")
