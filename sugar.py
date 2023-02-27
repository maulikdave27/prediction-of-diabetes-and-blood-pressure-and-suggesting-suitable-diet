
import numpy
import pandas as pd 


data= pd.read_csv("diabetes.csv")
data.head()


data.isnull().sum()


h=data.pop("Pregnancies")
h=data.pop("SkinThickness")


y=data.pop("Outcome")
X=data
#X=X.to_numpy()
#y=y.to_numpy()


data.head()



from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test= train_test_split(X,y,test_size=0.30,random_state=2432423121)



from sklearn.ensemble import RandomForestClassifier
clf = RandomForestClassifier(max_depth=7, random_state=121212)
clf.fit(X, y)


'''predic=clf.predict(X_test)
from sklearn import metrics
g=metrics.accuracy_score(y_test,predic)
print(round(g*100,2))'''