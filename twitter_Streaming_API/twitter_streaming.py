try:
    import json
except ImportError:
    import simplejson as json

# Import the necessary methods from "twitter" library
from twitter import Twitter, OAuth, TwitterHTTPError, TwitterStream


# Variables that contains the user credentials to access Twitter API
ACCESS_TOKEN = '1008737228166594560-4h4YeV2P0xHXMVyFsGGatnweV7OEQJ'
ACCESS_SECRET = 'VDTC8tD2YMQhNSnxdTELfwVXTRZcofJxZqZ6GA6lZTtop'
CONSUMER_KEY = 'CDC5ThtbeOg9wz5RO1lfQ96ba'
CONSUMER_SECRET = 'fLvpGKK3o1mo3onKyMWi6FFMtKeAwT70qKoxhjpylc8FRBHJDo'

oauth = OAuth(ACCESS_TOKEN, ACCESS_SECRET, CONSUMER_KEY, CONSUMER_SECRET)

# Initiate the connection to Twitter Streaming API
twitter_userstream = TwitterStream(auth=oauth, domain='userstream.twitter.com')
twitter_stream = TwitterStream(auth=oauth, domain='stream.twitter.com')

# Get a sample of the public data following through Twitter
#parameter
#follow	        optional	A comma separated list of user IDs, indicating the users to return statuses for in the stream. See follow for more information.
#track	        optional	Keywords to track. Phrases of keywords are specified by a comma-separated list. See track for more information.
#locations	    optional	Specifies a set of bounding boxes to track. See locations for more information.
#delimited	    optional	Specifies whether messages should be length-delimited. See delimited for more information.
#stall_warnings	optional	Specifies whether stall warnings should be delivered. See stall_warnings for more information.

iterator = twitter_stream.statuses.filter(track='#ถ้าหลวง')

# Print each tweet in the stream to the screen
# Here we set it to stop after getting 1000 tweets.
# You don't have to set it to stop, but can continue running
# the Twitter API to collect data for days or even longer.
tweet_count = 1000
for tweet in iterator:
    tweet_count -= 1
    # Twitter Python Tool wraps the data returned by Twitter
    # as a TwitterDictResponse object.
    # We convert it back to the JSON format to print/score
    print(json.dumps(tweet))

    # The command below will do pretty printing for JSON data, try it out
    # print json.dumps(tweet, indent=4)

    if tweet_count <= 0:
        break
