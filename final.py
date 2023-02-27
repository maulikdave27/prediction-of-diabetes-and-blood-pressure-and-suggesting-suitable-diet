from sklearn import metrics
import pandas as pd
#import requests
import pywhatkit as kt
import PySimpleGUI as sg

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

from sklearn.ensemble import RandomForestClassifier


data = pd.read_csv("diabetes.csv")
data.head()


data.isnull().sum()


h = data.pop("Pregnancies")
h = data.pop("SkinThickness")


y = data.pop("Outcome")
X = data
# X=X.to_numpy()
# y=y.to_numpy()


data.head()
# df1 = data


X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.31, random_state=2432423121)


scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)


clf = RandomForestClassifier(max_depth=7, random_state=25)
clf.fit(X_train, y_train)


predic = clf.predict(X_test)
g = metrics.accuracy_score(y_test, predic)
h = round(g*100)
#print(round(g*100, 2))


data1 = pd.read_csv("bp.csv")
data1.head()
data1 = data1.drop(index=[0, 800])


data1.pop("id")
data1.pop('gender')
data1.pop('gluc')
# data.pop('active')
data1.pop('w')
y1 = data1.pop("cardio")


X1 = data1

data1.head()


# df2 = data1

X_train1, X_test1, y_train1, y_test1 = train_test_split(
    X1, y1, test_size=0.31, random_state=121212121)


scaler = StandardScaler()
X_train_scaled1 = scaler.fit_transform(X_train1)
X_test_scaled1 = scaler.transform(X_test1)

clf1 = RandomForestClassifier(max_depth=9, random_state=12121212)
clf1.fit(X_train1, y_train1)


predic1 = clf1.predict(X_test1)
g = metrics.accuracy_score(y_test1, predic1)
#rint(round(g*100, 2))




sg.theme('Black')   # Add a touch of color
# All the stuff inside your window.
layout = [  
            [sg.Text('NAME: '), sg.InputText()],
            [sg.Text('AGE: '),sg.InputText()],
            [sg.Text('Enter the following health details: ')],
            [sg.Text('INSULIN: '),sg.InputText()],
            [sg.Text('GLUCOSE: '),sg.InputText()],
            [sg.Text('BP VALUE: '),sg.InputText()],
            [sg.Text('HEIGHT: '),sg.InputText()],
            [sg.Text('WEIGHT: '),sg.InputText()],
            [sg.Text('DPT: '),sg.InputText()],
            [sg.Text('AP HI: '),sg.InputText()],
            [sg.Text('AP LOW: '),sg.InputText()],
            [sg.Text('CHOLESTROL: '),sg.InputText()],
            [sg.Text('SMOKE[0 if no or 1 if yes]: '),sg.InputText()],
            [sg.Text('ALCOHOL[0 if no or 1 if yes]: '),sg.InputText()],
            [sg.Text('ACTIVE[0 if no or 1 if yes]: '),sg.InputText()],
            [sg.Text('DIABETES[0 if no or 1 if yes]: '),sg.InputText()],
            [sg.Text('CARDIOVASCULAR DISEASE[0 if no or 1 if yes]: '),sg.InputText()],
            [sg.Text('\n\n\n')],
            [sg.Text('MENU:\nEnter 1 for RICE\nEnter 2 for POTATO\nEnter 3 for MAIZE\nEnter 4 for YAMS\nEnter 5 for SORGHUM\nEnter 6 for CASSAVA\n ')],
            [sg.Text('CHOICE: '),sg.InputText()],
            [sg.Button('Generate'), sg.Button('Cancel')] ]

# Create the Window
window = sg.Window('DIET RECOMENDATION PLAN', layout)
# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Cancel': # if user closes window or clicks cancel
        break
    
    name=values[0]
    age=values[1]
    age=int(age)
    insuline=values[2]
    insuline=int(insuline)
    glucose=values[3]
    glucose=int(glucose)
    blood_pressure=values[4]
    blood_pressure=int(blood_pressure)
    height=values[5]
    height=int(height)
    weight=values[6]
    weight=int(weight)
    dpf=values[7]
    dpf=float(dpf)
    ap_hi=values[8]
    ap_hi=int(ap_hi)
    ap_lo=values[9]
    ap_lo=int(ap_lo)
    cholestrol=values[10]
    cholestrol=int(cholestrol)
    smoke=values[11]
    smoke=int(smoke)
    alco=values[12]
    alco=int(alco)
    active=values[13]
    active=int(active)
    sugr=values[14]
    sugr=int(sugr)
    bld_prs=values[15]
    bld_prs=int(bld_prs)
    food=values[16]
    food=int(food)
    break
