
# This is a social media bot
# That will post your favorite quotes into social media
# Currently supported social media : Twitter
# Upcoming bot support : Whatsapp


import tweepy
import os

class SocialBot:
    def __init__(self, platform = 'twitter'):
        self.use_environment_variables = False
        self.credential_list = ["CONSUMER_KEY", "CONSUMER_SECRET", "ACCESS_KEY", "ACCESS_SECRET"]
        self.CONSUMER_KEY = ''
        self.CONSUMER_SECRET = ''
        self.ACCESS_KEY = ''
        self.ACCESS_SECRET = ''
        self.platform = platform
        self.api = None
        self.user = None
    
    def init_bot(self):
        counter = 0
        for credential in self.credential_list:
            if credential in os.environ:
                counter += 1
                
        if counter == len(self.credential_list):
            self.use_environment_variables = True
            
    def get_credentials(self):
        if self.use_environment_variables == True:
            self.CONSUMER_KEY = os.environ['CONSUMER_KEY']
            self.CONSUMER_SECRET = os.environ['CONSUMER_SECRET']
            self.ACCESS_KEY = os.environ['ACCESS_KEY']
            self.ACCESS_SECRET = os.environ['ACCESS_SECRET']
        elif self.use_file_variables == True:
            try:
                # from credentials import Credentials
                pass
            except ImportError:
                print("An error occured.")
                print("The bot will not shut down.")
                self.setup_credentials()
                
    def setup_credentials(self):
        exit()
    
    def user_info(self,api, user):
        print("Username: {}".format(self.api.get_user(self.user.id).screen_name))
        print("Display Name: {}".format(self.user.name))
        
    def login(self, successMessage):
        # Initialize the bot and get user credentials
        self.init_bot()
        self.get_credentials()

        # Then try logging in
        if self.platform == 'twitter':
            try:
                auth = tweepy.OAuthHandler(self.CONSUMER_KEY, self.CONSUMER_SECRET)
                auth.set_access_token(self.ACCESS_KEY, self.ACCESS_SECRET)
                self.api = tweepy.API(auth)
                self.user = self.api.me()
                self.user_info(self.api, self.user)
                print(successMessage)
        
            except tweepy.TweepError:
                print("There's an authentication error!!!")
                exit()
            
    def post(self, post, successMessage):
        if self.platform == 'twitter':
            try:
                self.api.update_status(post[0:140])
                print(successMessage)
            except:
                print("Sorry, unable to post. An error occured")