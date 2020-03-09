import tweepy
import keys
import io
import os
import wget
import json
from PIL import Image

#malhinoah, johnmulaneybot, TheGoldenRatio4
def vision_feed(image_list, username):

    data = {}
    data['tweets'] = []
    tweet_texts = []
    success = 0
  
    try:
        auth = tweepy.OAuthHandler(keys.consumer_key, keys.consumer_secret)
        auth.set_access_token(keys.access_token, keys.access_token_secret)
        api = tweepy.API(auth)
        public_tweets = api.user_timeline(screen_name = username, count = 20, include_rts =True)
        
        for tweet in public_tweets:
          
            media_files = set()
            media = tweet.entities.get('media', [])
            if(len(media) > 0):
                media_files.add(media[0]['media_url'])  
                tweet_texts.append((tweet.text, 1)) 
                
            else:
                tweet_texts.append((tweet.text, 0))
        
            for media_file in media_files:
                test = wget.download(media_file)
                image_list.append(test)
        success = 1
        return (image_list, tweet_texts, success)
 
    except ValueError:
            success = 0
            with open('tweetson.json') as json_file:
                data_parse = json.load(json_file)
                for tweets in data_parse['twittertest']:
                    tweet_texts.append(str(tweets['Tweet']))
                    #if (str(tweets['Image']) != 0):
                        #test = wget.download(str(tweets['Image']))
                        #image_list.append(test)
                    
            
            return(image_list, tweet_texts, success)
