#!/usr/bin/python
import requests
import json

class Quotes:

    def __init__(self):
        pass
    
    def generateRandomQuote(self):
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
        quoteJSON = json.dumps(parsed, indent = 4)
        return quoteJSON
        
    def getQuote(self, quoteJSON):
        # quoteJSON = self.generateRandomQuote()
        quote = "abc"
        quoteAuthor = "def"
        return (quote, quoteAuthor)
        
    def formatQuote(self, quoteTuple):
    # Format quote for printing 
        pass
        
    def DonateAQuote(self, quote, author):
    # Have a Quote? Donate the quote to 
        pass