import string
from collections import Counter

# Read the file
with open("sample-file.txt", "r", encoding="utf-8") as f:
    text = f.read()

# Split into tokens (words)
tokens = text.split()

cleaned_tokens = []

for token in tokens:
    # Convert to lowercase
    token = token.lower()
    
    # Remove punctuation from beginning and end
    token = token.strip(string.punctuation)
    
    # Count alphabetic characters
    alpha_count = sum(1 for c in token if c.isalpha())
    
    # Keep tokens with at least two alphabetic characters
    if alpha_count >= 2:
        cleaned_tokens.append(token)

# Count word frequencies
freqs = Counter(cleaned_tokens)

# Get the 10 most frequent words
top_10 = freqs.most_common(10)

# Print results
for word, count in top_10:
    print(f"{word} -> {count}")
