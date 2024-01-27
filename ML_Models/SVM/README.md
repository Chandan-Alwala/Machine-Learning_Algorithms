# Binary Equipment Failure Prediction using SVM

## Overview

This repository contains code for a Support Vector Machine (SVM) model designed to predict equipment failure. The model is trained on a dataset consisting of features related to equipment performance and labeled with binary failure indicators (0 or 1).

## Contents

1. **Data Files:**
   - `x_train.csv`: CSV file containing training data features.
   - `y_train.csv`: CSV file containing corresponding labels for the training data.
   - `x_test.csv`: CSV file containing testing data features.
   - `y_test.csv`: CSV file containing corresponding labels for the testing data.

2. **Code Files:**
   - `SVM.py`: Python script implementing the SVM model for equipment failure prediction.
  
## Prerequisites

- Ensure you have Python installed (preferably Python 3.x).
- Install necessary libraries using `pip install scikit-learn numpy`.

## Usage

1. **Data Preparation:**
   - Place the training and testing data files (`x_train.csv`, `y_train.csv`, `x_test.csv`, `y_test.csv`) in the same directory as the script.

2. **Run the Script:**
   - Execute the script `SVM.py` to train the SVM model and evaluate its performance.

3. **Results:**
   - The script will display information about the training and testing datasets, pre-processing steps, and the SVM model's accuracy on the testing data.

## Script Details

- The script uses the `scikit-learn` library for SVM model implementation, feature scaling, and feature selection.
- It employs a radial basis function (RBF) kernel with specified parameters (C, gamma, degree).
- Feature scaling is performed using Min-Max scaling, and feature selection is applied using the SelectKBest method with ANOVA F-statistic as the scoring function.

## Dataset Information

- The dataset consists of equipment-related features, and the goal is to predict equipment failure (binary: 0 or 1).
- Features include numerical measurements related to equipment performance.

## Note

- The code assumes the input data is in a specific format with features and labels separated into different files.


