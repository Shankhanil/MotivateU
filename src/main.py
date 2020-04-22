#!/usr/bin/python

# QuoteGarden by Prathamesh More
# MotivateU by Shankhanil, Chhanda

from Quotes import Quotes, Quotes2
from license import License
from SocialBot import SocialBot
import sys


class UnknownCommandException(Exception):
    pass
    
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
                    if len(Q) > 140:
                        print('''\
                            This quote is more than 140 characters long.\n\
                            This tweet will be truncated to 140 characters.\n\
                            Proceed? (Y/n):''')
                        choice2 = input()
                        if choice2 == 'y' or choice2 =='Y' :
                            tweetbot.post(Q, successMessage = "You've just tweeted an awesome Quote!")
                        elif choice2 == 'n' or choice2 == 'N':
                            pass
                        else:
                            raise UnknownCommandException("Unknown choice {}".format(choice2))
                    else:
                        tweetbot.post(Q, successMessage = "You've just tweeted an awesome Quote!")
        elif sys.argv[1] == 'donate':
            print("Donation of Quotes is under construction. Will be operational soon")
            pass
        else:
            raise UnknownCommandException("Unknown command {}".format(sys.argv[1]))
    
    except IndexError:
        print('''\nPls use \'python src/main.py quote\' to get a quote\n'''\
            '''Use \'python src/main.py donate\' to donate a quote to QuoteGarden API
            ''');
    except UnknownCommandException:
        print("\n{} is not a known MotivateU command".format(sys.argv[1]))