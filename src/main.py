#!/usr/bin/python

# QuoteGarden by Prathamesh More
# MotivateU by Shankhanil, Chhanda

from Quotes import Quotes, Quotes2
from license import License
from SocialBot import SocialBot
import sys

if __name__ == "__main__":
    
    quote = Quotes2()
    tweetbot = SocialBot()
    # cli_command = cliCommands.analyse(sys.argv[1:])
    try:
        if sys.argv[1] == 'quote':
            try:
                quote.formatQuote(quote.getQuote(quote.generateQuote(author = sys.argv[2])))
            except:
                print('Here\'s a random quote for you')
                Q = quote.formatQuote(quote.getQuote(quote.generateQuote()))
                print(Q)
                print("Like this quote? Want to tweet it? (Y/n)")
                choice = input()
                if choice == 'y' or choice == 'Y':
                    tweetbot.login()
                    tweetbot.post(Q, successMessage = "You've just tweeted an awesome Quote!")
                    
        elif sys.argv[1] == 'donate':
            print("Donation of Quotes is under construction. Will be operational soon")
            pass
    except:
        # print(sys.exc_info())
        print('''Pls use \'python src/main.py quote\' to get a quote\n'''\
            '''Use \'python src/main.py donate\' to donate a quote to QuoteGarden API
            ''');