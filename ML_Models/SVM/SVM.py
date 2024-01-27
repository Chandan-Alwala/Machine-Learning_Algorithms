from sklearn import svm
from sklearn.preprocessing import MinMaxScaler
from sklearn.feature_selection import f_classif
from sklearn.feature_selection import SelectKBest
import numpy as np

# specify path to training data and testing data
train_x_location = "x_train.csv"
train_y_location = "y_train.csv"
test_x_location = "x_test.csv"
test_y_location = "y_test.csv"

print("Reading training data")
x_train = np.loadtxt(train_x_location, delimiter=",")
y_train = np.loadtxt(train_y_location, delimiter=",")

m, n = x_train.shape # m training examples, each with n features
m_labels,  = y_train.shape # m2 examples, each with k labels
l_min = y_train.min()

assert m_labels == m, "x_train and y_train should have same length."
assert l_min == 0, "each label should be in the range 0 - k-1."
k = y_train.max()+1

print(m, "examples,", n, "features,", k, "categories.")

print("Reading testing data")
x_test = np.loadtxt(test_x_location, delimiter=",")
y_test = np.loadtxt(test_y_location, delimiter=",")

m_test, n_test = x_test.shape
m_test_labels,  = y_test.shape

assert m_test_labels == m_test, "x_test and y_test should have same length."
assert n_test == n, "train and x_test should have same number of features."

print(m_test, "test examples.")

# ====================================
# STEP 2: pre processing
print("Pre processing data")

scaler = MinMaxScaler()
x_train = scaler.fit_transform(x_train)
x_test = scaler.transform(x_test)

k = 5  # number of top features to select
selector = SelectKBest(f_classif, k=k)
x_train = selector.fit_transform(x_train, y_train)
x_test = selector.transform(x_test)

# ====================================
# STEP 3: train model.

print("---train---")

C = 2
kernel = 'rbf'
gamma = 'scale'
degree = 2
model = svm.SVC(C=C, kernel=kernel, degree=degree, gamma=gamma)
model.fit(x_train, y_train)

# ====================================
# STEP3: evaluate model

print("---evaluate---")
print("number of support vectors: ", model.n_support_)
acc = model.score(x_test, y_test)
print("accuracy is:", acc)

