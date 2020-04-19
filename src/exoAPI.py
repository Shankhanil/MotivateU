#!/usr/bin/python
import requests
import json

'''
An REST API interface. 
It supports the following functions
    1. set up a list of API urls,                       : addAPI_URL
    2. get data in JSON format from the API urls        : getDataAsJSON
    3. extract specific data from the JSON data format  : getDataFromJSON
'''
class exoREST:

    def __init__(self):
        self.url_list = {}
    
    def addAPI_URL(self, url_name, url):
        if url_name not in self.url_list.keys():
            self.url_list[url_name] = url
        else:
            print("try a different url name")
            
    def getURL_LIST(self):
        for url_name in self.url_list.keys():
            print(url_name, self.url_list[url_name])
            
    def getDataAsJSON(self, url_name, method = 'get', outputformat = 'json'):
        url = self.url_list[url_name]
        parsed = {}
        response = None
        if method == 'get':
            response = requests.get(url)
        data = response.text
        parsed = json.loads(data)
        if outputformat == 'json':
            return parsed
        if outputformat == 'str':
            return json.dump(parsed)

    def getDataFromJSON(self, JSONdict, parameters):
        '''
            parameters: JSON data parameters, which will be
                        used to access JSON data 
                type: LIST
                format:
                    param1/param2,
                        where param1 is upper hierarchy
                              param2 is lower hierarchy
                              
                CAUTION: ONLY hierarchy upto level 2 is supported
        '''
        data = []
        for p in parameters:
            _p0 = (p.split('/'))[0]
            try:
                _p1 = (p.split('/'))[1]
                data.append(JSONdict[_p0][_p1])
            except:
                data.append(JSONdict[_p0])
        return data