'''
Created on Sep 22, 2013

@author: Ryan
'''
import sys
import json

if __name__ == '__main__':
    tweet_file = open(sys.argv[1])
    
    term_frequencies = {} # initialize an empty dictionary
    total_term_count = 0.0

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
                    # If the term is in our dictionary, increment its frequency count
                    if term in term_frequencies:
                        term_frequencies[term] += 1
                        
                    # Otherwise add the term to the dictionary
                    else:
                        term_frequencies[term] = 1
                        
                    total_term_count += 1.0
        
    for frequency in term_frequencies:
        print frequency + " " + str(term_frequencies[frequency] / total_term_count)