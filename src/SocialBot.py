
# This is a social media bot
# That will post your favorite quotes into social media
# Currently supported social media : Twitter
import tweetpy

credential_list = ["CONSUMER_KEY", "CONSUMER_SECRET", "ACCESS_KEY", "ACCESS_SECRET"]
credential_list = ["CONSUMER_KEY", "CONSUMER_SECRET", "ACCESS_KEY", "ACCESS_SECRET"]
use_environment_variables = bool
use_file_variables = bool
amount_of_credentials = len(credential_list)
credential_counter = 0

CONSUMER_KEY = str
CONSUMER_SECRET = str
ACCESS_KEY = str
ACCESS_SECRET = str

for credential in credential_list:
    if credential_list[0] in os.environ:
        credential_counter += 1

if credential_counter == amount_of_credentials:
    logging.info("All environment variables were found!")
    use_environment_variables = True
    use_file_variables = False
else:
    logging.warning("Environment variables were not successfully found!")
    logging.info("Using credentials.py instead.")
    use_environment_variables = False
    use_file_variables = True

if use_environment_variables == True:
    logging.info("Using environment variables.")
    CONSUMER_KEY = os.environ['CONSUMER_KEY']
    CONSUMER_SECRET = os.environ['CONSUMER_SECRET']
    ACCESS_KEY = os.environ['ACCESS_KEY']
    ACCESS_SECRET = os.environ['ACCESS_SECRET']
elif use_file_variables == True:
    logging.info("Using file variables.")
    try:
        from credentials import *
    except ImportError:
        logging.critical("An error occured while importing the credentials from the credentials.py file.")
        logging.critical("The bot will now shut down.")
        logging.info("Please check the README.md file for more information.")
        exit()


class SocialBot:
    def __init__(self):        
        self.credential_list = ["CONSUMER_KEY", "CONSUMER_SECRET", "ACCESS_KEY", "ACCESS_SECRET"]
        self.CONSUMER_KEY = ''
        self.CONSUMER_SECRET = ''
        self.ACCESS_KEY = ''
        self.ACCESS_SECRET = ''
    
    def signin(self):
        pass