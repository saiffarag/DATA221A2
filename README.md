# DATA221A2

## 📝 File Descriptions

### 🔹 Text Processing

**question1.py**
- Reads `sample-file.txt`
- Cleans tokens (lowercase, punctuation removal)
- Keeps tokens with at least two alphabetic characters
- Prints the 10 most frequent words

**question2.py**
- Builds bigrams from cleaned tokens
- Counts frequencies
- Prints the 5 most frequent bigrams

**question3.py**
- Identifies near-duplicate lines
- Normalizes text by removing whitespace and punctuation
- Prints number of duplicate sets and first two sets

**question10.py**
- Defines reusable function:
  `find_lines_containing(filename, keyword)`
- Case-insensitive search
- Prints total matches and first 3 matching lines

---

### 🔹 Data Analysis (Pandas)

**question4.py**
- Loads `student.csv`
- Filters students based on engagement criteria
- Saves results to `high_engagement.csv`

**question5.py**
- Creates `grade_band` column (Low / Medium / High)
- Generates grouped summary statistics
- Saves table as `student_bands.csv`

**question6.py**
- Loads `crime.csv`
- Creates `risk` category (HighCrime / LowCrime)
- Compares average unemployment rates

---

### 🔹 Web Scraping

**question7.py**
- Scrapes Wikipedia Data Science page
- Extracts page title
- Extracts first valid paragraph (≥ 50 characters)

**question8.py**
- Extracts all `<h2>` headings from main content
- Removes `[edit]` text
- Excludes References, External links, See also, Notes
- Saves results to `headings.txt`

**question9.py**
- Scrapes Wikipedia Machine Learning page
- Extracts first valid data table
- Handles headers and missing columns
- Saves table as `wiki_table.csv`
