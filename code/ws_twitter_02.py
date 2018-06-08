import twitter
import json

def oauth_login():
    # XXX: Go to http://twitter.com/apps/new to create an app and get values
    # for these credentials that you'll need to provide in place of these
    # empty string values that are defined as placeholders.
    # See https://dev.twitter.com/docs/auth/oauth for more information 
    # on Twitter's OAuth implementation.
    
    CONSUMER_KEY = ''
    CONSUMER_SECRET = '
    OAUTH_TOKEN = ''
    OAUTH_TOKEN_SECRET = ''
    
    auth = twitter.oauth.OAuth(OAUTH_TOKEN, OAUTH_TOKEN_SECRET,
                               CONSUMER_KEY, CONSUMER_SECRET)
    
    twitter_api = twitter.Twitter(auth=auth)
    return twitter_api

# Sample usage
twitter_api = oauth_login()    


# Code taken from: Mining the Social Web, 2nd Edition (O'Reilly)


def twitter_trends(twitter_api, woe_id):
    # Prefix ID with the underscore for query string parameterization.
    # Without the underscore, the twitter package appends the ID value
    # to the URL itself as a special-case keyword argument.
    return twitter_api.trends.place(_id=woe_id)

# woe_id numbers can ce looked up at: http://woeid.rosselliot.co.nz 

# The woeid for the Glasgow is 21125

GLASGOW_WOE_ID = 21125
glasgow_trends = twitter_trends(twitter_api, GLASGOW_WOE_ID)
print json.dumps(glasgow_trends, indent=1) 
