# Diabetes Dataset – Data Cleaning & Classification

This project focuses on data preprocessing, cleaning, and model training on the **Pima Indians Diabetes Dataset**. The primary goal is to demonstrate effective data cleaning strategies followed by the application of various classification algorithms for diabetes prediction.

## Project Report

You can read the full project report [here : Comprative-analysis-diabetes.pdf](https://github.com/user-attachments/files/21584972/Comprative-analysis-diabetes.pdf)


---

## Dataset Description

The dataset contains medical records of 768 female patients and includes the following features:

- **Pregnancies**
- **Glucose**
- **BloodPressure**
- **SkinThickness**
- **Insulin**
- **BMI**
- **DiabetesPedigreeFunction**
- **Age**
- **Outcome** (1 for diabetic, 0 for non-diabetic)

## Data Cleaning Steps

1. **Identified invalid values (zeros) in several features**
2. **Replaced 0 values in key columns with `NaN`**
3. **Imputed `NaN` values using the mean of the feature**
4. **Inspected the dataset using `.describe()`**
5. **Detected and prepared for outlier removal**

## Machine Learning Algorithms Used

After cleaning, the dataset was used to train and evaluate multiple classification models:

- Support Vector Machine (SVM)
- K-Nearest Neighbors (KNN)
- Logistic Regression
- Decision Tree
- Gaussian Naive Bayes

## Evaluation Metrics

The models were assessed using:

- Accuracy Score
- Confusion Matrix
- Precision
- Recall
- F1 Score
- Mean Absolute Error

## Libraries Used

- `numpy`
- `pandas`
- `matplotlib`
- `seaborn`
- `sklearn` (scikit-learn)
