#!/usr/bin/python

# QuoteGarden by Prathamesh More
# MotivateU by Shankhanil, Chhanda

from Quotes import Quotes
from license import License
from SocialBot import SocialBot
import sys

if __name__ == "__main__":
    
    quote = Quotes()
    # cli_command = cliCommands.analyse(sys.argv[1:])
    try:
        if sys.argv[1] == 'quote':
            quote.formatQuote(quote.getQuote(quote.generateQuote()))
        elif sys.argv[1] == 'donate':
            print("Donation of tweets is under construction. Will be operational soon")
            pass
    except:
        print('''Pls use \'python src/main.py quote\' to get a quote\n'''\
            '''Use \'python src/main.py donate\' to donate a quote to QuoteGarden API
            ''');