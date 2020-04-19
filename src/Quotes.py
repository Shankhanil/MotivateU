#!/usr/bin/python
import requests
import json
from exoAPI import exoREST

class Quotes:

    def __init__(self):
        pass
    
    def generateQuote(self, author = 'random'):
        parsed = {}
        if author == 'random':
            url = "https://quote-garden.herokuapp.com/api/v2/quotes/random"
        response = requests.get(url)
        data = response.text
        parsed = json.loads(data)
        return parsed
        
    def getQuote(self, quoteJSON):
        quote = quoteJSON['quote']['quoteText']
        quoteAuthor = quoteJSON['quote']['quoteAuthor']
        return (quote, quoteAuthor)
        
    def formatQuote(self, quoteTuple):
    # Format quote for printing 
        print('''\n
        {}\n\t\t\t---{}
        '''.format(quoteTuple[0], quoteTuple[1]))
        pass
        
    def DonateAQuote(self, quote, author):
    # Have a Quote? Donate the quote to 
        pass
        
class Quotes2:
    '''
    A Quotes v2.0 : using the exoAPI interface
    '''
    def __init__(self):
        self.api = exoREST()
    
    def generateQuote(self, author = 'random'):
        self.api.addAPI_URL(url_name = 'randomQuote', \
            url = 'https://quote-garden.herokuapp.com/api/v2/quotes/random')
        
        return self.api.getDataAsJSON(url_name = 'randomQuote', \
                method = 'get', outputformat = 'json')
        
    def getQuote(self, quoteJSON):
        params = ['quote/quoteText', 'quote/quoteAuthor']
        
        [quote, quoteAuthor] = self.api.getDataFromJSON(quoteJSON, params)
        
        # quote = quoteJSON['quote']['quoteText']
        # quoteAuthor = quoteJSON['quote']['quoteAuthor']
        return [quote, quoteAuthor]
        
    def formatQuote(self, quoteTuple):
    # Format quote for printing 
        print('''\n
        {}\n\t\t\t---{}
        '''.format(quoteTuple[0], quoteTuple[1]))
        pass
        
    def DonateAQuote(self, quote, author):
    # Have a Quote? Donate the quote to 
        pass