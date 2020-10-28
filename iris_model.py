# -*- coding: utf-8 -*-
"""
Created on Sat Oct 24 11:07:06 2020

@author: Venu Karpuram
"""
from sklearn import datasets


from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression,LogisticRegression
from sklearn.tree import DecisionTreeClassifier
import pickle

iris=datasets.load_iris()
#print(iris)
X=iris.data
y=iris.target

x_train,x_test,y_train,y_test=train_test_split(X,y)
lin_reg=LinearRegression()
KM_clustering=LogisticRegression()
decision_tree = DecisionTreeClassifier(max_depth = 6,random_state = 0,criterion = "entropy")

lin_reg=lin_reg.fit(x_train,y_train)
KM_clustering=KM_clustering.fit(x_train,y_train)
decision_tree=decision_tree.fit(x_train, y_train)


pickle.dump(lin_reg,open('neuron_model.pkl','wb'))
pickle.dump(KM_clustering,open('kmc_model.pkl','wb'))
pickle.dump(decision_tree,open('decision_model.pkl','wb'))
