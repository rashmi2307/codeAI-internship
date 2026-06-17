# Cloud ML Discovery Series Projects

An engaging portfolio of four machine learning and data science mini-projects completed during the **Cloud ML Discovery Series** internship.


---

## Projects Overview

### 1. Sentiment Analysis Dashboard (`project1`)

**What it is**
An interactive sentiment analysis app that reads customer review text and generates instant insights using VADER and TextBlob.

**Why it matters**
- Converts raw text into meaningful sentiment categories
- Illustrates how to deploy model output in a dashboard
- Covers both NLP preprocessing and visual storytelling

**Skills**
Streamlit, NLP, sentiment analysis, text cleaning, visualization

**Key files**
- `project1/ana.py`
- `project1/Reviews intern.csv`

**Run it**
```bash
pip install streamlit pandas textblob vaderSentiment cleantext matplotlib
streamlit run project1/ana.py
```

---

### 2. Student Study Performance Modeling (`project2`)

**What it is**
A notebook-based analysis of student scores that combines regression and classification modeling with real school performance data.

**Why it matters**
- Shows how to preprocess categorical variables for ML
- Demonstrates predicting numeric outcomes and classification labels in one workflow
- Provides a complete analysis from raw data to predictions

**Skills**
pandas, scikit-learn, regression, classification, EDA, feature engineering

**Key files**
- `project2/proj_2.ipynb`
- `project2/study_performance.csv`

**Run it**
Open `project2/proj_2.ipynb` in Jupyter Notebook, JupyterLab, or Colab and execute the cells.

---

### 3. Diabetes Data Analysis & Modeling (`project3`)

**What it is**
A series of notebooks that explore diabetes health indicators, perform statistical analysis, and train classification models.

**Why it matters**
- Combines exploratory data analysis with modeling and evaluation
- Uses healthcare data to demonstrate responsible analytics
- Includes statistical testing such as ANOVA and performance evaluation with ROC curves

**Skills**
EDA, data visualization, statistical inference, logistic regression, Random Forest, model validation

**Key files**
- `project3/Data_Analysis_of_diabtes.ipynb`
- `project3/Data_Visualization_Diabetes.ipynb`
- `project3/Correlation_Diabetes.ipynb`
- `project3/ANOVA_Diabetes.ipynb`
- `project3/LogisticR_Diabetes.ipynb`
- `project3/Performance_of_Classifier.ipynb`

**Run it**
Open any notebook in `project3` using Jupyter Notebook or JupyterLab and run the analysis cells. Internet access is required for the remote dataset.

---

### 4. Book Search Utility (`project4`)

**What it is**
A lightweight command-line book search tool that finds matching titles, authors, and publishers from a metadata dataset.

**Why it matters**
- Demonstrates practical data filtering and search logic
- Shows how to build a useful instrument around CSV data
- Is easy to modify into a more advanced recommendation tool

**Skills**
Python, pandas, CLI design, string matching, data exploration

**Key files**
- `project4/app.py`
- `project4/books.csv`

**Run it**
```bash
pip install pandas
python project4/app.py
```

---

## What I learned
- How to design and ship an interactive data application with Streamlit.
- How to preprocess datasets and apply regression and classification models.
- How to interpret model performance using accuracy, confusion matrices, and ROC curves.
- How to visualize data in clear, recruiter-friendly formats.
- How to combine statistical analysis with machine learning in real projects.
- How to structure code and notebooks for reuse and learning.


---

## Notes
- `project1/ana.py` is a Streamlit web app; it should be launched with `streamlit run`.
- `project2/proj_2.ipynb` and the notebooks in `project3` are designed for interactive analysis.
- `project3` notebooks use a remote CSV URL; internet access is required to load the dataset.
- `project4/app.py` is a console-based search tool and uses `project4/books.csv` locally.




