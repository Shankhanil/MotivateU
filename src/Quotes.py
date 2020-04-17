#!/usr/bin/python
import requests
import json

class Quotes:

    def __init__(self):
        pass
    
    def getQuote(self):
        """
        Returns a random Quote
        
        Parameters
        ----------
        none
        """
        url = "https://quote-garden.herokuapp.com/api/v2/quotes/random"
        response = requests.get(url)
        data = response.text
        parsed = json.loads(data)
        quote = json.dumps(parsed, indent = 4)
        return quote