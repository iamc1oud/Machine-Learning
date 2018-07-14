import numpy as np
import matplotlib.pyplot as plt
from sklearn import cross_validation
from utilities import visualize_classifier
from sklearn.naive_bayes import GaussianNB
# input file containing data
input_file = 'data_multivar_nb.txt'

# loading data
data = np.loadtxt(input_file, delimiter=',')
X, y = data[:,:-1], data[:, -1]

# Naive bayes classifier
classifier = GaussianNB()

# train the classifier
classifier.fit(X,y)

# predict the value for training data
y_pred = classifier.predict(X)

# accuracy
accuracy = 100.0 * (y==y_pred).sum()/X.shape[0]
print("Accuracy of naive bayes classifier =", round(accuracy,2),"%")

# visualize
visualize_classifier(classifier, X, y)

# splitting data
X_train, y_train, X_test, y_test = cross_validation.train_test_split(X,y,test_size=0.2,random_state=3)
classifier_new = GaussianNB()
classifier_new.fit(X_train, y_train)
y_test_pred = classifier_new.predict(X_test)



