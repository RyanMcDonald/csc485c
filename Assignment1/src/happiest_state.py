'''
Created on Sep 22, 2013

@author: Ryan
'''
import sys
import json
import re

if __name__ == '__main__':
    sentiment_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    
    sentiment_scores = {} # initialize an empty dictionary
    
    state_sentiments = {
        'AL': 0,
        'AK': 0,
        'AZ': 0,
        'AR': 0,
        'CA': 0,
        'CO': 0,
        'CT': 0,
        'DE': 0,
        'DC': 0,
        'FL': 0,
        'GA': 0,
        'HI': 0,
        'ID': 0,
        'IL': 0,
        'IN': 0,
        'IA': 0,
        'KS': 0,
        'KY': 0,
        'LA': 0,
        'ME': 0,
        'MD': 0,
        'MA': 0,
        'MI': 0,
        'MN': 0,
        'MS': 0,
        'MO': 0,
        'MT': 0,
        'NE': 0,
        'NV': 0,
        'NH': 0,
        'NJ': 0,
        'NM': 0,
        'NY': 0,
        'NC': 0,
        'ND': 0,
        'OH': 0,
        'OK': 0,
        'OR': 0,
        'PA': 0,
        'RI': 0,
        'SC': 0,
        'SD': 0,
        'TN': 0,
        'TX': 0,
        'UT': 0,
        'VT': 0,
        'VA': 0,
        'WA': 0,
        'WV': 0,
        'WI': 0,
        'WY': 0
    }
    
    regex = re.compile('.*, (..)$')
    
    for line in sentiment_file:
        term, score = line.split("\t") # The file is tab-delimited. "\t" means "tab character"
        sentiment_scores[term] = int(score)  # Convert the score to an integer.

    for line in tweet_file:
        # Convert the line to a JSON object so we can process it
        tweet = json.loads(line)
        
        # Check if the tweet has the "text" key.
        if 'text' in tweet:
            if tweet['lang'] == 'en':
                sentiment_sum = 0
                
                tweet_text = tweet['text'].encode('utf-8')
                
                # Make the tweet text all lower case in case there are some words with capitals, which wouldn't match our dict keys
                tweet_text_lower = tweet_text.lower()
                
                terms = tweet_text_lower.split()
                
                # If any term ends with punctuation such as period, exclamation mark, question mark, then remove the punctuation.
                for i in range(len(terms)):
                    terms[i] = terms[i].rstrip('.!?,:;-')
                    
                for term in terms:
                    if term in sentiment_scores:
                        sentiment_sum += sentiment_scores[term]
                    
                # Find out what state the tweet came from
                tweet_place = tweet['place']
                tweet_user = tweet['user']
                
                if tweet_place is not None:
                    match = regex.match(tweet_place['full_name'])
                    if match is not None:
                        if match.group(1) in state_sentiments:
                            state_sentiments[match.group(1)] += sentiment_sum
                            continue
                        
                match = regex.match(tweet_user['location'])
                if match is not None:
                    #print match.group(1)
                    if match.group(1) in state_sentiments:
                            state_sentiments[match.group(1)] += sentiment_sum
                            continue
    
    happiestState = ''
    unhappiestState = ''
    highestSentiment = 0
    lowestSentiment = 0
    
    for state in state_sentiments:
        if state_sentiments[state] > highestSentiment:
            happiestState = state
            highestSentiment = state_sentiments[state]
        if state_sentiments[state] < lowestSentiment:
            unhappiestState = state
            lowestSentiment = state_sentiments[state]
            
    
    print happiestState + " " + str(highestSentiment)
    #print "Unhappiest: " + unhappiestState + " " + str(lowestSentiment)