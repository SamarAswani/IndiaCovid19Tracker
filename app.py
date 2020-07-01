#IMPORTS
import csv
import os
from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session, jsonify, url_for
from flask_session import Session
from tempfile import mkdtemp
import hashlib
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from pprint import pprint
import csv
import requests
import urllib
import pandas as pd

# scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]
# creds = ServiceAccountCredentials.from_json_keyfile_name("creds.json", scope)
# client = gspread.authorize(creds)
# sheetState = client.open("state_wise").sheet1
# sheetDistrict = client.open("district_wise").sheet1


# data = sheet.get_all_records()
# pprint(data)

app = Flask(__name__) #APPLICATION CREATED

@app.route("/index",methods=['POST','GET'])
def index():
    if request.method == "POST":
        district = request.form.get("distrctSearch")
        dataDistrict = pd.read_csv("https://api.covid19india.org/csv/latest/district_wise.csv")
        for i in range(1, 763):
            if dataDistrict["District"][i] == district:
                place = i

        districtInfo = [dataDistrict["District"][place], dataDistrict["Active"][place], dataDistrict["Confirmed"][place], dataDistrict["Recovered"][place], dataDistrict["Deceased"][place]]
        return render_template("district.html", districtInfo=districtInfo)

    # try:
    #     os.remove("state_wise.csv")
    #     os.remove("district_wise.csv")
    # except(FileNotFoundError):
    #     pass
    #url = "https://api.covid19india.org/csv/latest/state_wise.csv"
    #response = urllib.request.urlopen(url)
    #with open('state_wise.csv', 'w') as f:
        #writer = csv.writer(f)
        #for line in response.iter_lines():
            #writer.writerow(line.decode('utf-8').split(','))

    # url1 = "https://api.covid19india.org/csv/latest/district_wise.csv"
    # response = requests.get(url1)
    # with open('district_wise.csv', 'w') as f:
    #     writer = csv.writer(f)
    #     for line in response.iter_lines():
    #         writer.writerow(line.decode('utf-8').split(','))


    # contentState = open('state_wise.csv','r').read()
    # contentDistrict = open('district_wise.csv','r').read()
    # client.import_csv("1SCCloYWFwmBPVyG_szUxMcuApJaGLg4jRxTGvqsBkzI", contentState)
    # client.import_csv("1Vzi_2XOreu70TACgZpgXsnvDLFbTDaxEBIdUniBsFYU", contentDistrict)

    # dataState = sheetState.get_all_records()
    # dataDistrict = sheetDistrict.get_all_records()

    # pprint(dataState)
    # pprint(dataDistrict)

    else:
        dataState = pd.read_csv("https://api.covid19india.org/csv/latest/state_wise.csv")
        stateCases = []
        total = {}
        total[dataState["State"][0]]= dataState["Active"][0]
        for i in range(1, 38):
            temp = [dataState["State"][i], dataState["Active"][i], dataState["Confirmed"][i], dataState["Recovered"][i], dataState["Deaths"][i]]
            stateCases.append(temp)




        return render_template("index.html", stateCases=stateCases, total=total)
