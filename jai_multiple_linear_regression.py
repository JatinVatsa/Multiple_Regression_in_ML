#Multiple linear regression

#importing libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# importing data set
dataset = pd.read_csv('50_Startups.csv')
X=dataset.iloc[:,0:-1].values
Y=dataset.iloc[:,-1].values

#encoding categorical data
from sklearn.preprocessing import LabelEncoder,OneHotEncoder
from sklearn.compose import ColumnTransformer
label=LabelEncoder()
X[:,3]=label.fit_transform(X[:,3])
ct=ColumnTransformer([('State',OneHotEncoder(),[3])],remainder='passthrough')
X=ct.fit_transform(X)

#avoiding dummy variable trap
X=X[:,1:]
X=np.array(X,dtype=float)

#splitting the dataset into training set and test set
from sklearn.model_selection import train_test_split
X_train,X_test,Y_train,Y_test=train_test_split(X,Y,test_size=0.2,random_state=0)

#fitting multiple linear regression to training set
from sklearn.linear_model import LinearRegression
regressor=LinearRegression()
regressor.fit(X_train, Y_train)

#predicating the test results
y_pred=regressor.predict(X_test)

#building optimal model using backward elimination
import statsmodels.api as sm
X=np.append(arr=np.ones((50,1)).astype(int), values=X, axis=1)
X_opt=X[:,[0,1,2,3,4,5]]
regressor1=sm.OLS(endog=Y,exog=X_opt).fit()
"""regressor1.summary()  ---write in console"""