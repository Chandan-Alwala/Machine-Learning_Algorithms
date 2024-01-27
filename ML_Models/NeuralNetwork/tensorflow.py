import tensorflow as tf 
import numpy as np 
import random 
import matplotlib.pyplot as plt 
import os
os.environ['TF_DETERMINISTIC_OPS'] = '1' #disable certain non-deterministic operations in TensorFlow

# set the random seeds to make sure your results are reproducible
from numpy.random import seed
seed(1)
tf.random.set_seed(1)
np.random.seed(1)
random.seed(1)

# specify path to training data and testing data
train_x_location = "x_train.csv"
train_y_location = "y_train.csv"
test_x_location = "x_test.csv"
test_y_location = "y_test.csv"

print("Processing the training data")
x_train = np.loadtxt(train_x_location,  delimiter=",")
y_train = np.loadtxt(train_y_location,  delimiter=",")

m, n = x_train.shape # m training examples, each with n features
m_labels,  = y_train.shape # m examples, each with k labels
l_min = y_train.min()

assert m_labels == m, "x_train and y_train should have same length."
assert l_min == 0, "each label should be in the range 0 - k-1."
k = y_train.max()+1

print("There are ",m, "examples,", n, "features,", k, "categories.")

def plot_performance(history):
    #plotting accuracy, traing loss ,validation losses w.r.t epochs
    acc = history.history['accuracy']
    loss = history.history['loss']
    epochs = range(len(acc))
    plt.plot(epochs, acc, 'b', label='Training acc')
    plt.plot(epochs, loss, 'r', label='Training loss')
    plt.title('Trainng')
    plt.legend()
    plt.show()

# define the training model
model = tf.keras.models.Sequential([
    # input_shape should be specified in the first layer
    tf.keras.layers.Dense(5, activation=tf.keras.activations.relu,
                          input_shape=(n,)),
    # another layer
    tf.keras.layers.Dense(5, activation=tf.keras.activations.relu),
    # another layer with l2 regularization
    tf.keras.layers.Dense(5, activation=tf.nn.relu,
                        kernel_regularizer=tf.keras.regularizers.l2(0.1)),
    #Batch Normalization
    tf.keras.layers.BatchNormalization(
    axis=-1,
    momentum=0.099,
    epsilon=0.001,
    center=True,
    scale=True,
    beta_initializer='zeros',
    gamma_initializer='ones',
    moving_mean_initializer='zeros',
    moving_variance_initializer='ones',
    beta_regularizer=None,
    gamma_regularizer=None,
    beta_constraint=None,
    gamma_constraint=None
    ),
    # dropouts layer
    tf.keras.layers.Dropout(0.5),
    # last layer is softmax
    tf.keras.layers.Dense(k, activation=tf.nn.softmax)
])

model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

print("train")
history = model.fit(x_train, y_train, epochs=2000, batch_size=32, verbose=0)

print("Reading the testing data")
x_test = np.loadtxt(test_x_location, delimiter=",")
y_test = np.loadtxt(test_y_location, delimiter=",")

m_test, n_test = x_test.shape
m_test_labels,  = y_test.shape
l_min = y_train.min()
assert m_test_labels == m_test, "x_test and y_test should have same length."
assert n_test == n, "train and x_test should have same number of features."

print("There are a total of ",m_test, "test examples.")

print("evaluating")
acc=model.evaluate(x_test, y_test)
del model
print("accuracy is:",acc)
print("end")
plot_performance(history)

