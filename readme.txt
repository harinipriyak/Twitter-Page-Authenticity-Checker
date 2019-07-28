README.txt

TO BE INSTALLED
.-----------------
-Python 3.0
-Anaconda
-Flask

LIBRARIES TO BE INSTALLED
-----------------------------
-from pandas.plotting import scatter_matrix
-import matplotlib.pyplot as plt
-from sklearn import model_selection
-from sklearn.model_selection import train_test_split
-from sklearn.metrics import classification_report
-from sklearn.metrics import confusion_matrix
-from sklearn.metrics import accuracy_score
-from sklearn.linear_model import LogisticRegression
-from sklearn.tree import DecisionTreeClassifier
-from sklearn.neighbors import KNeighborsClassifier
-from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
-from sklearn.naive_bayes import GaussianNB
-from sklearn.svm import SVC
-from sklearn.externals import joblib
-from sklearn.preprocessing import LabelBinarizer
-from keras.models import Sequential
-from keras.layers import Dense, Dropout, Embedding, LSTM
-import numpy
-import tweepy
-import json
-import xlrd
-from openpyxl import load_workbook
-from flask import Flask, redirect, url_for, request, render_template
-from keras.models import model_from_json


RUN PROCEDURE
------------------
-Download dataset of Twitter URLs
-Change path name of dataset in dataset_writer.py accordingly
-Run dataset_writer.py to fill attributes in dataset
-Change path name of dataset accordingly in required training model file
-Run required training model file
-Use the saved trained model in load_model() method in app.py

FOR EXECUTION
-----------------
-Run app.py