# 📚 Book Search Utility


A command-line utility that searches book metadata for matching titles, authors, or publishers using a simple keyword search.

---

## 🧾 Executive Summary (For Hiring Managers)

* ✅ Built a **data-driven search tool** for book metadata exploration
* ✅ Implemented **keyword search across title, author, and publisher fields**
* ✅ Displayed **clean, easy-to-read book details** for matched results
* ✅ Demonstrated how to build a small utility around structured CSV data

If you only have a minute, review these:

1. [`app.py`](./app.py) – command-line program implementing the search interface
2. [`books.csv`](./books.csv) – dataset used for search queries

---

## 🧩 Problem & Context

Readers and analysts often need a fast way to locate books that match certain search terms. This project builds a small tool to answer:

* 🔎 Which books match the user's search keyword?
* 🧭 Can search results include title, author, and publisher matches?
* 📚 How can book metadata be surfaced clearly in a terminal interface?

The utility is designed for learners who want a practical example of CSV-based search and dataset exploration.

---

## 🧰 Tech Stack

* 🐍 **Language:** Python
* 📦 **Library:** Pandas
* 🛠️ **Development:** VS Code / any Python editor
* 📦 **Version Control:** Git & GitHub

---

## 📂 Repository Structure

```text
04 Book Search Utility/
├── app.py
├── books.csv
└── README.md
```

---

## 🏗 Analysis Overview

### 1. Text search across metadata

The app loads `books.csv` and searches for the user keyword in:
- `title`
- `authors`
- `publisher`

### 2. Result formatting

When matches are found, the app displays:
- book title
- author name(s)
- average rating
- ISBN / ISBN13
- language code
- page count
- ratings and reviews count
- publication date
- publisher

### 3. User interaction loop

The script prompts the user for a keyword and prints results in a readable format. This makes it easy to interact with the dataset without a graphical interface.

---

## 📊 Key Insights

* Simple keyword matching can make structured datasets accessible quickly.
* CSV data can support lightweight search tools without heavy infrastructure.
* A well-formatted terminal output improves usability for non-GUI scripts.

---

## 🧪 Skills Demonstrated

### Data exploration
* loading and filtering CSV data with Pandas
* working with text fields for search

### Tool development
* creating a simple command-line user experience
* displaying tabular information cleanly in the terminal

---

## 🎯 What I Learned

This project helped me practice:
* building a practical utility around structured dataset search
* applying Python and Pandas to interactive CLI workflows
* formatting complex object metadata for user-friendly display

---

## 🚀 How to Run

```bash
pip install pandas
python app.py
```

Enter a keyword at the prompt to search the book dataset.
