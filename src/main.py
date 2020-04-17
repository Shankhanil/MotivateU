#!/usr/bin/python

# QuoteGarden by Prathamesh More
# MotivateU by Shankhanil, Chhanda

from Quotes import Quotes
from license import License
from SocialBot import SocialBot

if __name__ == "__main__":
    
    quote = Quotes()
    # try:
    bot = SocialBot()
    bot.login()
    # except 
    # print("Here's a motivational quote from a bot" + quote.generateRandomQuote())