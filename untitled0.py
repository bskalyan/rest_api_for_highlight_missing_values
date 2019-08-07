# -*- coding: utf-8 -*-
"""
Created on Tue Jul 16 13:33:44 2019

@author: b.sudheendra.kalyan
"""

#from flask import Flask
import pandas as pd
from pandas import ExcelWriter
from pandas import ExcelFile
import xlwt
import openpyxl
import json
from flask import Flask,request,jsonify


app = Flask(__name__)


@app.route("/hello",methods=['POST'])
def hello():
    file=request.get_json()
    url=file['url']
    #url = "C:/Users/b.sudheendra.kalyan/Desktop/missing/excel/PythonExport.xlsx"
    result=[]
    print(url)
    df = pd.read_excel(url)
    df = pd.read_excel('PythonExport.xlsx', sheetname='Sheet5')
    df.style.highlight_null(null_color='green')
    df.style.highlight_null(null_color='green').to_excel('styled.xlsx', engine='openpyxl')
    for i, row in enumerate(df.values):
        if pd.isnull(row[1]):
            print(row[0])
            result.append(row[0])
    
        
    return jsonify(result)


if __name__ == '__main__':
    app.run(host='127.0.0.1',port=5005,debug=True)