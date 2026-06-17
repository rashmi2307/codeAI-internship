# 📘 Student Study Performance Modeling



A notebook-based analysis that explores student performance data and builds predictive models to understand how academic factors influence math scores and performance outcomes.

---

## 🧾 Executive Summary (For Hiring Managers)

* ✅ Built a **dual-model analysis** using both regression and classification
* ✅ Performed **feature engineering** on categorical school data
* ✅ Created **data visualizations** and exploratory analysis to explain model behavior
* ✅ Demonstrated the ability to turn raw student data into predictive insights

If you only have a minute, review these:

1. [`proj_2.ipynb`](./proj_2.ipynb) – Jupyter notebook containing the full analysis and modeling workflow
2. [`study_performance.csv`](./study_performance.csv) – dataset used for model training and exploration

---

## 🧩 Problem & Context

Students and educators want to know which factors most strongly influence math performance.

This project answers:

* 📌 What student attributes correlate with higher math scores?
* 🧠 Can math scores be predicted from reading and writing performance?
* 🎯 Can students be classified into high and low math performance groups?

The analysis is built for learners who want a clear introduction to regression and classification using real student data.

---

## 🧰 Tech Stack

* 🐍 **Language:** Python
* 📓 **Notebook:** Jupyter Notebook
* 📦 **Libraries:** Pandas, scikit-learn, NumPy, Matplotlib, Seaborn
* 🛠️ **Development:** VS Code / Jupyter
* 📦 **Version Control:** Git & GitHub

---

## 📂 Repository Structure

```text
02 Student Study Performance Modeling/
├── proj_2.ipynb
├── study_performance.csv
├── Pokemon.csv
└── README.md
```

---

## 🏗 Analysis Overview

### 1. Data Exploration

The notebook begins with data loading, validation, and summary statistics to understand the student dataset.

### 2. Feature Engineering

Categorical fields are label-encoded so models can learn from:
- gender
- race/ethnicity
- parental education level
- lunch type
- test preparation course status

### 3. Regression Modeling

Built a linear regression model to predict `math_score` from:
- `reading_score`
- `writing_score`

This demonstrates how to forecast continuous academic performance using related exam scores.

### 4. Classification Modeling

Built a logistic regression model to classify whether a student belongs to a high math performance group.

This demonstrates how to convert numeric targets into actionable categories.

---

## 📊 Key Insights

* Reading and writing scores are strong predictors of math performance.
* Categorical student attributes can be effectively encoded for model training.
* Regression and classification together provide a fuller understanding of performance outcomes.

---

## 🧪 Skills Demonstrated

### Data Science Workflow
* Data loading and inspection
* Dealing with categorical and numerical features
* Exploratory data analysis

### Modeling
* Linear regression for score prediction
* Logistic regression for performance classification
* Model evaluation and interpretation

### Visualization
* Plotting distributions and relationships with Matplotlib and Seaborn

---

## 🎯 What I Learned

This project helped me practice:
* engineering features from real-world categorical data
* building and comparing regression and classification models
* interpreting model results in the context of student performance
* structuring analysis in a notebook for easy review and reproducibility

---

## 🚀 How to Run

Open `proj_2.ipynb` in Jupyter Notebook, JupyterLab, or Google Colab, then run the cells in order.

```bash
pip install pandas scikit-learn numpy matplotlib seaborn
```


