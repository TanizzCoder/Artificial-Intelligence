import numpy as np

import matplotlib.pyplot as plt

import pandas as pd

 

# Importing the datasets

 

df = pd.read_csv('Social_Network_Ads.csv')

df.head()

 

df.shape

 

X = df.iloc[:, [2,3]]

Y = df.iloc[:, 4]

 

X.head()

 

Y.head()

 

# Splitting the dataset into the Training set and Test set

 

from sklearn.model_selection import train_test_split

X_Train, X_Test, Y_Train, Y_Test = train_test_split(X, Y, test_size = 0.25, random_state = 0)

 

print("Training data : ",X_Train.shape)

print("Training data : ",X_Test.shape)

 

# Feature Scaling

 

from sklearn.preprocessing import StandardScaler

sc_X = StandardScaler()

X_Train = sc_X.fit_transform(X_Train)

X_Test = sc_X.transform(X_Test)

 

from sklearn.svm import SVC

classifier = SVC(kernel = 'linear', random_state = 0)

classifier.fit(X_Train, Y_Train)

 

# Predicting the test set results

Y_Pred = classifier.predict(X_Test)

 

Y_Pred

 

from sklearn import metrics

print('Accuracy Score: with linear kernel')

 

print(metrics.accuracy_score(Y_Test,Y_Pred))

 

import matplotlib.pyplot as plt

 

plt.scatter(X_Train[:, 0], X_Train[:, 1],c=Y_Train) 

plt.xlabel('Age')

plt.ylabel('Estimated Salary')

plt.title('Training Data')

plt.show()

 

import matplotlib.pyplot as plt

 

 

plt.scatter(X_Test[:, 0], X_Test[:, 1],c=Y_Test) 

plt.xlabel('Age')

plt.ylabel('Estimated Salary')

plt.title('Test Data')

plt.show()

 
