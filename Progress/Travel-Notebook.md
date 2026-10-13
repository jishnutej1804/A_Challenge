# 📘 A_Challenge — Offline Travel Notebook

> 🌱 Revise. Practice. Improve. One day at a time.

**Purpose:** Offline revision of DSA, Python, SQL, EcoPulse, and Data Analysis.

---

## 📌 1. Data Structures and Algorithms

### 1.1 Two Sum — Hash Map

**File:** `DSA/Arrays/two_sum.py`

**Problem:** Find two numbers in an array whose sum equals a target.

**Approach:**
1. Create an empty hash map.
2. For each number, calculate `target - number`.
3. Check whether the complement is already in the map.
4. If found, return the two indices.
5. Otherwise, store the number and its index.

**Complexity:**
- Time: `O(n)` average
- Space: `O(n)`

**Key idea:** A hash map helps find previously visited numbers efficiently.

### 1.2 Valid Anagram — Frequency Counting

**File:** `DSA/Strings/valid_anagram.py`

**Problem:** Determine whether two strings contain the same characters with the same frequencies.

**Approach:**
1. If the lengths differ, return `False`.
2. Count the characters in both strings.
3. Compare the frequency counts.

**Complexity:**
- Time: `O(n)`
- Space: Depends on the number of distinct characters.

**Key idea:** Character frequency is more useful than character position.

### 1.3 Valid Palindrome — Two Pointers

**File:** `DSA/Two-Pointers/valid_palindrome.py`

**Problem:** Check whether a string is a palindrome, ignoring non-alphanumeric characters and letter case.

**Approach:**
1. Set one pointer at the beginning and another at the end.
2. Skip characters that are not letters or digits.
3. Compare the remaining characters without case sensitivity.
4. Move both pointers inward.
5. If a mismatch occurs, return `False`.

**Complexity:**
- Time: `O(n)`
- Space: `O(1)` if performed in place on the input representation.

**Key idea:** Two pointers can compare both ends without reversing the string.

### 1.4 Two Sum II — Sorted Array

**File:** `DSA/Two-Pointers/two_sum_ii_sorted.py`

**Problem:** Find two numbers in a sorted array that add up to a target.

**Approach:**
1. Place the left pointer at the beginning.
2. Place the right pointer at the end.
3. Calculate their sum.
4. If the sum is too small, move the left pointer right.
5. If the sum is too large, move the right pointer left.
6. Stop when the target is found.

**Complexity:**
- Time: `O(n)`
- Extra space: `O(1)`

**Key idea:** The sorted order tells us which pointer to move.

### 1.5 Best Time to Buy and Sell Stock

**File:** `DSA/Arrays/best_time_to_buy_sell_stock.py`

**Problem:** Find the maximum profit from buying before selling.

**Approach:**
1. Track the minimum price seen so far.
2. Calculate the profit from selling at the current price.
3. Update the maximum profit.
4. Update the minimum price when a lower price appears.

**Complexity:**
- Time: `O(n)`
- Extra space: `O(1)`

**Key idea:** Track the best buying opportunity while making one pass.

### 1.6 Valid Parentheses — Stack

**File:** `DSA/Stack/valid_parentheses.py`

**Problem:** Check whether brackets are correctly matched and nested.

**Approach:**
1. Create an empty stack.
2. Push opening brackets onto the stack.
3. For a closing bracket, check whether the stack has the matching opening bracket on top.
4. Return `False` for a mismatch.
5. At the end, the stack must be empty.

**Complexity:**
- Time: `O(n)`
- Space: `O(n)` in the worst case.

**Key idea:** A stack follows **LIFO — Last In, First Out**.

---

## 🗄️ 2. SQL and DBMS

### 2.1 Basic SQL Concepts

| Concept | Meaning |
|---|---|
| `CREATE TABLE` | Creates a table |
| `PRIMARY KEY` | Uniquely identifies each row |
| `NOT NULL` | Prevents a column from having a NULL value |
| `INSERT INTO` | Adds records |
| `SELECT` | Retrieves data |
| `WHERE` | Filters rows |
| `SUM()` | Calculates a total |
| `GROUP BY` | Groups rows for aggregate calculations |
| `AS` | Gives a column or expression an alias |

### 2.2 EcoPulse Database

**File:** `Projects/EcoPulse/db/schema_and_queries.sql`

The `user_activities` table contains:

- `activity_id`
- `user_id`
- `activity_date`
- `category`
- `activity_name`
- `amount`
- `unit`
- `carbon_emission_kg`

**Example — Total emissions by category:**

```sql
SELECT
    category,
    SUM(carbon_emission_kg) AS total_emission
FROM user_activities
GROUP BY category;
```

**Remember:** `GROUP BY` creates groups; `SUM()` calculates the total within each group.

### 2.3 SQL JOINs

**File:** `Projects/EcoPulse/db/window_functions.sql`

