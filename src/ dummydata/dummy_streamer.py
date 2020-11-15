#coding:utf-8
import json


def getDummyData():
    f = open('./dummysData.json', 'r')
    jsonData = json.load(f)
    f.close()
    return jsonData