import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
import matplotlib.pyplot as plt

switch=True
df=pd.read_csv("https://raw.githubusercontent.com/stedy/Machine-Learning-with-R-datasets/master/insurance.csv")
x = df[["age","sex","bmi","children","smoker"]]

x=pd.get_dummies(data=x, drop_first=True)
y = df[["charges"]]

x_train, x_test, y_train, y_test = train_test_split(x, y, train_size = 0.8, test_size = 0.2, random_state=6)

lm=LinearRegression()

lm.fit(x_train.values,y_train)


y_predict=lm.predict(x_test.values)

plt.scatter(y_test,y_predict)

while switch:
    try:
        age=int(input("How old are you? -----> "))
        if age<=0:
            print("Wrong input, please try again.")
        elif age>0:
            switch=False
    except:
        print("Wrong input, please try again.")
    
    

switch=True

while switch:
    try:
        sex=int(input("What is your sex? (Male is 1 and female is 0) -----> "))
        if sex!=0 and sex!=1:
            print("Wrong input, please try again.")
        else:
            switch=False
    except:
        print("Wrong input, please try again.")

switch=True

while switch:
    try:
        bmi=float(input("What is your BMI? -----> "))
        if bmi<=0:
            print("Wrong input, please try again.")
        elif bmi>0:
            switch=False
    except:
        print("Wrong input, please try again.")
    

switch=True

while switch:
    try:
        children=int(input("How many children do you have? -----> "))
        if children<=0:
            print("Wrong input, please try again.")
        elif children>0:
            switch=False
    except:
        print("Wrong input, please try again.")
    

switch=True

while switch:
    try:
        smoker=int(input("Do you smoke on a regular basis? (1 = yes, 0 = no) -----> "))
        if smoker!=0 and smoker!=1:
            print("Wrong input, please try again.")
        else:
            switch=False
    except:
        print("Wrong input, please try again.")
    



sampledata=[[age,sex,bmi,children,smoker]]
predict=lm.predict(sampledata)
print("Health insurance will cost approximately: $%.2f" % predict)
#print(lm.score(x_train.values,y_train))
#print(lm.score(x_test.values,y_test))



#plt.show()