window.close()
h=height/100
bmi=weight/(h*h)
def recommend_food(disease, food):
    if disease == "diabetes":
        
        global result_1
        a=0
        if food == "rice":
            result_1 =  "According to our Health Engin You are prone to Diabetes. therefore it is recommended to take half a cup of rice per meal for diabetes."
        elif food == "wheat":
            result_1 =  " According to our Health Engin You are prone to Diabetes. therefore it is recommended to take one cup of wheat per meal for diabetes."
        elif food == "potato":
            result_1 =  " According to our Health Engin You are prone to Diabetes. therefore it is recommended to take one medium sized potato per meal for diabetes."
        elif food == "maize":
            result_1 =  " According to our Health Engin You are prone to Diabetes. therefore it is recommended to take half a cup of maize per meal for diabetes."
        elif food == "yams":
            result_1 =  " According to our Health Engin You are prone to Diabetes. therefore it is recommended to take half a cup of yams per meal for diabetes."
        elif food == "sorghum":
            result_1 =  " According to our Health Engin You are prone to Diabetes. therefore it is recommended to take half a cup of sorghum per meal for diabetes."
        elif food == "cassava":
            result_1 =  " According to our Health Engin You are prone to Diabetes. therefore it is recommended to take one medium sized cassava per meal for diabetes."
        else:
            result_1 =  "Invalid food choice. Please choose from rice, wheat, potato, maize, yams, sorghum, or cassava."

        layout = [
                    [sg.Text(result_1)],
                    [sg.Button('Close')]
                 ]
        window = sg.Window('YOUR OPTIMISED DIET', layout)

        while True:
            event, values = window.read()
            if event == sg.WIN_CLOSED or event == 'Close': # if user closes window or clicks cancel
                break

        window.close()


    elif disease == "blood pressure":
        
        global result_2
        
        if food == "rice":
            result_2 =  "According to our Health Engin You are prone to blood Pressure. t is recommended to take half a cup of rice per meal for blood pressure."
        elif food == "wheat":
            result_2 =  " According to our Health Engin You are prone to blood Pressure. therefore it is recommended to take one cup of wheat per meal for blood pressure."
        elif food == "potato":
            result_2 =  " According to our Health Engin You are prone to blood Pressure. therefore it is recommended to take one medium sized potato per meal for blood pressure."
        elif food == "maize":
            result_2 =  " According to our Health Engin You are prone to blood Pressure. therefore it is recommended to take half a cup of maize per meal for blood pressure."
        elif food == "yams":
            result_2 =  " According to our Health Engin You are prone to blood Pressure. therefore it is recommended to take half a cup of yams per meal for blood pressure."
        elif food == "sorghum":
            result_2 =  " According to our Health Engin You are prone to blood Pressure. therefore it is recommended to take half a cup of sorghum per meal for blood pressure."
        elif food == "cassava":
            result_2 =  " According to our Health Engin You are prone to blood Pressure. therefore it is recommended to take one medium sized cassava per meal for blood pressure."
        else:
            result_2 =  "Invalid food choice. Please choose from rice, wheat, potato, maize, yams, sorghum, or cassava."
        layout = [
                    [sg.Text(result_2)],
                    [sg.Button('Close')]
                 ]
        window = sg.Window('YOUR OPTIMISED DIET', layout)

        while True:
            event, values = window.read()
            if event == sg.WIN_CLOSED or event == 'Close': # if user closes window or clicks cancel
                break

        window.close()

    

    elif disease == "NaN":
        
        global result_3
        
        if food == "rice":
            result_3 = "Recommended amount: 1 cup per serving. Rice is a good source of complex carbohydrates and is easy to digest. There is no hesitation to consume rice."
        elif food == "wheat":
            result_3 = "Recommended amount: 1/2 cup per serving. Wheat is a good source of fiber. However, it's important to limit your intake of gluten if you have an autoimmune condition. There is no hesitation to consume wheat."
        elif food == "potato":
            result_3 = "Recommended amount: 1 medium-sized potato per serving. Potatoes are a good source of vitamin C, which can help support the immune system. But be mindful of the portion size and prepare them in a healthy way. There is no hesitation to consume potato."
        elif food == "maize":
            result_3 = "Recommended amount: 1/2 cup per serving. Maize is a good source of carbohydrates. It's important to limit your intake if you have an autoimmune condition as it may contain gluten. There is no hesitation to consume maize."
        elif food == "yams":
            result_3 = "Recommended amount: 1 medium-sized yam per serving. Yams are a good source of potassium and fiber. There is no hesitation to consume yams."
        elif food == "sorghum":
            result_3 = "Recommended amount: 1/2 cup per serving. Sorghum is a good source of carbohydrates and contains antioxidants. It is gluten-free, which can be beneficial for people with autoimmune conditions. There is no hesitation to consume sorghum."
        elif food == "cassava":
            result_3 = "Recommended amount: 1 medium-sized cassava per serving. Cassava is a good source of carbohydrates. It's important to limit your intake if you have an autoimmune condition as it may contain gluten. There is no hesitation to consume cassava."
        
      

        layout = [
                    [sg.Text(result_3)],
                    [sg.Button('Close')]
                 ]
        window = sg.Window('YOUR OPTIMISED DIET', layout)

        while True:
            event, values = window.read()
            if event == sg.WIN_CLOSED or event == 'Close': # if user closes window or clicks cancel
                break
        
        window.close()

    else:
        layout = [
            [sg.Text("Sorry cant find data")],
                    [sg.Button('Close')]
                    ]
        window = sg.Window('YOUR OPTIMISED DIET', layout)
        while True:
            event, values = window.read()
            if event == sg.WIN_CLOSED or event == 'Close': # if user closes window or clicks cancel
                break
        
        window.close()  


