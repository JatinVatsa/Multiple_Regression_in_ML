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




