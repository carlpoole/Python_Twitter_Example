from twitter import *
import re

# --- oAuth Information -----------------------------------------------

OAUTH_TOKEN		    = ''
OAUTH_SECRET		= ''
CONSUMER_KEY		= ''
CONSUMER_SECRET	    = ''

# ---------------------------------------------------------------------

class Carltwitter:

    def __init__(self,OAUTH_TOKEN,OAUTH_SECRET,CONSUMER_KEY,CONSUMER_SECRET):

        # Some color constants for formatting
        self.BLUE		= '\033[94m'
        self.GREEN		= '\033[92m'
        self.RED		= '\033[91m'
        self.MAGENTA	= '\033[95m'
        self.ENDCOLOR	= '\033[0m'

        # Some regex pattern compilations for coloring usernames and hashtags
        self.reUser 	= re.compile(r"(?<=^|(?<=[^a-zA-Z0-9-\.]))@([A-Za-z_]+[A-Za-z0-9_]+)")
        self.reHashtag	= re.compile(r"(?<=^|(?<=[^a-zA-Z0-9-\.]))#([A-Za-z_]+[A-Za-z0-9_]+)")

        # Setup Twitter API
        self.t = Twitter(auth=OAuth(OAUTH_TOKEN, OAUTH_SECRET, CONSUMER_KEY, CONSUMER_SECRET))

    def printLastTweet(self, username):

        try:
            timeline = self.t.statuses.user_timeline(screen_name=username,count=1)

            print '\n'.join({self.BLUE + '@' + tweet['user']['screen_name'] + self.ENDCOLOR + ": "
                             + re.sub(self.reUser, self.RED + r'@\1' + self.ENDCOLOR,
                                      re.sub(self.reHashtag, self.GREEN + r'#\1' + self.ENDCOLOR,tweet['text']))
                             for tweet in timeline})
        except:
            print 'There was a problem getting tweets for ' + username + '. Please try again!'

    def printUserSummary(self, username):

        try:
            print 'do something'
        except:
            print 'error text here'

        def printTendingTopics(self):

            try:
                print 'do something'
            except:
                print 'error text here'

if __name__ == "__main__":
    username = raw_input("Enter a twitter @ username:")
    ct = Carltwitter(OAUTH_TOKEN,OAUTH_SECRET,CONSUMER_KEY,CONSUMER_SECRET)
    ct.printLastTweet(username)
