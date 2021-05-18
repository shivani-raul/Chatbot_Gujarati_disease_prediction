
import os
import glob
import pyrebase
import json
from flask import Flask, render_template, request, redirect, url_for, abort
from Final_Find_Symptoms import diseasePredict
app = Flask(__name__)

config = {
    "apiKey": "AIzaSyAVKJcWh09xvfMvod0mkkCf4hIBOpNY130",
    "authDomain": "chatbot-5f8d6.firebaseapp.com",
    "databaseURL": "https://chatbot-5f8d6-default-rtdb.firebaseio.com",
    "projectId": "chatbot-5f8d6",
    "storageBucket": "chatbot-5f8d6.appspot.com",
    "messagingSenderId": "821404467705",
    "appId": "1:821404467705:web:02a36d5dd10922f07d7d28",
    "measurementId": "G-0QRN4XBX83"
}

firebase = pyrebase.initialize_app(config)
db = firebase.database()
data = db.child("diseases").get().val()
data2 =[]
top = {}
for i in range(len(data)):
    data1 = dict(list(data.items())[i][1])
    data2.append(data1['predicted'])
for ds in data2:
    top[ds] = data2.count(ds)
@app.route('/')
def index():
    return render_template('index.html',files=top)


@app.route('/', methods=['GET', 'POST'])
def disease():

    if request.method == 'POST':
        symptoms = request.form['inp']
        output = diseasePredict(symptoms)
        maxp=output[1].index(max(output[1]))
        out_1 = output[0][maxp]+"  "+str(round(output[1][maxp],2))+"%"
        out_2 = output[2]
        db.child("diseases").push({"symptoms":symptoms,"predicted":output[0][maxp],"percentage":round(output[1][maxp],2)})
        return render_template('index.html', files=top, file1=out_1,file2=out_2)
    else:
        return render_template('index.html',files=top)


if __name__ == '__main__':
    app.run(debug=True)
