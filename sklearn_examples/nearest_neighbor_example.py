import numpy as np
from sklearn import datasets
iris = datasets.load_iris()
iris_X = iris.data
iris_y = iris.target
print np.unique(iris_y)
#array([0, 1, 2])
# Split iris data in train and test data
# A random permutation, to split the data randomly
np.random.seed(0)
indices = np.random.permutation(len(iris_X))
iris_X_train = iris_X[indices[:-10]]
iris_y_train = iris_y[indices[:-10]]
iris_X_test  = iris_X[indices[-10:]]
iris_y_test  = iris_y[indices[-10:]]
# Create and fit a nearest-neighbor classifier
from sklearn.neighbors import KNeighborsClassifier
knn = KNeighborsClassifier()
print knn.fit(iris_X_train, iris_y_train)
# KNeighborsClassifier(algorithm='auto', leaf_size=30, metric='minkowski', n_neighbors=5, p=2, weights='uniform')
print knn.predict(iris_X_test)
# array([1, 2, 1, 0, 0, 0, 2, 1, 2, 0])
print iris_y_test
# array([1, 1, 1, 0, 0, 0, 2, 1, 2, 0])