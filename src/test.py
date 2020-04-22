#!/usr/bin/python

# QuoteGarden by Prathamesh More
# MotivateU by Shankhanil, Chhanda

# from Quotes import Quotes
from exoAPI import exoREST
if __name__ == "__main__":
    api = exoREST()
    api.addAPI_URL(url_name = 'author', url = 'https://quote-garden.herokuapp.com/api/v2/authors/Carl%20Sandburg')
    # api.getURL_LIST()
    x = api.getDataAsJSON(url_name = 'author')
    gen = api.JSONTraverser(x)
    for g in next(gen):
        print(g)
        