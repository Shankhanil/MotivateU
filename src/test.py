#!/usr/bin/python

# QuoteGarden by Prathamesh More
# MotivateU by Shankhanil, Chhanda

# from Quotes import Quotes
from exoAPI import exoREST
if __name__ == "__main__":
    api = exoREST()
    api.addAPI_URL(url_name = 'randomQuote', url = 'https://quote-garden.herokuapp.com/api/v2/quotes/random')
    # api.getURL_LIST()
    print(api.getDataAsJSON(url_name = 'randomQuote'))
    