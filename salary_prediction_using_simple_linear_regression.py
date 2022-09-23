# -*- coding: utf-8 -*-
"""Salary Prediction Using simple linear regression.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1fpJe0ObBvLANtejHyKA5PwI69Z7yB1eo
"""

import pandas as pd
import numpy as np
import io
import matplotlib.pyplot as plt
import seaborn as sb
import sklearn as sk

from google.colab import files
uploaded = files.upload()

data = pd.read_csv("Salary_Data.csv")
data

x = data.iloc[:,:-1].values
y = data.iloc[:,1].values

from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.2,random_state=0)

from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
regressor = LinearRegression()
regressor.fit(x_train,y_train)
y_pred = regressor.predict(x_test)
y_pred
y_test
plt.scatter(x_train,y_train,color='red')
plt.plot(x_train,regressor.predict(x_train),color='blue')
plt.title("Salary vs Experience (Training set)")
plt.xlabel("Years of experience")
plt.ylabel("Salaries")
plt.show()