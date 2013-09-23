'''
Created on Sep 22, 2013

@author: Ryan
'''
import sys
import json
from operator import itemgetter

if __name__ == '__main__':
    tweet_file = open(sys.argv[1])
    
    hashtag_counts = {} # initialize an empty dictionary

    for line in tweet_file:
        # Convert the line to a JSON object so we can process it
        tweet = json.loads(line)
        
        if 'entities' in tweet:
            if tweet['lang'] == 'en':
                tweet_hashtags = tweet['entities']['hashtags']
                    
                for hashtag in tweet_hashtags:
                    # Make sure the hashtag is all lower case so we don't run into any case issues
                    hashtag_text = hashtag['text'].lower()
                    if hashtag_text in hashtag_counts:
                        hashtag_counts[hashtag_text] += 1.0
                    else:
                        hashtag_counts[hashtag_text] = 1.0
    
    # Put the counts into a list so we can sort it to find the top 10
    top_ten = []
    for hashtag in hashtag_counts:
        top_ten.append((hashtag, hashtag_counts[hashtag]))
    
    # Sort the list by counts
    top_ten.sort(key=itemgetter(1, 0), reverse=True)
    
    for i in range(0, 10):
        print top_ten[i][0].encode('utf-8') + " " + str(top_ten[i][1])