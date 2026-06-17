# 📊 Sentiment Analysis Dashboard


An interactive dashboard built with Streamlit to analyze customer review sentiment. The project converts raw text into actionable insights by combining NLP sentiment scoring, polarity and subjectivity analysis, and data visualization.

---

## 🧾 Executive Summary (For Hiring Managers)

* ✅ Built an **interactive sentiment scoring dashboard** for customer feedback
* ✅ Used **VADER** for sentiment classification and **TextBlob** for polarity/subjectivity
* ✅ Added **live text cleaning** and **real-time user input analysis**
* ✅ Visualized sentiment distribution and presented results in a clean dashboard format

If you only have a minute, review these:

1. `project1/ana.py` — Streamlit app and sentiment analysis implementation
2. `project1/Reviews intern.csv` — review dataset used for analysis

---

## 🧩 Problem & Context

Modern businesses need fast, reliable insight into customer feedback. This project answers:

* 📌 Is customer feedback mostly positive, neutral, or negative?
* 🧠 How subjective is the text?
* 🔧 How can raw review text be cleaned and prepared for analysis?

The dashboard was built to help teams quickly classify sentiment, understand text quality, and review sentiment patterns in a simple UI.

---

## 🧰 Tech Stack

* 🐍 **Language:** Python
* 🌐 **Dashboard:** Streamlit
* 📦 **Libraries:** Pandas, TextBlob, VADER, cleantext, Matplotlib
* 🛠️ **Development:** VS Code
* 📦 **Version Control:** Git & GitHub

---

## 📂 Repository Structure

```text
project1/
├── ana.py
├── Reviews intern.csv
└── README.md
```

---

## 🏗 Analysis Overview

### 1. Sentiment scoring with VADER

The app calculates VADER sentiment scores for each review and classifies them into:
- highly positive
- positive
- neutral
- negative
- highly negative

### 2. Polarity and subjectivity with TextBlob

Each review is also evaluated for:
- **polarity** — how positive or negative the text is
- **subjectivity** — how subjective vs objective the language is

### 3. Live text cleaning and user input analysis

The dashboard allows users to type custom feedback and:
- view cleaned text using `cleantext`
- see current sentiment classification and scores
- compare VADER and TextBlob outputs instantly

### 4. Visualization

The dashboard displays:
- sentiment distributions by class
- histograms of sentiment scores
- a data table showing review text, scores, and subjectivity

---

## 📊 Key Insights

* Customer reviews can be quickly categorized to highlight overall opinion trends.
* Combining VADER and TextBlob provides broader insight into both sentiment and text quality.
* A simple interactive app makes sentiment analysis accessible to business stakeholders.

---

## 🧪 NLP Skills Demonstrated

### Text Processing
* Loading and exploring text data with Pandas
* Cleaning user-entered text for analysis
* Applying rule-based sentiment scoring

### Sentiment Analysis
* Using VADER for robust sentiment classification
* Using TextBlob for polarity and subjectivity metrics

### Dashboard Development
* Building a Streamlit app for interactive analytics
* Designing a user input workflow for live model feedback
* Displaying charts and tables in a responsive interface

---

## 🎯 What I Learned

This project helped me practice:
* turning raw customer feedback into structured sentiment insights
* combining multiple NLP tools to improve analysis quality
* building a polished, user-friendly analytics app in Streamlit
* interpreting sentiment and subjectivity for business decisions

---

## 🚀 How to Run

```bash
pip install streamlit pandas textblob vaderSentiment cleantext matplotlib
streamlit run ana.py
```

Open the URL displayed by Streamlit in your browser, then enter review text to see sentiment scores and cleaned output.
