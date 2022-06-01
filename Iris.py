from sklearn.svm import SVC

from sklearn.datasets import load_iris

from sklearn.datasets import make_classification

from sklearn.model_selection import train_test_split

from sklearn.model_selection import cross_val_score

from sklearn.metrics import confusion_matrix

from sklearn.metrics import classification_report

 

x, y = make_classification(n_samples=5000, n_features=10,

                           n_classes=3,

                           n_clusters_per_class=1)

 

xtrain, xtest, ytrain, ytest=train_test_split(x, y, test_size=0.15)

 

svc = SVC()

print(svc)

 

svc.fit(xtrain, ytrain)

score = svc.score(xtrain, ytrain)

print("Score: ", score)

 

cv_scores = cross_val_score(svc, xtrain, ytrain, cv=10)

print("CV average score: %.2f" % cv_scores.mean())

 

ypred = svc.predict(xtest)

 

cm = confusion_matrix(ytest, ypred)

print(cm)

 

cr = classification_report(ytest, ypred)

print(cr)

 

 

# Iris dataset classification

print("Iris dataset classification with SVC")

iris = load_iris()

x, y = iris.data, iris.target

xtrain, xtest, ytrain, ytest=train_test_split(x, y, test_size=0.15)

 

svc = SVC()

print(svc)

 

svc.fit(xtrain, ytrain)

score = svc.score(xtrain, ytrain)

print("Score: ", score)

 

cv_scores = cross_val_score(svc, xtrain, ytrain, cv=10)

print("CV average score: %.2f" % cv_scores.mean())

 

ypred = svc.predict(xtest)

 

cm = confusion_matrix(ytest, ypred)

print(cm)

 

cr = classification_report(ytest, ypred)

print(cr)
