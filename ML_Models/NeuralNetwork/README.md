# Equipment Failure Prediction Model Readme

## Overview
This repository contains code for a machine learning model built using TensorFlow and Keras to predict equipment failure based on input features. The model is trained on a dataset with labeled examples of equipment performance.

## Files
- **tensorflow.py**: This script loads training data, builds and trains a neural network model, and saves the trained model weights and gives the prediction.
- **x_train.csv**: CSV file containing training data features.
- **y_train.csv**: CSV file containing corresponding labels for the training data.
- **x_test.csv**: CSV file containing test data features.
- **y_test.csv**: CSV file containing corresponding labels for the test data.

## Setup
1. Install the required dependencies by running:
   ```bash
   pip install tensorflow numpy matplotlib
   ```
2. Run the file (`tensorflow.py`) to obtain the model accuracy. 

# Model Architecture
The model architecture is defined in the `train_model.py` script using TensorFlow and Keras. It consists of three dense layers with ReLU activation functions, a batch normalization layer, a dropout layer, and a final softmax layer for binary classification.

# Training
The model is trained using the Adam optimizer and sparse categorical crossentropy loss. The training process is logged, and the performance (accuracy and loss) is visualized using the `plot_performance` function in the script.

# Data
The training and testing data are loaded from CSV files (`x_train.csv`, `y_train.csv`, `x_test.csv`, `y_test.csv`). The data should be structured such that each row corresponds to a data example, with features in the input file and corresponding labels in the output file.

# Note
- Ensure that the CSV files have the correct format and are properly preprocessed.
- Adjust hyperparameters and model architecture as needed for specific use cases.
- Experiment with different training epochs and batch sizes for optimal model performance.