- `INNER JOIN`: Returns rows with matching values in both tables.
- `LEFT JOIN`: Returns all rows from the left table and matching rows from the right table. Unmatched right-side values appear as `NULL`.

Example:

```sql
SELECT
    u.user_id,
    a.activity_name
FROM users AS u
LEFT JOIN user_activities AS a
    ON u.user_id = a.user_id;
```

### 2.4 Window Functions

A window function calculates a value across related rows while retaining the individual rows.

Example:

```sql
SELECT
    user_id,
    total_emission,
    RANK() OVER (
        ORDER BY total_emission DESC
    ) AS emission_rank
FROM user_totals;
```

**Remember:**
- `RANK()` assigns rankings.
- `ORDER BY` inside `OVER()` determines ranking order.
- Tied values receive the same rank, and the next rank may be skipped.

---

## 🌱 3. EcoPulse — Sustainability Carbon Tracker

**Project folder:** `Projects/EcoPulse/`

### Project Files

| File | Responsibility |
|---|---|
| `index.html` | Page structure |
| `styles.css` | Appearance and responsive styling |
| `script.js` | Interactions and carbon calculator |
| `db/schema_and_queries.sql` | Schema and aggregate queries |
| `db/window_functions.sql` | JOINs and window functions |

### Basic Architecture

```text
User
 |
 v
HTML Interface
 |
 v
JavaScript
 |
 +--> Carbon Calculator
 |
 +--> Dashboard Interactions
 |
 v
Displayed Results

SQL Files
 |
 v
Database Schema and Analysis Queries
```

### Concepts to Remember

- **HTML:** Defines the page structure.
- **CSS:** Controls layout, colors, spacing, and responsive design.
- **JavaScript:** Adds behavior and calculations.
- **DOM:** The browser's representation of the webpage, which JavaScript can access and update.
- **Responsive design:** Adapts the interface to different screen sizes.
- **Reduced-motion support:** Respects preferences for less animation.

### Review Questions

1. What is the role of each frontend file?
2. How does the carbon calculator obtain and display a result?
3. Why should a dashboard work on mobile screens?
4. How are SQL queries used to analyze activity data?

---

## 📊 4. Python and Data Analysis

**File:** `analysis/carbon_eda.py`

### Pandas Revision

- A **Series** is a one-dimensional labeled data structure.
- A **DataFrame** is a two-dimensional table.
- `head()` displays the first rows.
- `info()` summarizes columns and data types.
- `describe()` provides descriptive statistics.
- `groupby()` groups data for analysis.
- `mean()` calculates an average.
- `sum()` calculates a total.

### Typical EDA Workflow

```text
Load Data
   |
Inspect Data
   |
Check Missing Values
   |
Summarize Data
   |
Group and Compare
   |
Interpret Findings
```

### Carbon-Emissions Analysis

Useful questions:
- Which category has the highest total emissions?
- Which category has the highest average emissions?
- How do total emissions differ between users?
- What patterns can be observed in the sample data?

**Important:** A result from a sample dataset describes that dataset; it does not automatically represent the real world.

---

## 🔁 5. Complexity Quick Reference

| Complexity | General meaning |
|---|---|
| `O(1)` | Constant work |
| `O(log n)` | Work grows logarithmically |
| `O(n)` | Work grows linearly |
| `O(n log n)` | Common in efficient sorting |
| `O(n²)` | Often appears with nested loops |

**Rule of thumb:** Consider how the number of operations grows as the input size increases.

---

## ✍️ 6. Offline Practice Checklist

### DSA
- [ ] Explain Two Sum without looking at the notes.
- [ ] Write Valid Anagram from memory.
- [ ] Trace Valid Palindrome using two pointers.
- [ ] Solve Two Sum II on a sorted array.
- [ ] Explain the stock-profit single-pass approach.
- [ ] Trace Valid Parentheses using a stack.

### SQL
- [ ] Write a `CREATE TABLE` statement.
- [ ] Use `INSERT INTO` to add sample records.
- [ ] Calculate totals using `SUM()` and `GROUP BY`.
- [ ] Explain `INNER JOIN` versus `LEFT JOIN`.
- [ ] Explain `RANK()` and how ties work.

### EcoPulse
- [ ] Draw the project architecture from memory.
- [ ] Explain the purpose of each project file.
- [ ] Describe how the carbon calculator works.
- [ ] Suggest one improvement to the dashboard.

### Data Analysis
- [ ] Explain Series versus DataFrame.
- [ ] Describe the EDA workflow.
- [ ] Explain total versus average emissions.
- [ ] Write down one insight from the sample dataset.

---

## 📝 7. Travel Practice Log

Use this section to record offline practice. Update it when you return to your computer.

| Date | Topic | What I Practiced | Doubts |
|---|---|---|---|
| | | | |
| | | | |
| | | | |
| | | | |
| | | | |

---

## 🎯 Final Reminder

**Consistency over perfection. Progress over promises.**

Use travel time to revise concepts, trace code by hand, and strengthen your understanding. Record any changes you make later in the main repository.

