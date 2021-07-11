# Multiple_Regression_in_ML
Regression is a type of supervised learning. It is a statistical method used in finance, investing,
and other disciplines that attempts to determine the strength and character of the relationship between one dependent variable (usually denoted by Y)
and a series of other variables (known as independent variables).



We have a dataset of 50 start-up companies. This dataset contains five main information: R&D Spend, Administration Spend, Marketing Spend, State, and Profit for a financial year. Our goal is to create a model that can easily determine which company has a maximum profit, and which is the most affecting factor for the profit of a company.







5 Methods of building a model

1.All-in

2.Backward Elimination

3.Forward Selection

4.Bidirectional Elimination

5.Score Comparison



In this we use Backward elimination which is a feature selection technique while building a machine learning model. It is used to remove those features that do not have
a significant effect on the dependent variable or prediction of output.
Steps of Backward Elimination
Below are some main steps which are used to apply backward elimination process:

Step-1: Firstly, We need to select a significance level to stay in the model. (SL=0.05)


Step-2: Fit the complete model with all possible predictors/independent variables.

Step-3: Choose the predictor which has the highest P-value, such that.

If P-value >SL, go to step 4.
Else Finish, and Our model is ready.
Step-4: Remove that predictor.

Step-5: Rebuild and fit the model with the remaining variables.



we get summary


![image](https://user-images.githubusercontent.com/85051683/125206511-5183b780-e2a5-11eb-9efa-d867c175eddd.png)


In the above image, we can clearly see the p-values of all the variables. Here x1, x2 are dummy variables, x3 is R&D spend, x4 is Administration spend, and x5 is Marketing spend.

From the table, we will choose the highest p-value, which is for x1=0.953 Now, we have the highest p-value which is greater than the SL value, so will remove the x1 variable (dummy variable) from the table and will refit the model. 

By doing above steps we finally get 
![image](https://user-images.githubusercontent.com/85051683/125206550-88f26400-e2a5-11eb-9ab8-5b5671590a1b.png)

As we can see in the above output image, only two variables are left. So only the R&D independent variable is a significant variable for the prediction. So we can now predict efficiently using this variable.


