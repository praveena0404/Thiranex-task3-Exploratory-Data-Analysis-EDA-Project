# Exploratory Data Analysis (EDA) Project

## Overview
This project explores the Diabetes Disease Progression dataset to uncover patterns, trends, correlations and potentially influential features.

## Dataset
The local CSV is exported from scikit-learn's built-in diabetes dataset, so no additional dataset download is needed. It has 442 rows, 10 input features and one target variable.

## Workflow
1. Load and inspect the data
2. Check duplicates and missing values
3. Generate descriptive statistics
4. Analyze correlations
5. Create visualizations
6. Summarize findings in `EDA_Report.txt`

## Visualizations
- Target distribution
- BMI distribution
- BMI vs target
- Age vs target
- Correlation heatmap

## Key findings
- `bmi` has the strongest absolute correlation with target (0.586).
- `s5` has the second strongest correlation (0.566).
- Correlation shows association and does not prove causation.

## Folder structure
```text
EDA_Project/
├── dataset/diabetes_dataset.csv
├── outputs/
│   ├── target_distribution.png
│   ├── bmi_distribution.png
│   ├── bmi_vs_target.png
│   ├── age_vs_target.png
│   ├── correlation_heatmap.png
│   ├── statistical_summary.csv
│   ├── missing_values.csv
│   └── correlation_matrix.csv
├── eda_analysis.py
├── EDA_Report.txt
├── requirements.txt
└── README.md
```

## Run in VS Code
```bash
pip install -r requirements.txt
python eda_analysis.py
```
