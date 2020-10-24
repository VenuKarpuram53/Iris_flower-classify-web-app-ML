# -*- coding: utf-8 -*-
"""
Created on Sat Oct 24 11:07:06 2020

@author: Venu Karpuram
"""
from sklearn import datasets


from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression,LogisticRegression
from sklearn.svm import SVC,LinearSVC
from sklearn.tree import DecisionTreeClassifier
import pickle

iris=datasets.load_iris()
#print(iris)
X=iris.data
y=iris.target

x_train,x_test,y_train,y_test=train_test_split(X,y)
lin_reg=LinearRegression()
log_reg=LogisticRegression()
upport_VM=SVC(kernel='linear',probability=True)
decision_tree = DecisionTreeClassifier(max_depth = 6,random_state = 0,criterion = "entropy")

lin_reg=lin_reg.fit(x_train,y_train)
log_reg=log_reg.fit(x_train,y_train)
support_VM=support_VM.fit(x_train,y_train)
decision_tree=decision_tree.fit(x_train, y_train)


pickle.dump(lin_reg,open('neuron_model.pkl','wb'))
pickle.dump(log_reg,open('log_model.pkl','wb'))
pickle.dump(support_VM,open('svc_model.pkl','wb'))
pickle.dump(decision_tree,open('decision_model.pkl','wb'))
