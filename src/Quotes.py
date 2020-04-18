#!/usr/bin/python
import requests
import json

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