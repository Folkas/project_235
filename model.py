#importing data
from sklearn.datasets import load_boston
data = load_boston()

#training the regression model
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(data.data, data.target)

from sklearn.linear_model import LinearRegression
clf = LinearRegression()
clf.fit(X_train, y_train)


#evaluating the trained model
from sklearn.metrics import mean_squared_error, r2_score
import numpy as np

predicted = clf.predict(X_test)
expected = y_test

print(f"Mean Squared Error: {mean_squared_error(expected, predicted)}")
print(f"R2 Score: {r2_score(expected, predicted)}")
print("RMS: %r " % np.sqrt(np.mean((predicted - expected) ** 2)))

#saving model to file
import pickle

pickle.dump(clf, open("lregression.pkl", "wb"))

# [4.0974e+00, 0.0000e+00, 1.9580e+01, 0.0000e+00, 8.7100e-01, 5.4680e+00, 1.0000e+02, 1.4118e+00, 5.0000e+00, 4.0300e+02,
        # 1.4700e+01, 3.9690e+02, 2.6420e+01]