# Value Model

patient_data_ML1=[glucose, blood_pressure, insuline,bmi , dpf, age]



patient_data_ML2 = [age, height, weight, ap_hi,ap_lo, cholestrol, smoke, alco, active]





if sugr==1 and bld_prs==0:
    predic1 = clf1.predict([patient_data_ML2])
    print(predic1)
    conclusion2 = predic1[0]

if bld_prs==1 and bld_prs==0:
    predic = clf.predict([patient_data_ML1])
    print(predic)
    conclusion1 = predic[0]
if bld_prs==1 and sugr==1:
    conclusion1=1 
    conclusion2=1

else:
    predic = clf.predict([patient_data_ML1])
    print(predic)
    predic1 = clf1.predict([patient_data_ML2])
    print(predic1)
    conclusion1 = predic[0]
    conclusion2 = predic1[0]



if conclusion1 == 1:
    disease = "diabetes"
else:
    disease = "NaN"

if conclusion2 == 1:
    disease1 = "blood pressure"
else:
    disease1 = "NaN"


list_foods = ["rice", "potato", "maize", "yams", "sorghum", "cassava"]
if food==1:
    food='rice'
elif food==2:
    food="potato"
elif food==3:
    food="maize"
elif food==4:
    food="yams"
elif food==5:
    food="sorghum"
elif food==6:
    food="cassa"


recommend_food(disease, food)
recommend_food(disease1, food)

food
if (food != 'NaN' and disease != 'NaN'):
    
    target = food + ' and '+disease
    kt.search(target)

elif (food != 'NaN' and disease == 'NaN'):
    target = 'how much ' + food + ' should i consume on daily basis '
    kt.search(target)


if (food != 'NaN' and disease1 != 'NaN'):

    target = food + ' and '+disease1
    kt.search(target)

elif (food != 'NaN' and disease1 == 'NaN'):
    target = ' how much ' + food + ' should i consume on daily basis '
    kt.search(target)



