# Cloud ML Discovery Series Projects

An engaging portfolio of four machine learning and data science mini-projects completed during the **Cloud ML Discovery Series** internship.

Each project includes practical code, real datasets, and recruiter-friendly summaries.

---

## 🚀 Projects Overview

### 1. Sentiment Analysis Dashboard 

**What it is**
An interactive sentiment analysis app that reads customer review text and generates instant insights using VADER and TextBlob.

**Why it matters**
- Converts raw text into meaningful sentiment categories
- Demonstrates how to deploy model output in a dashboard
- Covers NLP preprocessing and visual storytelling

**Skills**
Streamlit, NLP, sentiment analysis, text cleaning, visualization

**Key files**
- [ana.py](./01%20Sentiment%20Analysis%20Dashboard/ana.py)
- [Reviews intern.csv](./01%20Sentiment%20Analysis%20Dashboard/Reviews%20intern.csv)
- [README.md](./01%20Sentiment%20Analysis%20Dashboard/README.md)

**Run it**
```bash
pip install streamlit pandas textblob vaderSentiment cleantext matplotlib
streamlit run "01 Sentiment Analysis Dashboard/ana.py"
```

---

### 2. Student Study Performance Modeling 

**What it is**
A notebook-based analysis of student scores that combines regression and classification modeling with real school performance data.

**Why it matters**
- Shows how to preprocess categorical variables for ML
- Demonstrates predicting numeric outcomes and classification labels in one workflow
- Provides a complete analysis from raw data to predictions

**Skills**
pandas, scikit-learn, regression, classification, EDA, feature engineering

**Key files**
- [proj_2.ipynb](./02%20Student%20Study%20Performance%20Modeling/proj_2.ipynb)
- [study_performance.csv](./02%20Student%20Study%20Performance%20Modeling/study_performance.csv)
- [README.md](./02%20Student%20Study%20Performance%20Modeling/README.md)

**Run it**
Open [proj_2.ipynb](./02%20Student%20Study%20Performance%20Modeling/proj_2.ipynb) in Jupyter Notebook, JupyterLab, or Colab and execute the cells.

---

### 3. Diabetes Data Analysis & Modeling 

**What it is**
A series of notebooks that explore diabetes health indicators, perform statistical analysis, and train classification models.

**Why it matters**
- Combines exploratory data analysis with modeling and evaluation
- Uses healthcare data to demonstrate responsible analytics
- Includes statistical testing such as ANOVA and performance evaluation with ROC curves

**Skills**
EDA, data visualization, statistical inference, logistic regression, Random Forest, model validation

**Key files**
- [Data_Analysis_of_diabtes.ipynb](./03%20Diabetes%20Data%20Analysis%20&%20Modeling/Data_Analysis_of_diabtes.ipynb)
- [Data_Visualization_Diabetes.ipynb](./03%20Diabetes%20Data%20Analysis%20&%20Modeling/Data_Visualization_Diabetes.ipynb)
- [Correlation_Diabetes.ipynb](./03%20Diabetes%20Data%20Analysis%20&%20Modeling/Correlation_Diabetes.ipynb)
- [ANOVA_Diabetes.ipynb](./03%20Diabetes%20Data%20Analysis%20&%20Modeling/ANOVA_Diabetes.ipynb)
- [LogisticR_Diabetes.ipynb](./03%20Diabetes%20Data%20Analysis%20&%20Modeling/LogisticR_Diabetes.ipynb)
- [Performance_of_Classifier.ipynb](./03%20Diabetes%20Data%20Analysis%20&%20Modeling/Performance_of_Classifier.ipynb)
- [README.md](./03%20Diabetes%20Data%20Analysis%20&%20Modeling/README.md)

**Run it**
Open any of the notebooks in [03 Diabetes Data Analysis & Modeling](./03%20Diabetes%20Data%20Analysis%20&%20Modeling/README.md) using Jupyter Notebook or JupyterLab and run the analysis cells. Internet access is required for the remote dataset.

---

### 4. Book Search Utility 

**What it is**
A lightweight command-line book search tool that finds matching titles, authors, and publishers from a metadata dataset.

**Why it matters**
- Demonstrates practical data filtering and search logic
- Shows how to build a useful tool around CSV data
- Is easy to modify into a more advanced recommendation tool

**Skills**
Python, pandas, CLI design, string matching, data exploration

**Key files**
- [app.py](./04%20Book%20Search%20Utility/app.py)
- [books.csv](./04%20Book%20Search%20Utility/books.csv)
- [README.md](./04%20Book%20Search%20Utility/README.md)

**Run it**
```bash
pip install pandas
python "04 Book Search Utility/app.py"
```

---

## ✨ What I learned
- How to design and ship an interactive data application with Streamlit.
- How to preprocess datasets and apply regression and classification models.
- How to interpret model performance using accuracy, confusion matrices, and ROC curves.
- How to visualize data in clear, recruiter-friendly formats.
- How to combine statistical analysis with machine learning in real projects.
- How to structure code and notebooks for reuse and learning.

---

## 📝 Notes
- [01 Sentiment Analysis Dashboard/README.md](./01%20Sentiment%20Analysis%20Dashboard/README.md) is a Streamlit app folder. Launch `ana.py` with `streamlit run`.
- [02 Student Study Performance Modeling/README.md](./02%20Student%20Study%20Performance%20Modeling/README.md) and [03 Diabetes Data Analysis & Modeling/README.md](./03%20Diabetes%20Data%20Analysis%20&%20Modeling/README.md) are interactive notebook folders.
- [03 Diabetes Data Analysis & Modeling](./03%20Diabetes%20Data%20Analysis%20&%20Modeling/README.md) requires internet access for the remote dataset.
- [04 Book Search Utility/README.md](./04%20Book%20Search%20Utility/README.md) is a console-based search tool using local CSV data.

