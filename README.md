# Polynomial-Regression
Regression
<br/>

Polynomial Regression is a form of linear regression in which the relationship between the independent variable x and dependent variable y is modelled as an nth-degree polynomial. Polynomial regression fits a nonlinear relationship between the value of x and the corresponding conditional mean of y, denoted E(y | x). In this article, we’ll go in-depth about polynomial regression.
<br/>

**What is a Polynomial Regression?** <br/>
* There are some relationships that a researcher will hypothesize is curvilinear. Clearly, such types of cases will include a polynomial term.

* Inspection of residuals. If we try to fit a linear model to curved data, a scatter plot of residuals (Y-axis) on the predictor (X-axis) will have patches of many positive residuals in the middle. Hence in such a situation, it is not appropriate.

* An assumption in the usual multiple linear regression analysis is that all the independent variables are independent. In the polynomial regression model, this assumption is not satisfied.
<br/>

**Why Polynomial Regression?** <br/>
Polynomial regression is a type of regression analysis used in statistics and machine learning when the relationship between the independent variable (input) and the dependent variable (output) is not linear. While simple linear regression models the relationship as a straight line, polynomial regression allows for more flexibility by fitting a polynomial equation to the data. <br/>
When the relationship between the variables is better represented by a curve rather than a straight line, polynomial regression can capture the non-linear patterns in the data. <br/>
<br/>

**How does a Polynomial Regression work?** <br/>
1. **The choice of the polynomial degree (n)** is a crucial aspect of polynomial regression. A higher degree allows the model to fit the training data more closely, but it may also lead to overfitting, especially if the degree is too high. Therefore, the degree should be chosen based on the complexity of the underlying relationship in the data.
2. The polynomial regression model is trained to **find the coefficients** that minimize the difference between the predicted values and the actual values in the training data.
3. Once the model is trained, it can be used to make predictions on new, unseen data. The polynomial equation captures the non-linear patterns observed in the training data, allowing the model to generalize to non-linear relationships. <br/>
<br/>

**Implementation** <br/>
1. Data Preparation <br/>
Before applying polynomial regression, data should be preprocessed, which includes:
* Data Cleaning: Handling missing values, outliers, and irrelevant features.
* Feature Scaling: Normalizing or standardizing data if needed.
  
2. Creating Polynomial Features <br/>
To implement polynomial regression, transform the original features into polynomial features.

3. Model Fitting <br>
Use a linear regression model on the transformed polynomial features. Libraries like scikit-learn in Python provide built-in functions to create polynomial features and fit the model.

4. Evaluation <br/>
Evaluate the model using metrics like:
* Mean Squared Error (MSE): Measures the average squared difference between the predicted and actual values.
* R-squared: Indicates the proportion of variance in the dependent variable that is predictable from the independent variable(s).
