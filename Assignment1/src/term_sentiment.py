import sys
import json

def main():
    sentiment_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    
    sentiment_scores = {} # initialize an empty dictionary
    
    # This is a dictionary of arrays with [0] being positive tweets containing that term, and [1] being negative.
    zero_sentiment_terms = {}
    
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
                
                # If the term ends with any punctuation such as period, exclamation mark, question mark, then remove it
                for i in range(len(terms)):
                    terms[i] = terms[i].rstrip('.!?,:;-')
                
                # First, add all terms without a sentiment score to the zero_sentiment_scores dictionary,
                # while at the same time calculating the total sentiment of the tweet.
                for term in terms:
                    if term not in sentiment_scores:
                        if term not in zero_sentiment_terms:
                            zero_sentiment_terms[term] = [0, 0]
                    else:
                        sentiment_sum += sentiment_scores[term]
                        
                # Next, we go through the list of terms in the tweet and, if the term has zero sentiment, we
                # add 1 to index 0 of the zero_sentiment_terms[term] array if the sentiment_sum is positive.
                # Similarly, add 1 to index 1 if the sentiment_sum is negative.
                for term in terms:
                    if term in zero_sentiment_terms:
                        if sentiment_sum > 0:
                            zero_sentiment_terms[term][0] += 1
                        elif sentiment_sum < 0:
                            zero_sentiment_terms[term][1] += 1
                
    # Go through the zero_sentiment_terms and calculate the sentiment value based on the number of positive and negative
    # tweets that the term was a part of.
    for term in zero_sentiment_terms:
        is_negative_sentiment = zero_sentiment_terms[term][0] < zero_sentiment_terms[term][1]
        
        prefix = ""
        if is_negative_sentiment:
            prefix = "-"
            
        # If the negative count is 0, just ignore it and only use the positive count.
        if zero_sentiment_terms[term][1] != 0:
            # If the positive count is 0, just ignore it and only use the negative count.
            if zero_sentiment_terms[term][0] == 0:
                print term + " " + prefix + str(float(zero_sentiment_terms[term][1]))
                
            # Otherwise, get the ratio of positive / negative counts to obtain the sentiment value.
            else:
                print term + " " + prefix + str(float(zero_sentiment_terms[term][0]) / float(zero_sentiment_terms[term][1]))
        else:
            print term + " " + prefix + str(float(zero_sentiment_terms[term][0]))

if __name__ == '__main__':
    main()
