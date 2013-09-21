import sys
import json

def main():
    sentiment_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    
    sentiment_scores = {} # initialize an empty dictionary
    
    for line in sentiment_file:
        term, score = line.split("\t") # The file is tab-delimited. "\t" means "tab character"
        sentiment_scores[term] = int(score)  # Convert the score to an integer.

    for line in tweet_file:
        # Convert the line to a JSON object so we can process it
        tweet = json.loads(line)
        
        # Check if the tweet has the "text" key.
        if 'text' in tweet:
            #if tweet['lang'] == 'en':
                tweet_text = tweet['text'].encode('utf-8')
                
                # Make the tweet text all lower case in case there are some words with capitals, which wouldn't match our dict keys
                tweet_text_lower = tweet_text.lower()
                
                sentiment_sum = 0
                terms = tweet_text_lower.split()
                for term in terms:
                    if term in sentiment_scores:
                        sentiment_sum += sentiment_scores[term]
                    
                #print '<' + tweet_text + ' : ' + str(sentiment_sum) + '>'
                print sentiment_sum

        
if __name__ == '__main__':
    main()
