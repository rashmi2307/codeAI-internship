# 🩺 Diabetes Data Analysis & Modeling



A notebook series that analyzes diabetes health indicators, builds predictive models, and explores statistical relationships in healthcare data.

---

## 🧾 Executive Summary (For Hiring Managers)

* ✅ Built a **healthcare-focused analytical pipeline** using real diabetes indicator data
* ✅ Performed **exploratory data analysis** and **visualization** to understand feature relationships
* ✅ Applied **statistical testing** such as ANOVA to compare health indicators by diabetes status
* ✅ Built **classification models** and evaluated them using ROC, confusion matrix, and classification reports

If you only have a minute, review these:

1. [`Data_Analysis_of_diabtes.ipynb`](./Data_Analysis_of_diabtes.ipynb) – main exploratory analysis and logistic regression modeling
2. [`Data_Visualization_Diabetes.ipynb`](./Data_Visualization_Diabetes.ipynb) – data visualization and correlation insights
3. [`ANOVA_Diabetes.ipynb`](./ANOVA_Diabetes.ipynb) – statistical comparison of health indicators by diabetes class
4. [`Performance_of_Classifier.ipynb`](./Performance_of_Classifier.ipynb) – classifier performance evaluation including Random Forest and metrics

---

## 🧩 Problem & Context

Healthcare teams want to identify patterns and risk factors associated with diabetes.

This project answers:

* 📌 Which health indicators are most strongly related to diabetes?
* 🧠 Can diabetes status be predicted using logistic regression and tree-based models?
* 📈 How do model performance and feature relationships compare across datasets?

The analysis is built for learners who want to understand healthcare analytics using real-world binary health data.

---

## 🧰 Tech Stack

* 🐍 **Language:** Python
* 📓 **Notebook:** Jupyter Notebook
* 📦 **Libraries:** Pandas, NumPy, Matplotlib, Seaborn, scikit-learn, statsmodels, Plotly
* 🛠️ **Development:** VS Code / Jupyter
* 📦 **Version Control:** Git & GitHub

---

## 📂 Repository Structure

```text
03 Diabetes Data Analysis & Modeling/
├── ANOVA_Diabetes.ipynb
├── Correlation_Diabetes.ipynb
├── Data_Analysis_of_diabtes.ipynb
├── Data_Visualization_Diabetes.ipynb
├── LogisticR_Diabetes.ipynb
├── Performance_of_Classifier.ipynb
└── README.md
```

---

## 🧪 Analysis Overview

### 1. Exploratory Data Analysis

The notebooks begin with data loading, dataset shape inspection, and descriptive statistics to understand the health indicators and diabetes distribution.

### 2. Correlation and Visualization

The analysis includes:
- correlation heatmaps
- histograms and scatter plots
- count plots and pie charts
- cross-tab analysis of health indicators vs diabetes status

### 3. Statistical Testing

ANOVA is used to compare health indicator distributions across diabetes and non-diabetes groups.

### 4. Predictive Modeling

The notebooks include:
- logistic regression modeling for diabetes status
- Random Forest classification and performance comparison
- model validation with accuracy, ROC curves, confusion matrices, and classification reports

---

## 📊 Key Insights

* Certain health indicators such as BMI, high blood pressure, and cholesterol show strong relationships with diabetes.
* Visualization helps identify how risk factors differ between diabetic and non-diabetic groups.
* Logistic regression provides a transparent baseline, while tree-based models show additional predictive power.
* Combining EDA, statistics, and modeling creates a strong analytical narrative for healthcare data.

---

## 🧪 Skills Demonstrated

### Data Analysis
* feature exploration
* correlation analysis
* data visualization

### Statistical Techniques
* ANOVA
* group comparison
* hypothesis interpretation

### Modeling & Evaluation
* logistic regression
* Random Forest classification
* ROC curve analysis
* confusion matrix and classification reporting

---

## 🎯 What I Learned

This project helped me practice:
* interpreting healthcare data through the lens of diabetes risk factors
* combining statistical inference with machine learning modeling
* explaining model performance using intuitive metrics and plots
* structuring analytical notebooks for reproducibility and insight delivery

---

## 🚀 How to Run

Open the notebooks in Jupyter Notebook, JupyterLab, or Google Colab, then run the cells in order.

```bash
pip install pandas numpy matplotlib seaborn scikit-learn statsmodels plotly
```

---

## Note
The diabetes dataset is loaded remotely from a public CSV URL, so internet access is required during notebook execution.
