
***

# Day 25 – Working with CSV Files & Introduction to Pandas 🐼

## 📌 Overview

This lesson demonstrates how Python can be used to **automate repetitive data work** by reading and analyzing CSV (Comma Separated Values) files.  
It starts with **basic file handling**, moves to Python’s built‑in `csv` module, and then introduces **Pandas**, the industry‑standard library for working with tabular data efficiently.

---

## 📊 Dataset Used

The dataset represents **weather data** for one week.

### Columns:
- **day** → Day of the week
- **temp** → Temperature in Celsius
- **condition** → Weather description

### File name:
```

weather\_data.csv

````

### Example CSV structure:
```text
day,temp,condition
Monday,12,Sunny
Tuesday,14,Rain
Wednesday,15,Cloudy
````

The file was created in Google Sheets and downloaded as a CSV file.

***

## 📁 What is a CSV File?

**CSV (Comma Separated Values)** is a common format used for tabular data.

### Characteristics:

*   Each row represents one record
*   Values are separated by commas
*   Easy to create and share
*   Widely used in:
    *   Data analysis
    *   Machine learning datasets
    *   Business reports
    *   Spreadsheet exports

***

## 🐍 Reading CSV Using Python File Handling

### Code:

```python
with open("weather_data.csv") as data_file:
    data = data_file.readlines()

print(data)
```

### Output:

*   A list of strings
*   Each line contains commas
*   All values are strings

⚠️ **Limitation**

*   Hard to extract columns
*   Requires heavy manual cleaning
*   Not scalable for large datasets

***

## 📦 Reading CSV Using Python’s `csv` Module

Python provides a built‑in library to handle CSV files more effectively.

### Code:

```python
import csv

with open("weather_data.csv") as data_file:
    data = csv.reader(data_file)
    for row in data:
        print(row)
```

### Output:

```python
['day', 'temp', 'condition']
['Monday', '12', 'Sunny']
['Tuesday', '14', 'Rain']
```

✅ Advantages:

*   Each row becomes a list
*   Values are separated automatically
*   Easier access using indexes

***

## 🔍 Extracting Temperature Values (Challenge)

### Goal:

Create a list of temperatures as integers:

```python
[12, 14, 15, ...]
```

### Solution:

```python
import csv

temperatures = []

with open("weather_data.csv") as data_file:
    data = csv.reader(data_file)
    for row in data:
        if row[1] != "temp":
            temperatures.append(int(row[1]))

print(temperatures)
```

### Key Points:

*   `row[1]` accesses the temperature column
*   Header row (`temp`) is skipped
*   Strings are converted to integers using `int()`

***

## ⚠️ Why This Approach Becomes a Problem

Even with the `csv` module:

*   Code becomes verbose
*   More columns = more complexity
*   Manual filtering and conversions grow quickly
*   Not ideal for real‑world data analysis

➡️ **This leads to Pandas.**

***

## 🐼 Introduction to Pandas

### What is Pandas?

Pandas is a **powerful Python library for data analysis**, designed specifically to work with **tabular data** such as CSV files.

### Widely used in:

*   Data Science
*   Machine Learning
*   Business Analytics
*   Automation & Reporting

> Most Python developers immediately use Pandas when working with CSV files.

***

## 📦 Installing Pandas

Pandas is not a built‑in library.

### Install in PyCharm:

```python
import pandas
```

Hover over the red underline → **Install package `pandas`**

***

## 📚 Pandas Documentation

Official website:

    https://pandas.pydata.org

Recommended sections:

*   Getting Started
*   User Guide
*   API Reference

✅ Always check the **Getting Started** guide when learning a new library.

***

## 📊 Reading CSV Using Pandas (One Line)

### Code:

```python
import pandas

data = pandas.read_csv("weather_data.csv")
print(data)
```

### Output:

*   Formatted table
*   Column headers detected automatically
*   Rows indexed automatically

Example:

           day  temp condition
    0   Monday    12     Sunny
    1  Tuesday   14      Rain

***

## 🎯 Accessing a Single Column Using Pandas

### Code:

```python
print(data["temp"])
```

✅ No loops  
✅ No manual parsing  
✅ Clean and readable

Pandas automatically understands column names from the CSV header.

***

## 🔥 CSV Module vs Pandas

| Feature        | csv Module | Pandas    |
| -------------- | ---------- | --------- |
| Ease of Use    | Medium     | Very Easy |
| Code Length    | Long       | Short     |
| Readability    | Average    | Excellent |
| Scalability    | Poor       | Excellent |
| Industry Usage | Limited    | Standard  |

✅ Pandas is the **preferred tool** for working with CSV data in Python.

***

## ✅ Key Takeaways

*   CSV files store structured tabular data
*   Python’s `csv` module works but does not scale well
*   Pandas:
    *   Simplifies data access
    *   Improves readability
    *   Is faster and more powerful
*   Pandas is the **industry standard** for Python data analysis

***

## 🔜 What’s Next

In the next lesson:

*   Deeper exploration of Pandas
*   Understanding DataFrames and Series
*   Performing real‑world data analysis tasks

***

## 💬 Author’s Note

This lesson highlights an important programming mindset:

> Don’t do manually what a computer can automate.

Learning the **right tools** is just as important as learning Python syntax.

```

---

If you want next:
✅ **Day‑26 README**  
✅ Repo structure suggestions  
✅ `requirements.txt`  
✅ Interview questions from this lesson  
✅ Add exercises section  

Just tell me 👍
```
