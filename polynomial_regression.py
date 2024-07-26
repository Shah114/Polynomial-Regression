# Importing Libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Importing the dataset
data = pd.read_csv('data.csv')

# Features and the target variables
x = data.iloc[:, 1:2].values
y = data.iloc[:, 2].values

# Fitting Linear Regression to the dataset
from sklearn.linear_model import LinearRegression
lin = LinearRegression()
lin.fit(x, y)

# Fitting Polynomial Regression to the dataset
from sklearn.preprocessing import PolynomialFeatures

poly = PolynomialFeatures(degree=4)
x_poly = poly.fit_transform(x)

poly.fit(x_poly, y)
lin2 = LinearRegression()
lin2.fit(x_poly, y)

# Visualising the Linear Regression results
plt.scatter(x, y, color='blue')
plt.plot(x, lin.predict(x), color='red')
plt.title('Linear Regression')
plt.xlabel('Temperature')
plt.ylabel('Pressure')
plt.show()

# Visualising the Polynomial Regression results
plt.scatter(x, y, color='blue')
plt.plot(x, lin2.predict(poly.fit_transform(x)),
         color='red')
plt.title('Polynomial Regression')
plt.xlabel('Temperature')
plt.ylabel('Pressure')
plt.show()

'''
Predicting a new result with Linear Regression
after converting predict variable to 2D array
'''
pred = 100.0
predarray = np.array([[pred]])
prediction = lin2.predict(poly.fit_transform(predarray))
print(f"Prediction: {prediction}")