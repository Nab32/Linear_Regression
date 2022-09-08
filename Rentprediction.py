import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
import matplotlib.pyplot as plt


switch=True
df=pd.read_csv("https://raw.githubusercontent.com/Codecademy/datasets/master/streeteasy/queens.csv")
x = df[['bedrooms', 'bathrooms', 'size_sqft', 'floor']]

y = df[['rent']]

x_train, x_test, y_train, y_test = train_test_split(x, y, train_size = 0.8, test_size = 0.2, random_state=6)

lm = LinearRegression()

model = lm.fit(x_train.values, y_train)


while switch:
    try:
        bedrooms=int(input("How many bedrooms? --> "))
        if bedrooms<=0:
            print("Wrong input, please try again.")
        elif bedrooms>0:
            switch=False
    except:
        print("Wrong input, please try again.")

switch=True

while switch:
    try:
        bathrooms=int(input("How many bathrooms? --> "))
        if bathrooms<=0:
            print("Wrong input, please try again.")
        elif bathrooms>0:
            switch=False
    except:
        print("Wrong input, please try again.")

switch=True

while switch:
    try:
        size=int(input("The size of the building in sqft? --> "))
        if size<=0:
            print("Wrong input, please try again.")
        elif size>0:
            switch=False
    except:
        print("Wrong input, please try again.")
        
switch=True

while switch:
    try:
        floor=int(input("How many floors? --> "))
        if floor<=0:
            print("Wrong input, please try again.")
        elif floor>0:
            switch=False
    except:
        print("Wrong input, please try again.")



userx=[[bedrooms,bathrooms,size,floor]]

y_predict= lm.predict(userx)

print("The rent will cost approximately: $%.2f" % y_predict)
#print(lm.score(x_train.values,y_train))
#print(lm.score(x_test.values,y_test))


