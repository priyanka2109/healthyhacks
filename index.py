import tweepy
import sys

class MyStreamListener(tweepy.StreamListener):
    def on_status(self,status):
        count=0
        while count<4:
            print(status.text)
            count=count+1

        
    def on_error(self,status_code):
        cnt=0
        while cnt<4:
            print(status_code)
            cnt=cnt+1
        


consumer_key="XZlNv3ff7wMPdZQZx3fB1GKVK"
consumer_secret="zYTqErmiQDHYWH7mZyAFgrUbNYK6xsDrYRBwU3IqN3yRn6AG6o"
access_token="923811743062663168-4JpwdWOQlSo3hPqS6RtmGqOmuMjuhq6"
access_token_secret="2utCRjt5FgCGv8jWfs7EzEBsmtOlVtoflPJ5j1PSjeWX1"


auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

if (not api):
    print("Authentication failed!")
    sys.exit(-1)

myStreamListener = MyStreamListener()
myStream = tweepy.Stream(auth = api.auth, listener=myStreamListener)
myStream.filter(track=["news"])